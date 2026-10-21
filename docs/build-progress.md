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
Task 3: complete — source published to the requested public repository on main.
GitHub CI passed for build commit cf5455f. Gallery contribution submitted as
https://github.com/omacom/omarchy-site/pull/602; maintainer review is pending.

Final compatibility review found that the native shell uses HOME/.config
directly even with a different XDG_CONFIG_HOME. Added a failing regression,
aligned the profile path with the shell, and reran all nine tests successfully.

Temporary test shell/compositor processes have been stopped. Live installation
and real account/agent-task acceptance remain separate optional follow-up work.
