# Changelog

## 1.0.2 — 2026-11-05

- Re-encode the three existing 3840×2160 backgrounds as metadata-free, quality-82
  WebP files, reducing their combined size from 19,750,574 to 874,746 bytes.
- Remove the GitHub Actions workflow and its embedded validation program from
  the theme repository. Validation tools are maintained outside the package.
- Update background, validation and migration documentation. Select your
  preferred background again after an update or rollback across this format change.

The palette, nine shell sections, icons and screenshots are unchanged. The
wallpapers retain the same artwork and ordering, with lossy compression.

## 1.0.1 — 2026-10-26

- Add controlled single-theme updates, backup restoration and failed-update
  recovery guidance, including pinned releases and local modifications.
- Enforce the approved palette, shell, icon and image hashes during source
  validation without changing the appearance.
- Clarify signature verification, release immutability and the separate
  evidence required for Omarchy compatibility upgrades.

The palette, shell styling and all artwork remain identical to v1.0.0.
No runtime helper or workstation installer is added.

## 1.0.0 — 2026-10-24

First versioned GitHub release of HALDO Phosphor / Phosphor Studio.

- Ivory text, phosphor green, Claude Code orange and petrol-ink surfaces.
- Nine coordinated Omarchy shell sections and palette-generated app themes.
- Jade Prism as the initial wallpaper, with Ember Coast and Phosphor Bloom.
- Current 2560×1440 real desktop screenshots and a 1200×675 gallery preview.
- Explicit release identity, installation/update guidance, workstation notes,
  plugin compatibility notes and automated source validation.

This release retains the palette and artwork from unversioned commit
`6105ca3f16665e3aa4d688b48d0c8d123a3b8375`. The repair restores documentation,
validation and versioning; it does not redesign the theme or apply a workstation
layout. Earlier unversioned commits remain in Git history.

Wallpaper files are 3840×2160 exports upscaled from 1672×941 generated artwork.
Screenshots are native 2560×1440 captures. These are different assets.

Community gallery submission: [omacom/omarchy-site#602](https://github.com/omacom/omarchy-site/pull/602).
Gallery review and merge are controlled by the Omarchy maintainers and are
separate from this GitHub release.
