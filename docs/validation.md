# Validation and release traceability

## Automated source checks

[Validate theme](https://github.com/mapski/omarchy-haldo-phosphor-theme/actions/workflows/validate.yml)
runs on pushes and pull requests, including tag pushes. The workflow checks:

- Semantic version syntax and agreement between a release tag and `VERSION`.
- Palette and nine shell-section TOML files, including semantic color contrast.
- Exactly the three approved wallpapers at 3840×2160.
- Native 2560×1440 screenshot dimensions and absence of text/EXIF metadata.
- README/document links, matching Jade Prism preview and absence of bundled
  Python, shell or Lua script files.

Validation executes inside GitHub Actions; Omarchy does not execute it during
theme installation. No standalone testing scripts are shipped in this theme.

## Native and visual checks

Native imported-theme staging was checked on Omarchy 4.0.6-1 in a temporary
HOME, using the repository's imported-theme path and generated app configs.
The exact v1.0.0 tag is checked again before its GitHub Release is published.
This does not change the author's daily desktop configuration.

The screenshots are real Wayland captures with Foot, Neovim using Omarchy's
generated Aether palette, live btop and terminal palette swatches. The CPU model
label is customized for the showcase; the graphs remain actual system metrics.
Screenshots demonstrate the appearance, not a widget layout installed by the
theme. Wallpaper exports are upscaled artwork, as disclosed in the README.

## Release versus gallery approval

[GitHub Release v1.0.0](https://github.com/mapski/omarchy-haldo-phosphor-theme/releases/tag/v1.0.0)
identifies the theme tag and source commit. Its archive and checksum attachment
provide a reproducible record of the distributed files.

[Gallery PR #602](https://github.com/omacom/omarchy-site/pull/602) records the
release tag, full theme commit, gallery-branch commit, preview checksum and
validation evidence. Its two canonical gallery links still point to this theme
repository, as required by the
[submission guide](https://github.com/omacom/omarchy-site#adding-your-theme).

The gallery export is 1200×675 WebP, 68,130 bytes, generated from the current
Jade Prism screenshot. Source validation, a GitHub Release, a conflict-free PR
and maintainer approval are different states. The gallery PR remains under
maintainer review; this theme is not claimed as an approved or built-in release.
