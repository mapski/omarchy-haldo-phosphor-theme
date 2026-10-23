# HALDO Phosphor

**Warm theme for long workdays.** Phosphor Studio pairs petrol ink surfaces
with warm green, ivory text, Claude Code orange, and restrained magenta.
Three coordinated backgrounds complete the theme.

![Jade Prism — default wallpaper](backgrounds/01-jade-prism.png)

**Jade Prism** is the default. **Ember Coast** and **Phosphor Bloom** are also included.
The 3840×2160 files are AI-generated artwork, upscaled from 1672×941 sources;
they are not native 4K renders. No generation script is required.

![Ember Coast](backgrounds/02-ember-coast.png)
![Phosphor Bloom](backgrounds/03-phosphor-bloom.png)

## Earlier runtime screenshots

The following real captures document the earlier contour-wallpaper/amber version;
they do not show the current backgrounds or orange refinement.

![Phosphor Studio with live btop graphs, themed Neovim source, and labeled palette swatches](preview.png)

Live btop CPU and memory graphs, Neovim, and the Phosphor palette in an isolated
Omarchy session. The centered clock uses AM/PM; the original signal wallpaper
and native shell share the same warm green and ivory palette.

![Native Codex and Claude menu over the Phosphor Studio workspace](docs/images/agents-menu.png)

The native Agents menu keeps Codex and Claude equally accessible. Both images
are real 1920×1080 Wayland captures, not mockups.

## Install

Built and tested with **Omarchy 4.0.6-1 / Quattro**, Hyprland 0.56.2 and
Quickshell 0.3.2. Older releases may not understand the shell section settings.

```bash
omarchy theme install https://github.com/mapski/omarchy-haldo-phosphor-theme.git
```

The installed name is **HALDO Phosphor** (`haldo-phosphor`). Omarchy generates
the terminal, editor, compositor and supported agent colors from `colors.toml`.
The theme adds nine shell section overrides, including visible keyboard focus,
green selections, magenta hover, opaque panels, a 13px shell type scale, and a
30px horizontal bar. It retains your selected monospace font family.

Cycle between the three included backgrounds through Omarchy's background picker.
No third-party plugin is needed. Matrix Rain can be used separately if you
already have it; these wallpapers work on their own.

## Optional agentic workstation profile

The theme styles existing widgets. To add the agreed workstation layout,
preview the separate profile:

```bash
python3 ~/.config/omarchy/themes/haldo-phosphor/scripts/workstation.py
```

Then explicitly apply it:

```bash
python3 ~/.config/omarchy/themes/haldo-phosphor/scripts/workstation.py --apply
```

This sets a compact top bar with **one native Agents widget** and adds an
**Agents → Codex / Claude** menu. The two launch entries have equal prominence.
They appear when the corresponding CLI is installed and launch through
Omarchy's terminal helper. Install/sign in to the agents through your usual
workflow; the profile does not install them, start sessions, or change your
default agent. Each CLI retains its configured permission behavior.

The centered clock uses a 12-hour format, for example **Wed 3:05 PM**. The native
Omarchy update indicator is enabled and appears when updates are available.
Existing third-party/custom widgets retain their bar sections, relative order,
and settings when the profile is applied. Newly installed plugins still need
their usual enablement and placement. [Plugin compatibility](docs/plugins.md).

The native Agents widget displays actual usage/limits and can hide when there
are no usage records. It is not a live task-status monitor. Codex and Claude
reporting are enabled, Fireworks is disabled for this profile, usage refresh
stays at 900 seconds, and cross-device sync is off. Hermes is deferred.

Unrelated settings are preserved. Native bar defaults are rebuilt while
existing third-party/custom widgets are retained. Exact originals are backed up privately; JSONC comments are normalized
when the new menu is written. See [profile details and rollback](docs/workstation.md).

## Development

Python 3.11+ is sufficient for tests and static validation. Wallpapers ship as
finished image files.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
python3 scripts/validate.py --native  # requires installed Omarchy
```

[Design](docs/design.md) · [Validation evidence and limits](docs/validation.md) ·
[Credits](CREDITS.md) · [MIT license](LICENSE)

Community gallery submission: [omacom/omarchy-site#602](https://github.com/omacom/omarchy-site/pull/602)
(maintainer review pending).
