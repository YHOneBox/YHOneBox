"""Generate the animated HUD banner for the GitHub profile README."""

from pathlib import Path

W, H = 1200, 280
CYAN = "#5ce1ff"
PURPLE = "#b794f6"
TEAL = "#2ee6a6"
AMBER = "#f0d48a"
INK = "#e8f4ff"
MUTED = "#9bb3c9"

layers = [
    [(740, y) for y in (72, 124, 176, 228)],
    [(860, y) for y in (52, 88, 124, 160, 196, 232)],
    [(980, y) for y in (52, 88, 124, 160, 196, 232)],
    [(1100, y) for y in (92, 140, 188)],
]

# A few packets travel along selected edges so the net feels alive.
packets = [
    (0, 0, 1, 1, "3.2s", CYAN),
    (0, 1, 1, 2, "2.6s", TEAL),
    (0, 2, 1, 3, "3.8s", PURPLE),
    (0, 3, 1, 4, "2.9s", CYAN),
    (1, 0, 2, 1, "3.4s", PURPLE),
    (1, 2, 2, 2, "2.4s", CYAN),
    (1, 3, 2, 3, "3.1s", TEAL),
    (1, 5, 2, 4, "2.7s", PURPLE),
    (2, 1, 3, 0, "2.8s", CYAN),
    (2, 2, 3, 1, "3.6s", TEAL),
    (2, 4, 3, 2, "3.0s", PURPLE),
]


def line(a, b, opacity=0.18, color=CYAN, width=1):
    return (
        f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" '
        f'stroke="{color}" stroke-width="{width}" opacity="{opacity}"/>'
    )


parts: list[str] = []

parts.append(
    f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Yi-Ho Chang, AI Engineer">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#050914"/>
      <stop offset="45%" stop-color="#071226"/>
      <stop offset="100%" stop-color="#100816"/>
    </linearGradient>
    <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{CYAN}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{CYAN}" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="{CYAN}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{INK}"/>
      <stop offset="70%" stop-color="{CYAN}"/>
      <stop offset="100%" stop-color="{PURPLE}"/>
    </linearGradient>
    <radialGradient id="orb" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{CYAN}" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="{CYAN}" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="2.4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <circle cx="980" cy="140" r="120" fill="url(#orb)">
    <animate attributeName="r" values="110;140;110" dur="8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.7;1;0.7" dur="8s" repeatCount="indefinite"/>
  </circle>
'''
)

# Perspective grid
for x in range(24, W, 36):
    parts.append(
        f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{CYAN}" stroke-width="0.6" opacity="0.06"/>'
    )
for y in range(16, H, 28):
    parts.append(
        f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{CYAN}" stroke-width="0.6" opacity="0.06"/>'
    )

# Sweeping scan
parts.append(
    f'''  <rect x="0" width="{W}" height="36" fill="url(#scan)" opacity="0.55">
    <animate attributeName="y" values="-36;{H};-36" dur="7s" repeatCount="indefinite"/>
  </rect>
'''
)

# HUD corners
def corner(x, y, dx, dy):
    return (
        f'<path d="M{x + dx * 22},{y} H{x} V{y + dy * 22}" fill="none" '
        f'stroke="{CYAN}" stroke-width="1.6" opacity="0.85"/>'
    )


parts.append(corner(18, 16, 1, 1))
parts.append(corner(W - 18, 16, -1, 1))
parts.append(corner(18, H - 16, 1, -1))
parts.append(corner(W - 18, H - 16, -1, -1))

# Status + copy
parts.append(
    f'''  <g font-family="IBM Plex Mono, ui-monospace, Consolas, monospace">
    <circle cx="46" cy="42" r="4.5" fill="{TEAL}">
      <animate attributeName="opacity" values="1;0.25;1" dur="1.6s" repeatCount="indefinite"/>
    </circle>
    <text x="60" y="46" fill="{TEAL}" font-size="13">ONLINE · STILL COMPILING</text>
    <text x="46" y="116" fill="url(#title)" font-size="42" font-weight="600">YI-HO CHANG</text>
    <text x="46" y="148" fill="{MUTED}" font-size="16">AI ENGINEER</text>
    <text x="46" y="186" fill="{CYAN}" font-size="13">ML · LLM / RAG · VISION · EDGE</text>
    <text x="46" y="226" fill="{MUTED}" font-size="12">Oregon · models that leave the notebook</text>
    <text x="740" y="36" fill="{MUTED}" font-size="11">INFERENCE GRAPH</text>
  </g>
'''
)

# Neural net edges
for i, src_layer in enumerate(layers[:-1]):
    dst_layer = layers[i + 1]
    color = (CYAN, PURPLE, TEAL)[i]
    for a in src_layer:
        for b in dst_layer:
            parts.append("  " + line(a, b, opacity=0.14, color=color))

# Highlighted packet paths
for si, sj, di, dj, dur, color in packets:
    a, b = layers[si][sj], layers[di][dj]
    parts.append("  " + line(a, b, opacity=0.55, color=color, width=1.4))
    parts.append(
        f'''  <circle r="3.2" fill="{color}" filter="url(#glow)">
    <animateMotion dur="{dur}" repeatCount="indefinite" path="M{a[0]},{a[1]} L{b[0]},{b[1]}"/>
  </circle>
'''
    )

# Nodes
for li, layer in enumerate(layers):
    color = (CYAN, PURPLE, TEAL, AMBER)[li]
    r = 5.2 if li in (0, 3) else 4.4
    for idx, (x, y) in enumerate(layer):
        delay = 0.18 * (li + idx)
        parts.append(
            f'''  <circle cx="{x}" cy="{y}" r="{r}" fill="#071226" stroke="{color}" stroke-width="1.6" filter="url(#glow)">
    <animate attributeName="r" values="{r};{r + 1.6};{r}" dur="2.8s" begin="{delay:.2f}s" repeatCount="indefinite"/>
  </circle>
'''
        )

# Orbit around the output layer
parts.append(
    f'''  <g transform="translate(1100 140)">
    <ellipse cx="0" cy="0" rx="58" ry="22" fill="none" stroke="{AMBER}" stroke-width="0.8" opacity="0.35"/>
    <circle r="2.4" fill="{AMBER}" filter="url(#glow)">
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="6s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate" values="58,0" additive="sum" dur="6s" repeatCount="indefinite"/>
    </circle>
  </g>
  <circle cx="1100" cy="140" r="3.2" fill="{AMBER}">
    <animateTransform attributeName="transform" type="rotate" values="0 1100 140;360 1100 140" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="cx" values="1158;1158" dur="6s" repeatCount="indefinite"/>
  </circle>
'''
)

# Cleaner orbit: a circle following an elliptical path
# Replace the messy orbit with animateMotion
parts[-1] = f'''  <ellipse cx="1100" cy="140" rx="58" ry="24" fill="none" stroke="{AMBER}" stroke-width="0.7" opacity="0.28"/>
  <circle r="2.6" fill="{AMBER}" filter="url(#glow)">
    <animateMotion dur="6s" repeatCount="indefinite" path="M1158,140 a58,24 0 1,1 -116,0 a58,24 0 1,1 116,0"/>
  </circle>
'''

parts.append("</svg>\n")

out = Path(__file__).with_name("banner.svg")
out.write_text("".join(parts), encoding="utf-8")
print(f"wrote {out} ({out.stat().st_size} bytes)")
