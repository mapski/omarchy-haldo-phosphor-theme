# Installation, updates and rollback

## Compatibility

Theme version: **1.0.0**. Checked against **Omarchy 4.0.6-1 / Quattro**,
Hyprland 0.56.2 and Quickshell 0.3.2. The theme version and Omarchy package
version are separate. Older Omarchy releases may not support the shell sections.

Omarchy generates terminal, editor and compositor configuration from
`colors.toml`. This repository supplies no executable theme overrides or
installation scripts. No additional plugin is required.

## Normal installation

Record your current theme and wallpaper first if you want an easy rollback.
The normal command installs the repository's current default branch:

Use this for a first installation only. The tested Omarchy installer removes
an existing `~/.config/omarchy/themes/haldo-phosphor` before cloning, so a repeat
installation can discard local edits or a pinned checkout even if the clone
fails. If that directory already exists, back it up and use the updates section
instead; do not use installation as an update command.

```bash
omarchy theme install https://github.com/mapski/omarchy-haldo-phosphor-theme.git
```

The installed slug is `haldo-phosphor`. The installer applies the theme.

## Exact version

The [v1.0.0 release](https://github.com/mapski/omarchy-haldo-phosphor-theme/releases/tag/v1.0.0)
links the immutable tag, source commit, archive and checksums. To install the
exact tag on a machine where the destination does **not** already exist:

```bash
mkdir -p ~/.config/omarchy/themes
git clone --branch v1.0.0 --depth 1 https://github.com/mapski/omarchy-haldo-phosphor-theme.git ~/.config/omarchy/themes/haldo-phosphor
omarchy theme set haldo-phosphor
```

A tag checkout is detached and stays pinned. Do not delete an existing theme
directory to use this example. Keep custom changes backed up and decide whether
you want a pinned release or a branch that receives updates.

## Updates

Omarchy's supported updater updates **all** user-installed Git themes:

```bash
omarchy theme update
omarchy theme set haldo-phosphor
```

This applies to branch checkouts. A pinned tag does not follow later releases.
Review and back up personal modifications before updating.

## Backgrounds

Use **Omarchy menu → Style → Background**, or `omarchy theme bg next`.
Re-selecting an already active theme can advance its background on the tested
Omarchy version. Choose Jade Prism explicitly in the picker if needed.

## Rollback

Select your previous theme through **Style → Theme**, then select its previous
background through **Style → Background**. Switching themes does not remove
HALDO Phosphor. The theme does not replace widget layout, keybindings, agent
credentials, monitor configuration or idle policy.
