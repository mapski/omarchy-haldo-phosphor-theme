#!/usr/bin/env python3
"""Preview or explicitly apply the optional Phosphor workstation profile."""
import argparse
from copy import deepcopy
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
STRING = r'"(?:\\.|[^"\\])*"'


def read_jsonc(text):
    # Match strings first so URLs, comment-like strings, and escaped quotes stay intact.
    clean = re.sub(f'({STRING})|//[^\\n]*|/\\*[\\s\\S]*?\\*/',
                   lambda m: m.group(1) if m.group(1) is not None else '\n' * m.group().count('\n'), text)
    clean = re.sub(f'({STRING})|,(\\s*[}}\\]])',
                   lambda m: m.group(1) if m.group(1) is not None else m.group(2), clean)
    value = json.loads(clean)
    if not isinstance(value, dict):
        raise ValueError('configuration must be a JSON object')
    return value


def build_profile(shell, menu):
    shell, menu = deepcopy(shell), deepcopy(menu)
    proposed = json.loads((ROOT / 'profiles/workstation.json').read_text())
    old_bar = shell.setdefault('bar', {})
    existing = {item['id']: item for items in old_bar.get('layout', {}).values()
                for item in items if isinstance(item, dict) and 'id' in item}
    for section, items in proposed['layout'].items():
        for index, item in enumerate(items):
            merged = deepcopy(existing.get(item['id'], {}))
            if item['id'] == 'omarchy.agents':
                providers = deepcopy(merged.get('providers', {}))
                for provider in providers.values():
                    provider['enabled'] = False
                for name, settings in item['providers'].items():
                    providers[name] = {**providers.get(name, {}), **settings}
                merged.update(item)
                merged['providers'] = providers
            else:
                merged.update(item)
            proposed['layout'][section][index] = merged
    # Rebuild native defaults, retaining only already-placed third-party/custom
    # widgets. Their section, relative order and per-widget settings survive.
    for section, items in old_bar.get('layout', {}).items():
        if section not in proposed['layout']:
            continue
        for position, item in enumerate(items):
            if isinstance(item, dict) and isinstance(item.get('id'), str) and not item['id'].startswith('omarchy.'):
                target = proposed['layout'][section]
                target.insert(min(position, len(target)), deepcopy(item))
    old_bar.update(proposed)
    if 'disabledPlugins' in shell:
        disabled = shell['disabledPlugins']
        if not isinstance(disabled, list) or any(not isinstance(item, str) for item in disabled):
            raise ValueError('disabledPlugins must be an array of plugin IDs')
        shell['disabledPlugins'] = [item for item in disabled
                                    if item not in ('omarchy.clock', 'omarchy.system-update')]
    shell.setdefault('version', 1)
    menu.update(json.loads((ROOT / 'profiles/menu.json').read_text()))
    return shell, menu


def atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='.phosphor-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='write configuration after private backups')
    args = parser.parse_args()
    home = Path.home()
    # Match the native shell/menu contract, which reads HOME/.config directly.
    config = home / '.config/omarchy'
    paths = [config / 'shell.json', config / 'extensions/omarchy-menu.jsonc']
    try:
        for path in [*paths, config / 'phosphor-backups']:
            if path.is_symlink() or any(p.is_symlink() for p in path.parents if p != Path('/')):
                raise ValueError(f'symlink path requires manual configuration: {path}')
        originals = [path.read_bytes() if path.exists() else None for path in paths]
        omarchy = Path(os.environ.get('OMARCHY_PATH', '/usr/share/omarchy'))
        shell = read_jsonc(originals[0].decode() if originals[0] is not None else
                           (omarchy / 'config/omarchy/shell.json').read_text())
        menu = read_jsonc(originals[1].decode()) if originals[1] is not None else {}
        updated = build_profile(shell, menu)
        rendered = [(json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode() for value in updated]
        if not args.apply:
            print('Preview: top bar; one Agents widget (Codex + Claude); two Agents menu launchers.')
            print('Existing unrelated settings and default agent will be preserved.')
            print('JSONC comments will be normalized to JSON; exact originals are backed up on apply.')
            print('Run again with --apply to write these two files:')
            for path in paths:
                print(path)
            return 0
        backup_root = config / 'phosphor-backups'
        backup_root.mkdir(parents=True, exist_ok=True, mode=0o700)
        backup = backup_root / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
        backup.mkdir(mode=0o700)
        for path, original in zip(paths, originals):
            if original is not None:
                atomic_write(backup / path.name, original)
            else:
                atomic_write(backup / (path.name + '.missing'), b'Originally absent\n')
        written = []
        try:
            for path, data in zip(paths, rendered):
                atomic_write(path, data)
                written.append(path)
        except OSError:
            for path, original in zip(paths, originals):
                if path not in written:
                    continue
                if original is None:
                    path.unlink()
                else:
                    atomic_write(path, original)
            raise
        print('Applied workstation profile. Exact originals saved privately in:')
        print(backup)
        return 0
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        print(f'Cannot apply Phosphor profile: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
