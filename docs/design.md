# HALDO Phosphor / Phosphor Studio

Approved direction: warm phosphor green, ivory text, petrol ink surfaces,
Claude Code orange, restrained magenta and three coordinated backgrounds.
The user approved starting the build with one native Agents widget and Codex
and Claude menu entries. Hermes is deferred.

## Version one

- Installable repository: `mapski/omarchy-haldo-phosphor-theme`, slug `haldo-phosphor`.
- Palette source `colors.toml`, semantic normal/bright ANSI colors, meaningful
  error/warning/diff colors. No executable theme overrides.
- Use generated terminal, editor and agent themes; override individual shell
  sections for readable menus, launcher, popups, notification, lock and controls.
- 13px shell base, 30px horizontal bar at that size, existing monospace family.
- Opaque ink surfaces, 2px keyboard focus, green selection, small magenta hover.
- Three static 3840x2160 wallpapers: Jade Prism (default), Ember Coast and
  Phosphor Bloom. AI-generated 1672x941 sources, exported as upscaled 4K PNGs.
- Optional workstation profile: top bar; menu/workspaces left; clock centered;
  one native Agents widget plus indicators/updates/tray/network/audio/power right.
- Centered clock uses `ddd h:mm AP` (for example Wed 3:05 PM). Explicitly enable
  clock and native update indicator while preserving unrelated disabled plugins.
- Preserve existing third-party/custom widget sections, relative order and settings.
- Codex and Claude enabled equally in the Agents provider settings, native
  900-second refresh, account sync off. No fabricated usage or task state.
- Menu offers named Codex and Claude launch actions. Preserve the existing
  default agent and installed credentials. Agent installation is separate.
- Profile application is explicit, merges unrelated settings, validates both
  files before writing, and makes private backups. Preview is the default.
- Theme installation does not apply the workstation profile automatically.

## Acceptance

Check theme palette contrast, actual Omarchy generation/staging in a temporary
HOME, JSON/TOML syntax, one Agents widget, two menu launch entries, JSONC merge,
backup/rollback, existing-file preservation, and profile idempotence.

Render actual themed shell surfaces and a real isolated Wayland desktop if
available. Public screenshots must identify their actual origin; concept
mockups are never desktop evidence. Gallery submission requires a real 16:9
desktop with terminal/editor, own wallpaper, metadata stripped, approximately
1200x675 and under 100KB.

Publish the tested source to the user's supplied public repository. Keep live
desktop installation, account login, agent invocation, and optional profile
application separate from building and publishing.

## Source contracts

- [Theme authoring](https://github.com/omacom/omarchy/blob/quattro/manual/43-making-your-own-theme.md)
- [Theme generation](https://github.com/omacom/omarchy/blob/quattro/docs/theming.md)
- [Gallery submission](https://github.com/omacom/omarchy-site#adding-your-theme)
- [Omarchy doctrine](https://github.com/omacom/omarchy-site/blob/master/content/doctrine.md)

Development baseline: installed Omarchy 4.0.6-1. Upstream Quattro can advance
independently; compatibility claims must name their tested version.
