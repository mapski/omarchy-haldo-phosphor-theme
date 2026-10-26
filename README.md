# HALDO Phosphor

**Warm theme for long workdays.** Phosphor Studio brings ivory text, phosphor
green and Claude Code orange to deep petrol-ink surfaces.

**Theme release: [v1.0.1](https://github.com/mapski/omarchy-haldo-phosphor-theme/releases/tag/v1.0.1)** ·
[Changelog](CHANGELOG.md) ·
[Validation](https://github.com/mapski/omarchy-haldo-phosphor-theme/actions/workflows/validate.yml)

Community gallery submission: [omacom/omarchy-site#602](https://github.com/omacom/omarchy-site/pull/602)
— under maintainer review. Publishing this GitHub release does not imply gallery
approval or inclusion as an Omarchy built-in theme.

![HALDO Phosphor with Jade Prism, themed Neovim, live btop and palette swatches](preview.png)

## Install

For a first installation:

```bash
omarchy theme install https://github.com/mapski/omarchy-haldo-phosphor-theme.git
```

If already installed, use the [update guidance](docs/installation.md#updates).
The installer replaces its destination directory; back up local changes first.

Select **HALDO Phosphor** from **Omarchy menu → Style → Theme**, or run:

```bash
omarchy theme set haldo-phosphor
```

Designed and checked with **Omarchy 4.0.6-1 / Quattro**. Omarchy generates
supported terminal, editor and application colors from `colors.toml`. Nine
shell sections coordinate the bar, menus, launcher, notifications, tooltips,
controls and lock screen. The shell uses 13px text and a 30px horizontal bar
while retaining your font family.

This is a theme-only package. It contains no installer, Python/shell helper
scripts or automatic workstation profile. Your widget arrangement, agent
accounts, terminal choice, shortcuts and idle policy remain yours.

See [installation, exact-version checkout, updates and rollback](docs/installation.md),
[optional workstation choices](docs/workstation.md), and
[third-party plugin compatibility](docs/plugins.md). The optional workstation
work remains documented separately; theme installation does not apply it.

## Backgrounds

**Jade Prism** is the initial background. **Ember Coast** and **Phosphor Bloom**
are included as alternatives. Open **Omarchy menu → Style → Background** to
choose one, or cycle with:

```bash
omarchy theme bg next
```

All three wallpapers ship as 3840×2160 PNGs. The artwork was AI-generated at
1672×941 and upscaled for 4K output; these are not native-detail 4K renders.

### Ember Coast

![Ember Coast with the same themed terminal and editor layout](screenshots/02-ember-coast.png)

### Phosphor Bloom

![Phosphor Bloom with the same themed terminal and editor layout](screenshots/03-phosphor-bloom.png)

## Palette

| Role | Color |
| --- | --- |
| Ink | `#101717` |
| Raised surface | `#1B2826` |
| Ivory | `#E5E3D5` |
| Phosphor green | `#9BCC9C` |
| Claude Code orange | `#D97757` |
| Magenta | `#C88BAB` |
| Error | `#E38D83` |

Screenshots are real, metadata-free 2560×1440 Wayland captures of the theme,
Foot, Neovim and btop. The sample bar arrangement demonstrates the appearance;
installing the theme does not replace your bar layout. Live system graphs are
shown without process lists, accounts or network information.

[Validation and release traceability](docs/validation.md) ·
[Credits](CREDITS.md) · [MIT license](LICENSE)
