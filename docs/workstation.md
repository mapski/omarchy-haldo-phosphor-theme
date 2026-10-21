# Optional workstation profile

Python 3.11+ and the native Omarchy shell are required. Preview by running
`python3 scripts/workstation.py` from this checkout. No arguments means no
configuration writes. Add `--apply` to apply the profile explicitly.

The profile uses `~/.config/omarchy`, matching the native shell/menu even when
`XDG_CONFIG_HOME` is set to a different location.

## What changes

- `~/.config/omarchy/shell.json`: top opaque bar; menu/workspaces left; 12-hour
  AM/PM clock centered; one Agents widget, indicators, Omarchy updates, tray,
  network, audio and power right. The clock format is `ddd h:mm AP`.
- `~/.config/omarchy/extensions/omarchy-menu.jsonc`: an Agents submenu with
  Codex and Claude entries. Entries are hidden when their CLI is missing.
- Agent widget settings: Codex and Claude enabled, other existing provider
  entries disabled, refresh 900 seconds, sync off.

The profile rebuilds native bar defaults while retaining existing third-party
and custom widget entries in their current sections and relative order, with
their per-widget settings intact. Native widget settings are merged, with the
profile's explicit settings winning. Unrelated
top-level shell/menu fields are preserved. Existing idle, lock, plugins,
credentials, default agent, monitors, and keybindings remain as configured.
Theme appearance is separate and comes from Omarchy theme installation.

The clock and update indicator are removed from `disabledPlugins` if listed;
unrelated disabled plugins remain disabled. The native update indicator checks
when loaded and every six hours, hides when no update is available, and opens
Omarchy's updater when clicked. No updates are run by applying the profile.

Preserving a widget means preserving its section and order among existing
third-party entries; added native defaults can change the exact pixel position.
The profile does not discover, install, or enable third-party plugins on its own.

Both inputs are parsed and the output is built before either file is written.
JSONC comments and trailing commas are accepted, including strings containing
URLs or comment-like text. The resulting files use JSON formatting; comments
remain in the byte-for-byte backup. Symlinked configuration paths are refused
so that users with linked dotfiles can merge the two profile fragments manually.

The launcher uses `omarchy-launch-terminal codex` or
`omarchy-launch-terminal claude`. Omarchy's helper determines terminal cwd from
the active terminal. When there is no active terminal, inspect the working
directory before beginning project work. These named launchers do not mutate
the global default agent or add automatic approval flags.

The installed 4.0.6-1 shell hot-reloads the config and menu. Upstream's Agents
panel is evolving; the packaged version is the compatibility baseline here.

## Backups and rollback

Application prints a private directory under:

```text
~/.config/omarchy/phosphor-backups/<UTC timestamp>/
```

Each saved config is mode 0600 inside a mode-0700 timestamp directory. The
backup contains `shell.json` and `omarchy-menu.jsonc`, or a corresponding
`.missing` marker if that input did not exist. Reapplying creates another
backup without duplicating widgets or menu entries.

To restore, use the timestamp printed by the apply command. For example:

```bash
backup="$HOME/.config/omarchy/phosphor-backups/<timestamp>"
cp "$backup/shell.json" "$HOME/.config/omarchy/shell.json"
cp "$backup/omarchy-menu.jsonc" "$HOME/.config/omarchy/extensions/omarchy-menu.jsonc"
```

Only use a `cp` command when that saved file exists. If a `.missing` marker is
present instead, remove the corresponding newly created configuration file
after reviewing it; this restores the original absence. Restoring a pre-profile
backup also replaces any later edits to that file, so save those edits first.

For a manual merge, use `profiles/workstation.json` as the bar subtree and add
the keys from `profiles/menu.json` to the menu extension. Do not overwrite the
entire shell configuration with the bar fragment.
