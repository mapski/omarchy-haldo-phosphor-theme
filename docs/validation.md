# Validation record

Build reviewed October 21, 2026, against installed Omarchy **4.0.6-1**,
Hyprland **0.56.2-4**, Quickshell **0.3.2.r7.g2b4501a-1**.

## Verified

- Eleven Python integration tests cover preview/no writes, JSONC parsing and
  unrelated-setting preservation, exactly one Agents widget and two named
  launch entries, idempotence, private exact backups, invalid input, symlink
  refusal, missing input files, and the HOME config path used by native Omarchy.
  The additional cases check the centered AM/PM clock, update indicator
  enablement, unrelated disabled plugins, and third-party widget preservation
  including idempotent reapplication.
  Packaged defaults are fixtures, so CI does
  not require Omarchy to be installed.
- All palette text/semantic roles checked by `scripts/validate.py` meet 4.5:1
  on the base, raised and selection backgrounds. These are opaque-color
  calculations, not a claim about every blend or font at every display scale.
- Native `omarchy-theme-set`, with headless mode and a temporary HOME, exercised
  the installed-from-Git staging branch and native template generation. The
  staged theme includes terminal/editor/agent outputs and the shipped assets.
  No unresolved placeholders were found. Font/bar sizing, focus width, menu
  selection, error state and distinct Claude diff colors were checked.
- The optional workstation profile was applied only inside temporary HOME.
- An isolated nested Wayland compositor ran the actual packaged Omarchy shell.
  Foot used its generated colors; Neovim used the generated Aether v3 palette.
  The actual menu displayed both Codex and Claude. No agent sessions were started.
- `preview.png` is an unmodified 1920x1080 real desktop capture with the
  included wallpaper, a terminal and editor, no pointer, and no notifications.
  `docs/images/agents-menu.png` captures the native menu. Neither is a browser
  mockup. The gallery WebP is 1200x675, stripped, and 34,558 bytes.
- A fresh read-only reviewer found a test portability issue; the missing-config
  test now uses an explicit packaged-default fixture. The complete test
  suite also passes with the external `OMARCHY_PATH` pointing at a nonexistent
  directory. No further verified production issue was reported by that review.

## Runtime conditions and limits

The AM/PM format was checked with native Qt formatting at midnight, noon and
15:05, including a negative probe that exited nonzero on a wrong expectation.
Existing desktop screenshots show the initial 24-hour-clock build; the new
profile settings were verified independently, not recaptured in those images.

The test compositor used a separate HOME, runtime directory and private D-Bus
session. Idle, polkit, notifications and night light were disabled only in that
temporary shell to avoid unrelated desktop services during capture. The test
used a 1920x1080 nested output, not a daily-desktop theme switch. Temporary
processes are stopped after verification.

The isolated shell reported host-portal/PipeWire connection warnings.
Creating an extra virtual output also produced duplicate panel IPC warnings;
the unused output was removed for final capture. Those warnings do not justify
claiming a warning-free full shell session.

Authentication/lock execution, multi-monitor acceptance, live subscription
usage endpoints, actual Codex/Claude tasks, and every supported editor/app were
not exercised. Their generated configuration was checked where described above.
With no authenticated usage records in the clean test HOME, the native Agents
widget can self-hide; no usage records were fabricated for the screenshots.

## Reproduce

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
python3 scripts/validate.py --native
```

`--native --keep` leaves its isolated HOME for further inspection and prints
its path. The native check never selects the theme on the user's daily desktop.
The optional profile is always explicit; theme installation does not run it.

Gallery asset preparation follows the site's README:

```bash
magick preview.png -strip -resize '1200>' -quality 80 docs/images/haldo-phosphor.webp
```
