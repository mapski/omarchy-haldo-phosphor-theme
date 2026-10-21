#!/usr/bin/env python3
"""Generate original signal-contour SVGs and rasterize with ImageMagick."""
from math import cos, sin, pi
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def artwork(quiet=False):
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160">',
             '<defs><radialGradient id="ink"><stop stop-color="#1B2826"/><stop offset="1" stop-color="#0C1211"/></radialGradient></defs>',
             '<rect width="3840" height="2160" fill="#101717"/>',
             '<ellipse cx="2950" cy="1280" rx="2300" ry="1800" fill="url(#ink)" opacity=".65"/>']
    for ring in range(30):
        radius = 180 + ring * 40
        points = []
        for step in range(481):
            t = step * 2 * pi / 480
            ripple = 1 + .055*sin(3*t + ring*.085) + .035*cos(5*t-ring*.06)
            x = 2860 + radius*ripple*cos(t) + 90*sin(t*2)
            y = 1280 + radius*.77*ripple*sin(t)
            points.append(f'{x:.1f},{y:.1f}')
        color = '#9BCC9C'
        opacity = .075 if quiet else .17
        if not quiet and ring in (10, 25):
            color, opacity = ('#D9AE6A', .32) if ring == 10 else ('#C88BAB', .22)
        parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{color}" stroke-opacity="{opacity}" stroke-width="2"/>')
    # Small registration marks are part of the original artwork, not desktop UI.
    parts.extend(['<g stroke="#9BCC9C" stroke-opacity=".25" stroke-width="2">',
                  '<path d="M144 1840h64m-32-32v64M144 1920h280"/>', '</g>', '</svg>'])
    return '\n'.join(parts) + '\n'


def main():
    (ROOT / 'art').mkdir(exist_ok=True)
    (ROOT / 'backgrounds').mkdir(exist_ok=True)
    for name, quiet in [('01-phosphor-signal', False), ('02-phosphor-quiet', True)]:
        svg = ROOT / 'art' / f'{name}.svg'
        svg.write_text(artwork(quiet))
        subprocess.run(['magick', '-background', '#101717', str(svg), '-strip',
                        '-define', 'png:color-type=2', str(ROOT / 'backgrounds' / f'{name}.png')], check=True)


if __name__ == '__main__':
    main()
