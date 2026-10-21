# Third-party plugins and Phosphor

Plugins that use Omarchy's shared `Commons.Color` and `Style` roles adopt the
active palette and supported shell settings. They keep their own functionality
and plugin configuration. Custom theme modes, fixed brand colors, album art,
and hard-coded state colors can remain distinct.

Read-only inspection of the installed plugin sources on October 21, 2026 found
shared theme references in Matrix Rain, ProtonDrive, Proton Authenticator,
Spotify, dual-monitor workspaces, and Altscape. This is static compatibility
evidence, not a completed visual acceptance test of every panel and state.

- Matrix Rain takes its theme accent/background from Omarchy, so Phosphor
  supplies warm green and ink when that plugin is enabled.
- ProtonDrive and the workspace widget reference shared shell roles.
- Proton Authenticator and Spotify use shared roles; individual artwork and
  some semantic/custom state colors can remain independent.
- Altscape receives bar text/background/accent from Omarchy. Its custom color
  mode, if selected in the plugin's own settings, intentionally overrides those.

The workstation profile preserves already-placed third-party/custom widgets in
their existing bar section and relative order, including widget settings.
Existing plugin enablement settings are preserved. It does not automatically
install or enable new plugins, and service/overlay plugins do not become bar
widgets merely because their code is installed.

Before applying the profile to a daily workstation, review the resulting bar
density and check each plugin's visible panel. Multiple workspace plugins or a
long media title may need a later layout choice. Existing exact config files
are backed up by the explicit apply step.
