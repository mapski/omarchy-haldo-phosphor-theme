# Validation and release traceability

## Source validation

The theme repository contains appearance data, images and documentation. It
ships no executable validators, GitHub Actions workflows, installers, hooks or
plugins. Checks are maintained and run outside this repository.

Release preparation checks the complete file inventory, including hidden paths,
against the reviewed package. It verifies palette contrast and TOML syntax,
the nine shell sections, protected palette/icon/shell/screenshot hashes, three
decodable 3840×2160 WebP backgrounds, stripped image metadata, background size
and documentation links. Background hashes change intentionally in v1.0.2
because the existing artwork is re-encoded with lossy compression.

Validation of v1.0.0 and v1.0.1 used an embedded GitHub Actions program. Those
historical runs do not validate v1.0.2. Their workflow was removed from the
current theme tree; a passing historical CI run is not current certification.

## Native and visual checks

The v1.0.2 candidate passed 14 native lifecycle checks and seven graphical
checks on Omarchy 4.5.0-3, Hyprland 0.56.2-4 and Quickshell
0.3.2.r7.g2b4501a-1. Native checks used the real installer and updater with an
offline Git fixture, a separate filesystem and network namespace, and no host
desktop sockets. They covered fresh installation, migration from each of the
three selected PNG backgrounds, WebP cycling, backup restoration, failed fetch,
incorrect source SHA, local edits and pinned-release handling.

Graphical checks used one nested Wayland display at scale 1 (1181×1296), Foot,
the packaged Omarchy Neovim/Aether profile, menu and clock panels, and all three
WebP backgrounds. Rollback restored the previous PNG background and the editor's
Aether palette without a restart. Packaged editor plugins were mounted read-only;
online parser downloads and desktop account services were not tested. The source
validator also rejected nine deliberately invalid package cases.

The v1.0.1 release was checked on Omarchy 4.0.6-1 with isolated installation,
update, failure recovery and rollback tests. A nested Wayland session covered
Foot, the packaged Omarchy Neovim profile, shell panels and the three original
backgrounds. That evidence applies to v1.0.1 and its recorded environment.

The retained screenshots are real Wayland captures with Foot, Neovim using
Omarchy's generated Aether palette, live btop and terminal palette swatches.
They show the same artwork before WebP re-encoding. The CPU model label is
customized for the showcase; the graphs are actual system metrics. Screenshots
demonstrate appearance, not a widget layout installed by the theme.

Current-version test results and their exact source identity belong in the
release notes. Do not infer a newer Omarchy compatibility result from the older
screenshots or historical tests. Physical login/lock, multiple monitors, account
integrations and an Omarchy system upgrade require separate validation.

## Release versus gallery approval

Versioned releases identify the source commit, archive and checksums. A release
manifest covers the exact distributed files. Existing published tags remain
fixed; subsequent corrections use a new version.

[Gallery PR #602](https://github.com/omacom/omarchy-site/pull/602) is a separate
submission. Its two gallery links point to the theme repository, as required by
the [submission guide](https://github.com/omacom/omarchy-site#adding-your-theme).
The retained gallery preview is a metadata-free 1200×675 WebP, 68,130 bytes.
Source validation, a published release and maintainer acceptance are separate
states. This theme is not claimed as approved or built into Omarchy.

## Signatures and release integrity

Local signature verification and GitHub identity recognition are separate
checks. Verify the exact release commit and annotated tag using
[GitHub's verification guidance](https://docs.github.com/en/authentication/troubleshooting-commit-signature-verification/checking-your-commit-and-tag-signature-verification-status).
Registering an SSH authentication key does not register it for signing.

Manifest and checksum comparisons establish which bytes were downloaded.
Neither a checksum nor a signed tag enables GitHub release immutability; that
is a separate repository setting. Verify current state instead of relying on
an old verification observation.

## Required release checks

Validate clean installation, update from the previous release, pinned-tag and
local-change handling, failed-download recovery and restoration of the previous
checkout. Inspect the terminal, editor, shell and all backgrounds in an isolated
graphical environment. For v1.0.2, exercise a selected PNG background through the
WebP update and back through rollback. Record exact application versions and
distinguish source checks, native staging and rendered checks.

After publication, resolve the remote tag and commit, check their signatures,
download every attachment and compare it with the manifest and tested source.
The theme no longer has in-repository CI; validation results must identify the
exact externally tested source. A blocked or untested required check is not a
pass. A temporary HOME alone does not isolate desktop services or IPC sockets.
