#!/usr/bin/env python3
"""Validate theme assets; optionally exercise installed Omarchy in a temporary HOME."""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import struct
import subprocess
import tempfile
import tomllib

ROOT = Path(__file__).resolve().parents[1]


def luminance(value):
    rgb = [int(value[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in rgb]
    return sum(c * weight for c, weight in zip(linear, (.2126, .7152, .0722)))


def contrast(a, b):
    low, high = sorted([luminance(a), luminance(b)])
    return (high + .05) / (low + .05)


def static_checks():
    palette = tomllib.loads((ROOT / 'colors.toml').read_text())
    for key, value in palette.items():
        if key != 'mode':
            assert re.fullmatch(r'#[0-9a-fA-F]{6}', value), f'Invalid palette value: {key}'
    for role in ['foreground', 'dark_foreground', 'accent', 'muted', 'red', 'yellow', 'orange',
                 'green', 'cyan', 'blue', 'magenta', 'bright_foreground']:
        for surface in ['background', 'lighter_background', 'selection']:
            ratio = contrast(palette[role], palette[surface])
            assert ratio >= 4.5, f'{role} on {surface}: {ratio:.2f}:1 below 4.5:1'
    for path in ROOT.glob('shell.*.toml'):
        tomllib.loads(path.read_text())
    for path in (ROOT / 'profiles').glob('*.json'):
        json.loads(path.read_text())
    wallpapers = list((ROOT / 'backgrounds').glob('*.png'))
    assert len(wallpapers) == 2, 'Two original wallpapers required'
    for path in wallpapers:
        data = path.read_bytes()
        assert data[:8] == b'\x89PNG\r\n\x1a\n'
        assert struct.unpack('>II', data[16:24]) == (3840, 2160), path.name
    forbidden = ['*.lua', 'alacritty.toml', 'foot.ini', 'ghostty.conf', 'kitty.conf', 'vscode.json']
    for pattern in forbidden:
        assert not list(ROOT.glob(pattern)), f'Executable theme override shipped: {pattern}'
    for directory in [ROOT, ROOT / 'backgrounds', ROOT / 'profiles']:
        assert not any(path.is_symlink() for path in directory.iterdir()), 'Symlink in theme assets'
    print(f'Static checks passed: palette contrast >=4.5:1, {len(list(ROOT.glob("shell.*.toml")))} shell sections, 2 wallpapers.')


def native_checks(keep=False):
    omarchy = Path(os.environ.get('OMARCHY_PATH', '/usr/share/omarchy'))
    assert (omarchy / 'bin/omarchy-theme-set').exists(), 'Installed Omarchy required for --native'
    home = Path(tempfile.mkdtemp(prefix='phosphor-native-'))
    try:
        source = home / '.config/omarchy/themes/haldo-phosphor'
        shutil.copytree(ROOT, source, ignore=shutil.ignore_patterns('.git', '.validation', '__pycache__'))
        # Exercise exactly the installed-from-Git branch in native staging.
        (source / '.git').mkdir()
        env = dict(os.environ, HOME=str(home), XDG_CONFIG_HOME=str(home / '.config'),
                   XDG_STATE_HOME=str(home / '.local/state'), XDG_CACHE_HOME=str(home / '.cache'),
                   OMARCHY_PATH=str(omarchy), OMARCHY_THEME_HEADLESS='1',
                   PATH=str(omarchy / 'bin') + os.pathsep + os.environ['PATH'])
        result = subprocess.run([str(omarchy / 'bin/omarchy-theme-set'), 'haldo-phosphor'], env=env,
                                capture_output=True, text=True)
        assert result.returncode == 0, result.stdout + result.stderr
        stage = home / '.local/state/omarchy/current/theme'
        generated = [p for p in stage.iterdir() if p.is_file()]
        for path in generated:
            if path.suffix in ['.toml', '.json', '.lua', '.theme', '.conf', '.ini', '.yaml']:
                assert '{{' not in path.read_text(), f'Unresolved placeholder in {path.name}'
        shell = tomllib.loads((stage / 'shell.toml').read_text())
        assert shell['font']['base-size'] == 13
        assert shell['bar']['size-horizontal'] == 30
        assert shell['controls']['focus-border-width'] == 2
        assert shell['menu']['selected-text'] == '#9BCC9C'
        assert shell['lock']['border-error'] == '#E38D83'
        claude = json.loads((stage / 'claude.json').read_text())
        assert claude['overrides']['claude'] == '#9BCC9C'
        assert claude['overrides']['diffAdded'] != claude['overrides']['diffRemoved']
        for filename in ['alacritty.toml', 'foot.ini', 'kitty.conf', 'ghostty.conf',
                         'neovim.lua', 'helix.toml', 'hyprland.lua', 'hermes.yaml', 'pi.json', 't3code.json']:
            assert (stage / filename).is_file(), f'Missing native output {filename}'
        for filename in ['alacritty.toml', 'helix.toml']:
            tomllib.loads((stage / filename).read_text())
        profile = subprocess.run([os.environ.get('PYTHON', 'python3'), str(ROOT / 'scripts/workstation.py'), '--apply'],
                                 env=env, capture_output=True, text=True)
        assert profile.returncode == 0, profile.stderr
        print(f'Native imported-theme staging, generated app configs, shell states and isolated profile apply passed ({len(generated)} files).')
        if keep:
            print(f'Kept isolated HOME: {home}')
    finally:
        if not keep:
            shutil.rmtree(home)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--native', action='store_true')
    parser.add_argument('--keep', action='store_true', help='keep isolated native HOME for runtime review')
    args = parser.parse_args()
    static_checks()
    if args.native:
        native_checks(args.keep)


if __name__ == '__main__':
    main()
