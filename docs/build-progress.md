# Build progress

Plan: `docs/superpowers/plans/2026-10-20-phosphor-studio.md`.

Execution is inline, following the user's explicit request to start building
the agreed defaults. Fresh checkout on `codex/phosphor-studio`; initial branch
contained only README and MIT license, with no tests or build system.

Ruling: use a fresh nested checkout because the project root's `.git` is a
protected environment placeholder, not a Git repository. No user checkout is
reset and the daily desktop remains untouched.

Ruling: named menu launch actions use `omarchy-launch-terminal codex` and
`omarchy-launch-terminal claude`; this preserves the user's default agent and
each CLI's configured permissions rather than changing the default just to
launch another agent.

Pre-flight: profile files feed profile merger/tests; palette and shell sections
feed native staging; publication consumes verified source/assets. No competing
writers or overlapping agent tasks.

Task 1: complete — eight profile integration tests pass. Initial expected red
run had six failures before the profile implementation existed. A fresh
reviewer found one host-dependent test; an explicit temporary packaged-default
fixture fixed it, including a passing run with external OMARCHY_PATH missing.

Task 2: complete — palette, nine native shell sections and two original
wallpapers pass static validation and actual imported-theme staging under
temporary HOME. Selection background was darkened to preserve dim syntax
contrast. Generated app outputs and semantic Claude diff colors verified.

Task 3: runtime verified — actual nested Omarchy shell, generated Foot colors,
generated Neovim/Aether palette, two-entry native Agents menu, 1920x1080 clean
desktop capture and 1200x675 gallery WebP. See docs/validation.md for limits.
Publication pending final full checks and remote verification.
