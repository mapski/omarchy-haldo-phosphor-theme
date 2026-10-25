# Plugin compatibility

Plugins that use Omarchy's shared `Commons.Color` and `Style` roles inherit
supported palette and shell styling. The theme does not install, enable,
disable, move or configure plugins.

Read-only inspection found shared theme references in Matrix Rain, ProtonDrive,
Proton Authenticator, Spotify, dual-monitor workspaces and Altscape. That is
source evidence, not a promise that every plugin state has been visually tested.
Fixed brand colors, custom plugin modes, cover art and semantic colors can
remain distinct.

- Keep a custom workspace plugin as the sole workspace widget if it already
  provides the desired monitor/workspace arrangement.
- A plugin's custom color mode can override shared theme colors intentionally.
- Matrix Rain is optional. Plugin enablement and the selected background are
  separate: rain only renders when its own background is selected. A static
  Phosphor wallpaper does not require the plugin.

Keep your existing third-party configuration and inspect panels after changing
themes. Plugin versions and their own settings determine their behavior.
