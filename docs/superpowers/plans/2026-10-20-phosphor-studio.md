# Phosphor Studio Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Build and publish HALDO Phosphor with the approved Codex/Claude workstation defaults.

**Architecture:** Declarative Omarchy palette and shell sections plus original
wallpapers. A separate optional profile merges bar/menu settings with private
backups; it never runs as part of theme installation.

**Tech Stack:** TOML, JSON, Python standard library, ImageMagick, native Omarchy/Quickshell.

**Spec:** `docs/design.md`

## Global Constraints

- One native Agents widget; Codex and Claude equally; Hermes deferred.
- Opaque ink, warm green, ivory, amber; semantic errors remain distinct.
- No changes to packaged Omarchy, live user configuration, agent credentials or default agent.
- Public installer must preserve the actual design without Lua/terminal override files.
- Repository MIT license stays intact.

## Review Focus

- Existing JSONC strings/comments and unrelated settings survive semantic merge.
- Invalid inputs and symlinks fail before either configuration file is changed.
- Reapplying a profile never adds duplicate widgets or menu entries.
- Theme rendering must use actual installed staging/templates, not only a custom parser.
- Native usage absence must not become invented usage or completion indicators.

### Task 1: Reversible workstation profile

**Files:** `profiles/workstation.json`, `profiles/menu.json`, `scripts/workstation.py`, `tests/test_workstation.py`.

**Interfaces:** `build_profile(shell: dict, menu: dict) -> tuple[dict, dict]` and
`read_jsonc(text: str) -> dict`; CLI previews by default, `--apply` writes.

- [ ] Write failing tests for JSONC strings/trailing commas, merge preservation, exactly one Agents widget/two launch entries, idempotence, invalid input, private backups and symlinks.
- [ ] Run `python3 -m unittest discover -s tests -v` and confirm expected failures before implementation.
- [ ] Implement profile files and merger, with native named CLI launches and unchanged default-agent setting.
- [ ] Run the complete test suite; inspect backup and preview behavior under temporary HOME.

### Task 2: Installable palette and original art

**Files:** `colors.toml`, `shell.*.toml`, `icons.theme`, `art/`, `backgrounds/`, `scripts/build-wallpapers.py`, `scripts/validate.py`.

**Interfaces:** Omarchy native TOML palette and section replacement contract; 3840x2160 PNG wallpapers.

- [ ] Build palette and section configuration from the approved design; use current generated defaults for unmodified surfaces.
- [ ] Generate original signal contours and quiet wallpaper with reproducible source.
- [ ] Validate palette roles/contrast, JSON/TOML, images, symlinks and imported-theme-safe files.
- [ ] Run native theme staging and template generation with temporary HOME; inspect rendered terminal/agent/editor configurations and merged shell states.

### Task 3: Runtime, documentation and publication

**Files:** `README.md`, `docs/workstation.md`, `docs/validation.md`, `CREDITS.md`, `.github/workflows/validate.yml`, previews.

**Interfaces:** Documented installation command, explicit optional profile command, backup rollback instructions.

- [ ] Render actual shell components and attempt an isolated real Wayland desktop; record exact verification limits.
- [ ] Review source, license, screenshots, repository contents, and run full tests/validation.
- [ ] Commit and push the tested build to the provided public repository; verify the remote commit and public contents.
- [ ] Submit a gallery PR only when the required real screenshot exists; otherwise document that remaining gate without claiming gallery acceptance.
