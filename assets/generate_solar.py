"""Hero intro and animated solar system for the profile README."""

from pathlib import Path
import random

OUT = Path(__file__).parent
rng = random.Random(7)
BG = "#04060f"
INK = "#e8f4ff"
MUTED = "#8aa0b8"
CYAN = "#5ce1ff"


def write(name: str, svg: str) -> None:
    (OUT / name).write_text(svg, encoding="utf-8")


def stars(n: int, w: int, h: int) -> str:
    bits = []
    for i in range(n):
        x = rng.randint(8, w - 8)
        y = rng.randint(8, h - 8)
        r = 0.6 if i % 4 else 1.1
        op = 0.25 + (i % 5) * 0.12
        bits.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#d7ecff" opacity="{op:.2f}"/>')
    return "\n".join(bits)


def hero() -> None:
    write(
        "hero.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="240" viewBox="0 0 1200 240" role="img" aria-label="Yi-Ho Chang, AI Engineer">
  <defs>
    <radialGradient id="sun" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff4c4"/>
      <stop offset="45%" stop-color="#ffb347"/>
      <stop offset="100%" stop-color="#ff7a18" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="name" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{INK}"/>
      <stop offset="100%" stop-color="{CYAN}"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="240" fill="{BG}"/>
  {stars(28, 1200, 240)}
  <circle cx="1080" cy="70" r="46" fill="url(#sun)"/>
  <ellipse cx="1080" cy="70" rx="70" ry="16" fill="none" stroke="{CYAN}" stroke-opacity="0.28">
    <animateTransform attributeName="transform" type="rotate" from="0 1080 70" to="360 1080 70" dur="14s" repeatCount="indefinite"/>
  </ellipse>
  <text x="64" y="108" fill="url(#name)" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="48" font-weight="600">Yi-Ho Chang</text>
  <text x="66" y="142" fill="{MUTED}" font-family="Consolas, ui-monospace, monospace" font-size="16">AI ENGINEER</text>
  <text x="66" y="178" fill="{CYAN}" font-family="Consolas, ui-monospace, monospace" font-size="14">vision x language  ·  models that work as one</text>
</svg>
''',
    )


def solar() -> None:
    cx, cy = 600, 360
    # Keep the outermost orbit inside the 720px viewBox (plus legend).
    planets = [
        ("Mercury", 55, 3.2, "#c2c2c2", 3.6),
        ("Venus", 82, 5.0, "#e6c07b", 5.8),
        ("Earth", 112, 5.6, "#3d8bfd", 8.0),
        ("Mars", 142, 4.4, "#d07050", 11.0),
        ("Jupiter", 188, 13.0, "#d4a574", 18.0),
        ("Saturn", 236, 11.0, "#e8d5a3", 24.0),
        ("Uranus", 278, 8.0, "#7fddd9", 32.0),
        ("Neptune", 318, 7.6, "#4b6cff", 40.0),
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720" role="img" aria-label="Solar system">'
        f'<rect width="1200" height="720" fill="{BG}"/>',
        stars(40, 1200, 720),
        f'''  <defs>
    <radialGradient id="core" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff6c8"/>
      <stop offset="40%" stop-color="#ffb347"/>
      <stop offset="100%" stop-color="#ff6a00" stop-opacity="0.15"/>
    </radialGradient>
  </defs>
  <circle cx="{cx}" cy="{cy}" r="26" fill="url(#core)"/>
  <circle cx="{cx}" cy="{cy}" r="14" fill="#ffd27a"/>
  <text x="{cx}" y="{cy + 52}" text-anchor="middle" fill="#ffd27a" font-family="Consolas, ui-monospace, monospace" font-size="11">SUN</text>
''',
    ]
    for name, orbit, pr, color, dur in planets:
        parts.append(
            f'<ellipse cx="{cx}" cy="{cy}" rx="{orbit}" ry="{orbit}" fill="none" stroke="#5ce1ff" stroke-opacity="0.18"/>'
        )
        extras = ""
        if name == "Saturn":
            extras = (
                f'<ellipse cx="{orbit}" cy="0" rx="{pr + 10}" ry="{pr * 0.35}" fill="none" '
                f'stroke="#e8d5a3" stroke-width="2" opacity="0.85"/>'
            )
        elif name == "Earth":
            extras = f'<circle cx="{orbit + 10}" cy="-2" r="1.7" fill="#cfd8e6"/>'
        elif name == "Jupiter":
            extras = f'<circle cx="{orbit}" cy="0" r="{pr * 0.55}" fill="#c48a5a" opacity="0.45"/>'
        parts.append(
            f'''  <g transform="translate({cx} {cy})">
    <g>
      <circle cx="{orbit}" cy="0" r="{pr}" fill="{color}"/>
      {extras}
      <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="{dur}s" repeatCount="indefinite"/>
    </g>
  </g>'''
        )
    legend = "  ·  ".join(name for name, *_ in planets)
    parts.append(
        f'<text x="600" y="700" text-anchor="middle" fill="#8aa0b8" font-family="Consolas, ui-monospace, monospace" font-size="12">{legend}</text>'
    )
    parts.append("</svg>\n")
    write("solar-system.svg", "".join(parts))


if __name__ == "__main__":
    hero()
    solar()
    print("wrote hero and solar system")
