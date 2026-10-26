# Installation, updates and rollback

## Compatibility

Theme version: **1.0.1**. Checked against **Omarchy 4.0.6-1 / Quattro**,
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
links the versioned tag, exact source commit, archive and checksums. Published
tags stay fixed by project policy; v1.0.0 does not have GitHub-enforced release
immutability. To install the
exact tag on a machine where the destination does **not** already exist:

```bash
mkdir -p ~/.config/omarchy/themes
git clone --branch v1.0.0 --depth 1 https://github.com/mapski/omarchy-haldo-phosphor-theme.git ~/.config/omarchy/themes/haldo-phosphor
omarchy theme set haldo-phosphor
```

A tag checkout is detached and stays pinned. Do not delete an existing theme
directory to use this example. Keep custom changes backed up and decide whether
you want a pinned release or a branch that receives updates.

Keep the cloned `.git` directory. Omarchy uses it to recognize an imported
theme and filter executable overrides. The release archive is a source and
integrity record; extracting it into the themes directory does not reproduce
that imported-theme path.

## Updates

Before any update, record your current theme and background and make a backup
outside the themes directory. These examples assume the installed path is a
regular Git clone, not a symlink. Keep the backup until the new version has
passed your application checks.

```bash
theme_dir="$HOME/.config/omarchy/themes/haldo-phosphor"
test -d "$theme_dir/.git" && test ! -L "$theme_dir" && test ! -L "$theme_dir/.git" || exit 1
origin=$(git -C "$theme_dir" remote get-url origin) || exit 1
test "$origin" = "https://github.com/mapski/omarchy-haldo-phosphor-theme.git" || exit 1
backup_root="$HOME/.local/state/haldo-phosphor/backups"
mkdir -p "$backup_root" || exit 1
backup_dir=$(mktemp -d "$backup_root/backup.XXXXXXXX") || exit 1
cp -a "$theme_dir" "$backup_dir/theme" || exit 1
diff -qr --no-dereference "$theme_dir" "$backup_dir/theme" || exit 1
source_commit=$(git -C "$backup_dir/theme" rev-parse --verify HEAD) || exit 1
printf '%s\n' "$source_commit" > "$backup_dir/source-commit.txt" || exit 1
printf 'Backup: %s\n' "$backup_dir"
git -C "$theme_dir" status --porcelain=v1 --untracked-files=all
```

If the last command reports local modifications or untracked files, stop and
decide how to preserve them. Do not discard them or automatically merge them
into a new release. The backup includes the clone's Git state and local files;
verify it can be restored before relying on it.

For a controlled update of this theme only, use a published tag and compare its
resolved commit with the exact SHA on that release. The example uses the
existing v1.0.0; replace both values together when choosing a later release:

```bash
theme_dir="$HOME/.config/omarchy/themes/haldo-phosphor"
target_tag=v1.0.0
expected_commit=bd2c29a2a4197ee54e1a6552879ab72cadd736dd
test -d "$theme_dir/.git" && test ! -L "$theme_dir" && test ! -L "$theme_dir/.git" || exit 1
origin=$(git -C "$theme_dir" remote get-url origin) || exit 1
test "$origin" = "https://github.com/mapski/omarchy-haldo-phosphor-theme.git" || exit 1
local_changes=$(git -C "$theme_dir" status --porcelain=v1 --untracked-files=all) || exit 1
test -z "$local_changes" || exit 1
git -C "$theme_dir" fetch --no-tags origin tag "$target_tag" || exit 1
resolved_commit=$(git -C "$theme_dir" rev-parse --verify "$target_tag^{commit}") || exit 1
test "$resolved_commit" = "$expected_commit" || exit 1
git -C "$theme_dir" switch --detach "$target_tag" || exit 1
omarchy theme set haldo-phosphor
```

A failed fetch or mismatched SHA must stop before checkout or theme application.
If your origin uses an SSH URL, inspect and confirm the equivalent repository
before adapting the URL check. A matching SHA establishes which source was
selected; it does not establish GitHub signature verification. Check commit
and tag signatures separately as described in [validation](validation.md).

Omarchy's general updater updates **all** user-installed Git themes:

```bash
omarchy theme update
omarchy theme set haldo-phosphor
```

It invokes `git pull` for each clone. It is not a release selector or a
single-theme update command. Detached tag checkouts do not follow releases and
can report a pull error; inspect every theme's result. For an intentionally
tracking, clean branch, a single-theme `git pull --ff-only` avoids creating an
automatic merge. Back up first and inspect the resulting commit before applying.

