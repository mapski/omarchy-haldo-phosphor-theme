import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class WorkstationProfileTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)
        self.omarchy = self.home / 'packaged-omarchy'
        defaults = self.omarchy / 'config/omarchy/shell.json'
        defaults.parent.mkdir(parents=True)
        defaults.write_text(json.dumps({'version': 1, 'idle': {'screensaver': 150, 'lock': 300}, 'bar': {}}))
        self.config = self.home / '.config/omarchy'
        (self.config / 'extensions').mkdir(parents=True)
        self.shell_path = self.config / 'shell.json'
        self.menu_path = self.config / 'extensions/omarchy-menu.jsonc'
        self.original_shell = {
            'version': 1, 'idle': {'lock': 617}, 'plugins': ['custom.plugin'],
            'bar': {'customOption': True, 'layout': {
                'left': [{'id': 'omarchy.agents'}],
                'right': [{'id': 'omarchy.agents', 'refreshIntervalSec': 30}],
            }},
        }
        self.shell_path.write_text(json.dumps(self.original_shell))
        self.menu_path.write_text('''{
          // Preserve URL and escaped quotes inside this string.
          "personal": {"label": "Personal", "description": "https://example.org/a//b \\\"note\\\"",},
          /* existing custom menu */
        }''')

    def run_profile(self, *args, config_home=None):
        env = dict(os.environ, HOME=str(self.home), XDG_CONFIG_HOME=str(config_home or self.home / '.config'), OMARCHY_PATH=str(self.omarchy))
        return subprocess.run([sys.executable, str(ROOT / 'scripts/workstation.py'), *args],
                              env=env, capture_output=True, text=True)

    def apply(self):
        result = self.run_profile('--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(self.shell_path.read_text()), json.loads(self.menu_path.read_text())

    def test_preview_does_not_write(self):
        before = self.shell_path.read_bytes(), self.menu_path.read_bytes()
        result = self.run_profile()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Preview', result.stdout)
        self.assertEqual(before, (self.shell_path.read_bytes(), self.menu_path.read_bytes()))
        self.assertFalse((self.config / 'phosphor-backups').exists())

    def test_apply_preserves_unrelated_settings_and_jsonc_strings(self):
        shell, menu = self.apply()
        self.assertEqual(shell['idle'], {'lock': 617})
        self.assertEqual(shell['plugins'], ['custom.plugin'])
        self.assertTrue(shell['bar']['customOption'])
        self.assertEqual(menu['personal']['description'], 'https://example.org/a//b "note"')

    def test_one_agents_widget_and_two_named_launchers(self):
        shell, menu = self.apply()
        agents = [item for section in shell['bar']['layout'].values()
                  for item in section if item['id'] == 'omarchy.agents']
        self.assertEqual(len(agents), 1)
        self.assertEqual(agents[0]['refreshIntervalSec'], 900)
        self.assertEqual(agents[0]['syncMode'], 'Off')
        self.assertTrue(agents[0]['providers']['codex']['enabled'])
        self.assertTrue(agents[0]['providers']['claude']['enabled'])
        self.assertFalse(agents[0]['providers']['fireworks']['enabled'])
        self.assertEqual(menu['phosphor.codex']['action'], 'omarchy-launch-terminal codex')
        self.assertEqual(menu['phosphor.claude']['action'], 'omarchy-launch-terminal claude')
        self.assertNotIn('phosphor.hermes', menu)
        self.assertFalse((self.config / 'defaults/agent').exists())

    def test_reapply_is_idempotent(self):
        self.apply()
        before = self.shell_path.read_bytes(), self.menu_path.read_bytes()
        self.apply()
        self.assertEqual(before, (self.shell_path.read_bytes(), self.menu_path.read_bytes()))

    def test_centered_am_pm_clock_and_update_indicator(self):
        self.original_shell['disabledPlugins'] = ['omarchy.clock', 'omarchy.system-update', 'custom.disabled']
        self.shell_path.write_text(json.dumps(self.original_shell))
        shell, _ = self.apply()
        self.assertEqual(shell['bar']['centerAnchor'], 'omarchy.clock')
        clocks = [item for item in shell['bar']['layout']['center'] if item['id'] == 'omarchy.clock']
        self.assertEqual(len(clocks), 1)
        self.assertEqual(clocks[0]['format'], 'ddd h:mm AP')
        updates = [item for section in shell['bar']['layout'].values()
                   for item in section if item['id'] == 'omarchy.system-update']
        self.assertEqual(len(updates), 1)
        self.assertNotIn('omarchy.clock', shell['disabledPlugins'])
        self.assertNotIn('omarchy.system-update', shell['disabledPlugins'])
        self.assertIn('custom.disabled', shell['disabledPlugins'])

    def test_private_backups_preserve_exact_originals(self):
        original = self.shell_path.read_bytes(), self.menu_path.read_bytes()
        self.apply()
        backups = list((self.config / 'phosphor-backups').iterdir())
        self.assertEqual(len(backups), 1)
        backup = backups[0]
        self.assertEqual((backup / 'shell.json').read_bytes(), original[0])
        self.assertEqual((backup / 'omarchy-menu.jsonc').read_bytes(), original[1])
        self.assertEqual(backup.stat().st_mode & 0o777, 0o700)
        self.assertEqual((backup / 'shell.json').stat().st_mode & 0o777, 0o600)

    def test_preserves_existing_third_party_widgets_and_their_settings(self):
        self.original_shell['bar']['layout'] = {
            'left': [{'id': 'omarchy.menu'}, {'id': 'custom.launcher', 'mode': 'compact'}, {'id': 'omarchy.workspaces'}],
            'center': [{'id': 'custom.media', 'options': {'scroll': False}}, {'id': 'omarchy.clock'}],
            'right': [{'id': 'custom.auth', 'iconOnly': True}, {'id': 'omarchy.agents'}, {'id': 'custom.sync'}],
        }
        self.shell_path.write_text(json.dumps(self.original_shell))
        shell, _ = self.apply()
        layout = shell['bar']['layout']
        self.assertEqual(layout['left'][1], {'id': 'custom.launcher', 'mode': 'compact'})
        self.assertEqual(layout['center'][0], {'id': 'custom.media', 'options': {'scroll': False}})
        self.assertEqual(layout['right'][0], {'id': 'custom.auth', 'iconOnly': True})
        self.assertEqual(layout['right'][2], {'id': 'custom.sync'})
        first = self.shell_path.read_bytes()
        self.apply()
        self.assertEqual(first, self.shell_path.read_bytes())

    def test_invalid_menu_leaves_both_files_untouched(self):
        self.menu_path.write_text('{ broken')
        before = self.shell_path.read_bytes(), self.menu_path.read_bytes()
        result = self.run_profile('--apply')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(before, (self.shell_path.read_bytes(), self.menu_path.read_bytes()))
        self.assertFalse((self.config / 'phosphor-backups').exists())

    def test_symlink_input_is_rejected_before_any_write(self):
        target = self.home / 'external.json'
        target.write_text(self.shell_path.read_text())
        self.shell_path.unlink()
        self.shell_path.symlink_to(target)
        menu_before = self.menu_path.read_bytes()
        result = self.run_profile('--apply')
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(self.shell_path.is_symlink())
        self.assertEqual(self.menu_path.read_bytes(), menu_before)

    def test_missing_configs_use_packaged_defaults_and_preserve_idle(self):
        self.shell_path.unlink()
        self.menu_path.unlink()
        shell, menu = self.apply()
        self.assertEqual(shell['idle'], {'screensaver': 150, 'lock': 300})
        self.assertIn('phosphor.codex', menu)

    def test_writes_the_home_config_path_used_by_native_omarchy(self):
        alternate = self.home / 'other-config'
        result = self.run_profile('--apply', config_home=alternate)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((alternate / 'omarchy/shell.json').exists())
        shell = json.loads(self.shell_path.read_text())
        agents = [item for section in shell['bar']['layout'].values()
                  for item in section if item['id'] == 'omarchy.agents']
        self.assertEqual(len(agents), 1)


if __name__ == '__main__':
    unittest.main()
