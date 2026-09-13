"""Decorative SVGs for the profile README."""

from pathlib import Path

CYAN = "#5ce1ff"
PURPLE = "#b794f6"
TEAL = "#2ee6a6"
AMBER = "#f0d48a"
INK = "#e8f4ff"
MUTED = "#9bb3c9"
BG = "#050914"
BG2 = "#071226"

OUT = Path(__file__).parent


def heading(name: str, title: str, accent: str) -> None:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="52" viewBox="0 0 1200 52" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{BG}"/>
      <stop offset="100%" stop-color="{BG2}"/>
    </linearGradient>
    <linearGradient id="beam" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{accent}" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="{PURPLE}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="52" rx="6" fill="url(#g)"/>
  <path d="M18,10 V42 M18,10 H36 M18,42 H36" fill="none" stroke="{accent}" stroke-width="1.4"/>
  <path d="M1182,10 V42 M1182,10 H1164 M1182,42 H1164" fill="none" stroke="{accent}" stroke-width="1.4"/>
  <circle cx="56" cy="26" r="4" fill="{accent}">
    <animate attributeName="opacity" values="1;0.25;1" dur="1.5s" repeatCount="indefinite"/>
  </circle>
  <text x="74" y="32" fill="{accent}" font-family="IBM Plex Mono, ui-monospace, Consolas, monospace" font-size="16">{title}</text>
  <rect x="40" y="46" width="160" height="3" rx="1.5" fill="url(#beam)">
    <animate attributeName="x" values="40;980;40" dur="5.5s" repeatCount="indefinite"/>
  </rect>
</svg>
'''
    (OUT / f"heading-{name}.svg").write_text(svg, encoding="utf-8")


def boot() -> None:
    lines = [
        ("$ whoami", INK, 0),
        ("yh  ·  ai engineer  ·  oregon", TEAL, 0.4),
        ("$ cat ~/now.txt", INK, 0.9),
        ("avatars that talk back · drones that see weeds · llms with a human in the loop", CYAN, 1.3),
        ("$ ping universe", INK, 1.8),
        ("64 bytes from curiosity: ttl=∞", PURPLE, 2.2),
        ("_", AMBER, 2.6),
    ]
    texts = []
    y = 42
    for content, color, delay in lines:
        texts.append(
            f'''  <text x="36" y="{y}" fill="{color}" font-family="IBM Plex Mono, ui-monospace, Consolas, monospace" font-size="15" opacity="0">{content}
    <animate attributeName="opacity" values="0;1" dur="0.2s" begin="{delay}s" fill="freeze"/>
  </text>'''
        )
        y += 28
    texts.append(
        f'''  <rect x="36" y="226" width="10" height="16" fill="{AMBER}">
    <animate attributeName="opacity" values="1;0;1" dur="0.9s" begin="2.6s" repeatCount="indefinite"/>
  </rect>'''
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="260" viewBox="0 0 1200 260" role="img" aria-label="Terminal intro">
  <defs>
    <linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#071226"/>
      <stop offset="100%" stop-color="#050914"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="260" rx="10" fill="url(#panel)" stroke="{CYAN}" stroke-opacity="0.22"/>
  <circle cx="28" cy="22" r="6" fill="#ff5f56"/>
  <circle cx="50" cy="22" r="6" fill="#ffbd2e"/>
  <circle cx="72" cy="22" r="6" fill="#27c93f"/>
  <text x="96" y="26" fill="{MUTED}" font-family="IBM Plex Mono, ui-monospace, Consolas, monospace" font-size="12">yh@oregon ~ zsh</text>
  <line x1="0" y1="40" x2="1200" y2="40" stroke="{CYAN}" stroke-opacity="0.12"/>
{chr(10).join(texts)}
</svg>
'''
    (OUT / "boot.svg").write_text(svg, encoding="utf-8")


def footer() -> None:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="90" viewBox="0 0 1200 90" role="img" aria-label="See you in the logs">
  <defs>
    <linearGradient id="wave" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{CYAN}"/>
      <stop offset="50%" stop-color="{PURPLE}"/>
      <stop offset="100%" stop-color="{TEAL}"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="90" fill="{BG}"/>
  <path d="M0,40 Q150,10 300,40 T600,40 T900,40 T1200,40" fill="none" stroke="url(#wave)" stroke-width="2" opacity="0.85">
    <animate attributeName="d" dur="6s" repeatCount="indefinite"
      values="M0,40 Q150,10 300,40 T600,40 T900,40 T1200,40;M0,40 Q150,70 300,40 T600,40 T900,40 T1200,40;M0,40 Q150,10 300,40 T600,40 T900,40 T1200,40"/>
  </path>
  <text x="600" y="72" text-anchor="middle" fill="{MUTED}" font-family="IBM Plex Mono, ui-monospace, Consolas, monospace" font-size="13">see you in the logs</text>
</svg>
'''
    (OUT / "footer.svg").write_text(svg, encoding="utf-8")


def chips() -> None:
    items = [
        (90, 36, "VISION", CYAN),
        (250, 70, "RAG", PURPLE),
        (150, 110, "YOLO", TEAL),
        (420, 40, "TTS / ASR", AMBER),
        (560, 88, "EDGE", CYAN),
        (720, 36, "AVATARS", PURPLE),
        (860, 100, "JETSON", TEAL),
        (1000, 48, "MULTIMODAL", CYAN),
        (340, 130, "PYTHON", INK),
        (680, 140, "DOCKER", AMBER),
        (920, 150, "LLM ROUTING", PURPLE),
    ]
    bubbles = []
    for i, (x, y, label, color) in enumerate(items):
        bubbles.append(
            f'''  <g transform="translate({x} {y})">
    <rect x="-8" y="-16" width="{len(label) * 9 + 20}" height="26" rx="13" fill="#071226" stroke="{color}" stroke-width="1"/>
    <text x="{len(label) * 4.5 + 2}" y="3" text-anchor="middle" fill="{color}" font-family="IBM Plex Mono, ui-monospace, Consolas, monospace" font-size="12">{label}</text>
    <animateTransform attributeName="transform" type="translate" values="{x},{y};{x},{y - 6};{x},{y}" dur="{3.2 + i * 0.17:.2f}s" repeatCount="indefinite"/>
  </g>'''
        )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="180" viewBox="0 0 1200 180" role="img" aria-label="Things I like building">
  <rect width="1200" height="180" rx="8" fill="{BG}"/>
{chr(10).join(bubbles)}
</svg>
'''
    (OUT / "chips.svg").write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    heading("now", "▸  NOW PLAYING", TEAL)
    heading("lab", "▸  THE LAB", CYAN)
    heading("kit", "▸  TOOLKIT", PURPLE)
    heading("sig", "▸  SIGNAL", AMBER)
    boot()
    footer()
    chips()
    print("wrote decorative svgs")