## Backgrounds

Use **Omarchy menu → Style → Background**, or `omarchy theme bg next`.
Re-selecting an already active theme can advance its background on the tested
Omarchy version. Choose Jade Prism explicitly in the picker if needed.

## Rollback

To recover the display quickly, select a known-working theme through
**Style → Theme**. This changes the active appearance; it does not restore an
older HALDO Phosphor checkout.

To restore the backed-up version, first select a known-working theme, then use
the exact backup directory recorded above. Replace `backup.REPLACE_ME` below
with that directory's name. This example validates a separate restored copy
before moving the installed checkout. It uses a unique recovery directory for
each attempt and preserves the displaced checkout there:

```bash
theme_parent="$HOME/.config/omarchy/themes"
theme_dir="$theme_parent/haldo-phosphor"
backup_dir="$HOME/.local/state/haldo-phosphor/backups/backup.REPLACE_ME"
repository="https://github.com/mapski/omarchy-haldo-phosphor-theme.git"
test -d "$theme_parent" && test ! -L "$theme_parent" && test ! -L "$theme_dir" || exit 1
test -d "$backup_dir/theme/.git" && test ! -L "$backup_dir" && test ! -L "$backup_dir/theme" && test ! -L "$backup_dir/theme/.git" || exit 1
test -f "$backup_dir/source-commit.txt" && test ! -L "$backup_dir/source-commit.txt" || exit 1
saved_commit=$(cat "$backup_dir/source-commit.txt") || exit 1
[[ "$saved_commit" =~ ^[0-9a-f]{40}$ ]] || exit 1
backup_commit=$(git -C "$backup_dir/theme" rev-parse --verify HEAD) || exit 1
test "$backup_commit" = "$saved_commit" || exit 1
backup_origin=$(git -C "$backup_dir/theme" remote get-url origin) || exit 1
test "$backup_origin" = "$repository" || exit 1
if test -e "$theme_dir"; then
  test -d "$theme_dir/.git" && test ! -L "$theme_dir/.git" || exit 1
  installed_origin=$(git -C "$theme_dir" remote get-url origin) || exit 1
  test "$installed_origin" = "$repository" || exit 1
fi
recovery_dir=$(mktemp -d "$theme_parent/.haldo-phosphor-recovery.XXXXXXXX") || exit 1
printf 'Recovery files: %s\n' "$recovery_dir"
cp -a "$backup_dir/theme" "$recovery_dir/ready" || exit 1
diff -qr --no-dereference "$backup_dir/theme" "$recovery_dir/ready" || exit 1
git -C "$recovery_dir/ready" fsck --full || exit 1
restored_commit=$(git -C "$recovery_dir/ready" rev-parse --verify HEAD) || exit 1
test "$restored_commit" = "$saved_commit" || exit 1
if test -e "$theme_dir"; then
  mv -T -- "$theme_dir" "$recovery_dir/previous" || exit 1
fi
if ! mv -T -- "$recovery_dir/ready" "$theme_dir"; then
  if test ! -e "$theme_dir" && test ! -L "$theme_dir" && test -d "$recovery_dir/previous"; then
    mv -T -- "$recovery_dir/previous" "$theme_dir" || exit 1
  fi
  exit 1
fi
omarchy theme set haldo-phosphor
```

If validation or copying fails, the installed checkout remains in place. Fix
the reported problem and rerun the block with the same verified backup; each
attempt gets a fresh recovery directory. If a rename or theme application fails,
inspect the printed recovery path and installed directory before retrying. A
non-Git partial installation or symlink is refused and needs manual inspection.
Do not remove recovery directories until their contents are no longer needed.

Select the recorded background explicitly afterward: reapplying a theme can
advance the background. Check your terminal, editor and shell again. Local
modifications and untracked files should match the backup as well as the commit.
Keep both copies until recovery is confirmed.

## Omarchy compatibility upgrades

Theme rollback cannot roll back an Omarchy system upgrade. Before upgrading
Omarchy, use its supported system backup/recovery process and test in a separate
VM or session. Check the old and new theme on both supported and proposed
Omarchy versions, including actual rendering and recovery. A temporary HOME
only isolates files; it does not isolate shared desktop services or IPC sockets.

Current compatibility claims cover the versions listed above. Newer Omarchy
versions require new evidence. Theme installation does not manage widget layout,
keybindings, agent credentials, monitor configuration or idle policy.
