# Validation and release traceability

## Automated source checks

[Validate theme](https://github.com/mapski/omarchy-haldo-phosphor-theme/actions/workflows/validate.yml)
runs on pushes and pull requests, including tag pushes. The workflow checks:

- Semantic version syntax and agreement between a release tag and `VERSION`.
- Palette and nine shell-section TOML files, including semantic color contrast.
- Exactly the three approved wallpapers at 3840×2160.
- SHA-256 preservation of the 18 approved palette, shell, icon and image files.
- Native 2560×1440 screenshot dimensions and absence of text/EXIF metadata.
- README/document links, matching Jade Prism preview and absence of bundled
  Python, shell or Lua script files.

Validation executes inside GitHub Actions; Omarchy does not execute it during
theme installation. No standalone testing scripts are shipped in this theme.

## Native and visual checks

Native imported-theme staging was checked on Omarchy 4.0.6-1 in a temporary
HOME, using the repository's imported-theme path and generated app configs.
The exact v1.0.0 tag was checked before its GitHub Release was published.
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

[Gallery PR #602](https://github.com/omacom/omarchy-site/pull/602) links the
release, theme source commit and validation evidence. Its two canonical
gallery links still point to this theme
repository, as required by the
[submission guide](https://github.com/omacom/omarchy-site#adding-your-theme).

The gallery export is 1200×675 WebP, 68,130 bytes, generated from the current
Jade Prism screenshot. Source validation, a GitHub Release, a conflict-free PR
and maintainer approval are different states. The gallery PR remains under
maintainer review; this theme is not claimed as an approved or built-in release.

## Signatures and release integrity

Local signature verification, GitHub identity recognition and passing CI are
independent checks. Verify both the release commit and its annotated tag. SSH
authentication-key registration does not register the key for signing; GitHub
requires that separate use. See [GitHub's verification guidance](https://docs.github.com/en/authentication/troubleshooting-commit-signature-verification/checking-your-commit-and-tag-signature-verification-status).

The v1.0.0 commit and tag have locally valid SSH signatures. At the October 26,
2026 check, GitHub reported both as `unknown_key` / Unverified. Do not describe
that release as GitHub-verified unless its current status confirms it.

Release manifests identify exact source and file hashes; checksums verify the
downloaded attachments. Neither a checksum nor a signed tag by itself enables
GitHub release immutability. Existing published tags stay fixed by project
policy. Enforced immutability is a separate GitHub setting for future releases.

## Required release checks

Validate clean installation, update from the previous release, pinned-tag and
local-change handling, failed-download recovery and restoration of the previous
checkout. Inspect the real terminal, editor, shell and all backgrounds in an
isolated graphical environment. Record exact Omarchy/application versions and
separate source, native staging, rendered, upgrade and rollback evidence.

After publication, resolve the remote tag and commit again, check their GitHub
verification and CI at the exact source SHA, download every attachment, and
compare it with the manifest and approved source. A blocked or untested required
check is not a pass. New Omarchy versions need their own compatibility checks;
successful staging on one version does not certify a system upgrade.
