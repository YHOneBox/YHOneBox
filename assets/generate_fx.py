"""Fashion-tech SVGs for the profile README. Abilities only, no projects."""

from pathlib import Path
import math
import random

CYAN = "#5ce1ff"
PURPLE = "#b794f6"
TEAL = "#2ee6a6"
AMBER = "#f0d48a"
MAGENTA = "#ff4d9a"
INK = "#e8f4ff"
MUTED = "#9bb3c9"
BG = "#050914"
BG2 = "#071226"
OUT = Path(__file__).parent
rng = random.Random(42)


def write(name: str, svg: str) -> None:
    (OUT / name).write_text(svg, encoding="utf-8")


def heading(name: str, title: str, accent: str) -> None:
    write(
        f"heading-{name}.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="56" viewBox="0 0 1200 56" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{BG}"/><stop offset="100%" stop-color="{BG2}"/>
    </linearGradient>
    <linearGradient id="beam" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0"/>
      <stop offset="45%" stop-color="{accent}"/>
      <stop offset="100%" stop-color="{PURPLE}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="56" rx="6" fill="url(#bg)"/>
  <path d="M16,12 V44 M16,12 H38 M16,44 H38" fill="none" stroke="{accent}" stroke-width="1.5"/>
  <path d="M1184,12 V44 M1184,12 H1162 M1184,44 H1162" fill="none" stroke="{accent}" stroke-width="1.5"/>
  <circle cx="54" cy="28" r="4.2" fill="{accent}">
    <animate attributeName="opacity" values="1;0.2;1" dur="1.2s" repeatCount="indefinite"/>
  </circle>
  <text x="72" y="34" fill="{accent}" font-family="IBM Plex Mono, ui-monospace, Consolas, monospace" font-size="17">{title}</text>
  <rect y="50" width="220" height="3" rx="1.5" fill="url(#beam)">
    <animate attributeName="x" values="-220;1200" dur="3.8s" repeatCount="indefinite"/>
  </rect>
</svg>
''',
    )


def matrix() -> None:
    glyphs = list("01YHMLRAGCVX|#*+")
    step = 18
    rows = 14
    loop_h = rows * step
    cols = 16
    streams = []
    for i in range(cols):
        x = 40 + i * 74
        delay = (i * 0.22) % 2.4
        dur = 3.2 + (i % 5) * 0.35
        stream = [rng.choice(glyphs) for _ in range(rows)]
        texts = []
        for copy in (0, 1):
            for j, ch in enumerate(stream):
                y = 16 + j * step + copy * loop_h
                # bright head, fading trail within each stream
                dist = (rows - 1 - j)
                if dist == 0:
                    color, op = CYAN, 1.0
                elif dist < 3:
                    color, op = TEAL, 0.85
                else:
                    color, op = MUTED, max(0.22, 0.7 - dist * 0.05)
                texts.append(
                    f'<text x="0" y="{y}" text-anchor="middle" fill="{color}" opacity="{op:.2f}" '
                    f'font-family="Consolas, ui-monospace, monospace" font-size="15">{ch}</text>'
                )
        streams.append(
            f'''  <g transform="translate({x} 0)">
    <g>
{chr(10).join("      " + t for t in texts)}
      <animateTransform attributeName="transform" type="translate" from="0 0" to="0 -{loop_h}" dur="{dur:.2f}s" begin="-{delay:.2f}s" repeatCount="indefinite"/>
    </g>
  </g>'''
        )
    write(
        "matrix.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="180" viewBox="0 0 1200 180" role="img" aria-label="Matrix rain">
  <rect width="1200" height="180" fill="{BG}"/>
{chr(10).join(streams)}
</svg>
''',
    )


def radar() -> None:
    labels = [
        (0, "VISION"),
        (60, "LLM"),
        (120, "RAG"),
        (180, "EDGE"),
        (240, "DEPLOY"),
        (300, "SYSTEMS"),
    ]
    cx, cy, r = 220, 150, 110
    rings = "".join(
        f'<circle cx="{cx}" cy="{cy}" r="{rad}" fill="none" stroke="{CYAN}" stroke-opacity="{op}"/>'
        for rad, op in ((36, 0.15), (68, 0.2), (100, 0.28), (110, 0.45))
    )
    spokes = "".join(
        f'<line x1="{cx}" y1="{cy}" x2="{cx + r * math.cos(math.radians(a - 90)):.1f}" '
        f'y2="{cy + r * math.sin(math.radians(a - 90)):.1f}" stroke="{CYAN}" stroke-opacity="0.18"/>'
        for a in range(0, 360, 30)
    )
    labs = []
    for ang, name in labels:
        x = cx + 132 * math.cos(math.radians(ang - 90))
        y = cy + 132 * math.sin(math.radians(ang - 90))
        labs.append(
            f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" fill="{TEAL}" '
            f'font-family="IBM Plex Mono, Consolas, monospace" font-size="11">{name}</text>'
        )
    # ability blips
    blips = [(70, 0.72), (140, 0.55), (210, 0.8), (300, 0.62)]
    dots = []
    for ang, dist in blips:
        x = cx + r * dist * math.cos(math.radians(ang - 90))
        y = cy + r * dist * math.sin(math.radians(ang - 90))
        dots.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" fill="{AMBER}">'
            f'<animate attributeName="opacity" values="1;0.2;1" dur="1.8s" repeatCount="indefinite"/></circle>'
        )
    write(
        "radar.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="Ability radar">
  <rect width="1200" height="300" rx="10" fill="{BG}"/>
  {rings}{spokes}
  <path d="M{cx},{cy} L{cx},{cy - r} A{r},{r} 0 0 1 {cx + r},{cy} Z" fill="{CYAN}" fill-opacity="0.16">
    <animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="4s" repeatCount="indefinite"/>
  </path>
  <circle cx="{cx}" cy="{cy}" r="3" fill="{CYAN}"/>
  {"".join(dots)}
  {"".join(labs)}
  <g font-family="IBM Plex Mono, Consolas, monospace" fill="{INK}">
    <text x="480" y="70" font-size="20" fill="{CYAN}">CORE ABILITIES</text>
    <text x="480" y="108" font-size="14" fill="{MUTED}">computer vision · detection · multimodal input</text>
    <text x="480" y="138" font-size="14" fill="{MUTED}">llm systems · rag · model routing · tool use</text>
    <text x="480" y="168" font-size="14" fill="{MUTED}">edge inference · containers · linux · jetson</text>
    <text x="480" y="198" font-size="14" fill="{MUTED}">speech in / speech out · asr · tts</text>
    <text x="480" y="228" font-size="14" fill="{MUTED}">full-stack around the model · apis · realtime ui</text>
    <text x="480" y="268" font-size="12" fill="{PURPLE}">EN  ·  ZH  ·  Python first</text>
  </g>
</svg>
''',
    )


def meters() -> None:
    rows = [
        ("COMPUTER VISION", 0.90, CYAN),
        ("LLM / RAG SYSTEMS", 0.88, PURPLE),
        ("EDGE + DEPLOY", 0.82, TEAL),
        ("MULTIMODAL IO", 0.80, AMBER),
        ("SYSTEMS INTEGRATION", 0.86, MAGENTA),
    ]
    blocks = []
    for i, (label, frac, color) in enumerate(rows):
        y = 28 + i * 42
        w = int(760 * frac)
        blocks.append(
            f'''  <text x="36" y="{y + 14}" fill="{MUTED}" font-family="IBM Plex Mono, Consolas, monospace" font-size="13">{label}</text>
  <rect x="360" y="{y}" width="760" height="16" rx="8" fill="#0b1220" stroke="{color}" stroke-opacity="0.25"/>
  <rect x="360" y="{y}" width="24" height="16" rx="8" fill="{color}" filter="url(#glow)">
    <animate attributeName="width" values="24;{w};{int(w * 0.92)};{w}" dur="{2.8 + i * 0.25:.2f}s" repeatCount="indefinite"/>
  </rect>
  <text x="1140" y="{y + 14}" text-anchor="end" fill="{color}" font-family="IBM Plex Mono, Consolas, monospace" font-size="12">{int(frac * 100):02d}</text>'''
        )
    write(
        "meters.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="250" viewBox="0 0 1200 250" role="img" aria-label="Ability meters">
  <defs>
    <filter id="glow" x="-10%" y="-50%" width="120%" height="200%">
      <feGaussianBlur stdDeviation="2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="1200" height="250" rx="10" fill="{BG}"/>
{chr(10).join(blocks)}
</svg>
''',
    )


def equalizer() -> None:
    bars = []
    for i in range(48):
        x = 30 + i * 24
        h = 20 + (i * 17) % 90
        color = (CYAN, PURPLE, TEAL, AMBER, MAGENTA)[i % 5]
        bars.append(
            f'''  <rect x="{x}" y="{140 - h}" width="12" height="{h}" rx="3" fill="{color}" opacity="0.85">
    <animate attributeName="height" values="{h};{12 + (i * 13) % 110};{h}" dur="{0.7 + (i % 7) * 0.18:.2f}s" repeatCount="indefinite"/>
    <animate attributeName="y" values="{140 - h};{140 - (12 + (i * 13) % 110)};{140 - h}" dur="{0.7 + (i % 7) * 0.18:.2f}s" repeatCount="indefinite"/>
  </rect>'''
        )
    write(
        "equalizer.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="160" viewBox="0 0 1200 160" role="img" aria-label="Signal equalizer">
  <rect width="1200" height="160" rx="8" fill="{BG}"/>
{chr(10).join(bars)}
</svg>
''',
    )


def hexgrid() -> None:
    hexes = []
    s = 16
    w = s * math.sqrt(3)
    for row in range(5):
        for col in range(18):
            x = 28 + col * w + (row % 2) * (w / 2)
            y = 18 + row * (s * 1.5)
            pts = []
            for k in range(6):
                ang = math.radians(60 * k - 30)
                pts.append(f"{x + s * math.cos(ang):.1f},{y + s * math.sin(ang):.1f}")
            delay = (row + col) * 0.08
            color = CYAN if (row + col) % 3 == 0 else (PURPLE if (row + col) % 3 == 1 else TEAL)
            hexes.append(
                f'<polygon points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="0.8" opacity="0.15">'
                f'<animate attributeName="opacity" values="0.12;0.7;0.12" dur="3.2s" begin="{delay:.2f}s" repeatCount="indefinite"/>'
                f"</polygon>"
            )
    write(
        "hexgrid.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="150" viewBox="0 0 1200 150" role="img" aria-label="Hex grid">
  <rect width="1200" height="150" fill="{BG}"/>
{"".join(hexes)}
</svg>
''',
    )


def dashboard() -> None:
    cards = [
        (40, "VISION", "CNN / YOLO / OpenCV", CYAN, "SEE"),
        (330, "LANGUAGE", "LLM · RAG · routing", PURPLE, "TALK"),
        (620, "EDGE", "Docker · Jetson · K8s", TEAL, "SHIP"),
        (910, "SYSTEMS", "APIs · realtime UI", AMBER, "WIRE"),
    ]
    bits = []
    for x, title, body, color, tag in cards:
        bits.append(
            f'''  <g transform="translate({x} 24)">
    <rect width="250" height="150" rx="10" fill="{BG2}" stroke="{color}" stroke-opacity="0.45"/>
    <rect width="250" height="3" rx="1.5" fill="{color}">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2.2s" repeatCount="indefinite"/>
    </rect>
    <text x="18" y="36" fill="{color}" font-family="IBM Plex Mono, Consolas, monospace" font-size="11">{tag}</text>
    <text x="18" y="70" fill="{INK}" font-family="IBM Plex Mono, Consolas, monospace" font-size="20">{title}</text>
    <text x="18" y="102" fill="{MUTED}" font-family="IBM Plex Mono, Consolas, monospace" font-size="12">{body}</text>
    <circle cx="220" cy="28" r="5" fill="{color}">
      <animate attributeName="opacity" values="1;0.15;1" dur="1.4s" repeatCount="indefinite"/>
    </circle>
  </g>'''
        )
    write(
        "dashboard.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="200" viewBox="0 0 1200 200" role="img" aria-label="Ability dashboard">
  <rect width="1200" height="200" rx="10" fill="{BG}"/>
{chr(10).join(bits)}
</svg>
''',
    )


def boot() -> None:
    lines = [
        ("$ boot --profile yh", INK, 0),
        ("loading neural runtime ............ ok", TEAL, 0.35),
        ("mounting vision stack ............. ok", CYAN, 0.7),
        ("linking llm / rag fabric .......... ok", PURPLE, 1.05),
        ("edge runtime · docker · linux ..... ok", TEAL, 1.4),
        ("locale: english ................... ok", AMBER, 1.75),
        ("status: online · still compiling", CYAN, 2.1),
    ]
    texts = []
    y = 48
    for content, color, delay in lines:
        texts.append(
            f'''  <text x="36" y="{y}" fill="{color}" font-family="IBM Plex Mono, Consolas, monospace" font-size="15" opacity="0">{content}
    <animate attributeName="opacity" values="0;1" dur="0.15s" begin="{delay}s" fill="freeze"/>
  </text>'''
        )
        y += 26
    write(
        "boot.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="260" viewBox="0 0 1200 260" role="img" aria-label="System boot">
  <rect width="1200" height="260" rx="10" fill="{BG2}" stroke="{CYAN}" stroke-opacity="0.25"/>
  <circle cx="28" cy="22" r="6" fill="#ff5f56"/>
  <circle cx="50" cy="22" r="6" fill="#ffbd2e"/>
  <circle cx="72" cy="22" r="6" fill="#27c93f"/>
  <text x="96" y="26" fill="{MUTED}" font-family="IBM Plex Mono, Consolas, monospace" font-size="12">yh@oregon ~ neural-shell</text>
  <line x1="0" y1="40" x2="1200" y2="40" stroke="{CYAN}" stroke-opacity="0.14"/>
{chr(10).join(texts)}
  <rect x="36" y="232" width="10" height="16" fill="{AMBER}">
    <animate attributeName="opacity" values="1;0;1" dur="0.85s" begin="2.2s" repeatCount="indefinite"/>
  </rect>
</svg>
''',
    )


def chips() -> None:
    items = [
        (80, 40, "VISION", CYAN),
        (230, 78, "RAG", PURPLE),
        (140, 120, "YOLO", TEAL),
        (400, 36, "ASR / TTS", AMBER),
        (540, 96, "EDGE", CYAN),
        (700, 40, "TRANSFORMERS", PURPLE),
        (860, 108, "JETSON", TEAL),
        (1000, 50, "MULTIMODAL", CYAN),
        (320, 140, "PYTHON", INK),
        (640, 148, "DOCKER", AMBER),
        (900, 156, "K8S", PURPLE),
    ]
    bubbles = []
    for i, (x, y, label, color) in enumerate(items):
        w = len(label) * 9 + 22
        bubbles.append(
            f'''  <g>
    <rect x="{x}" y="{y}" width="{w}" height="26" rx="13" fill="#071226" stroke="{color}"/>
    <text x="{x + w / 2:.1f}" y="{y + 17}" text-anchor="middle" fill="{color}" font-family="IBM Plex Mono, Consolas, monospace" font-size="12">{label}</text>
    <animateTransform attributeName="transform" type="translate" values="0 0;0 -6;0 0" dur="{3.1 + i * 0.16:.2f}s" repeatCount="indefinite"/>
  </g>'''
        )
    write(
        "chips.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="190" viewBox="0 0 1200 190" role="img" aria-label="Ability chips">
  <rect width="1200" height="190" rx="8" fill="{BG}"/>
{chr(10).join(bubbles)}
</svg>
''',
    )


def glitch() -> None:
    write(
        "glitch.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="90" viewBox="0 0 1200 90" role="img" aria-label="YH">
  <rect width="1200" height="90" fill="{BG}"/>
  <text id="a" x="600" y="58" text-anchor="middle" font-family="IBM Plex Mono, Consolas, monospace" font-size="36" fill="{CYAN}">YI-HO CHANG</text>
  <text x="604" y="58" text-anchor="middle" font-family="IBM Plex Mono, Consolas, monospace" font-size="36" fill="{MAGENTA}" opacity="0.4">YI-HO CHANG
    <animate attributeName="x" values="604;610;598;604" dur="0.4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.15;0.5;0.1;0.4" dur="0.35s" repeatCount="indefinite"/>
  </text>
  <text x="596" y="58" text-anchor="middle" font-family="IBM Plex Mono, Consolas, monospace" font-size="36" fill="{TEAL}" opacity="0.3">YI-HO CHANG
    <animate attributeName="x" values="596;590;602;596" dur="0.45s" repeatCount="indefinite"/>
  </text>
</svg>
''',
    )


def footer() -> None:
    write(
        "footer.svg",
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="100" viewBox="0 0 1200 100" role="img" aria-label="signal end">
  <rect width="1200" height="100" fill="{BG}"/>
  <path fill="none" stroke="{CYAN}" stroke-width="1.6" opacity="0.85"
    d="M0,42 Q150,12 300,42 T600,42 T900,42 T1200,42">
    <animate attributeName="d" dur="5s" repeatCount="indefinite"
      values="M0,42 Q150,12 300,42 T600,42 T900,42 T1200,42;M0,42 Q150,72 300,42 T600,42 T900,42 T1200,42;M0,42 Q150,12 300,42 T600,42 T900,42 T1200,42"/>
  </path>
  <path fill="none" stroke="{PURPLE}" stroke-width="1.2" opacity="0.55"
    d="M0,54 Q150,78 300,54 T600,54 T900,54 T1200,54">
    <animate attributeName="d" dur="6.5s" repeatCount="indefinite"
      values="M0,54 Q150,78 300,54 T600,54 T900,54 T1200,54;M0,54 Q150,30 300,54 T600,54 T900,54 T1200,54;M0,54 Q150,78 300,54 T600,54 T900,54 T1200,54"/>
  </path>
  <text x="600" y="86" text-anchor="middle" fill="{MUTED}" font-family="IBM Plex Mono, Consolas, monospace" font-size="13">// end of transmission</text>
</svg>
''',
    )


if __name__ == "__main__":
    heading("deck", "▸  SYSTEM DECK", CYAN)
    heading("core", "▸  ABILITY CORE", PURPLE)
    heading("link", "▸  UPLINK", AMBER)
    matrix()
    radar()
    meters()
    equalizer()
    hexgrid()
    dashboard()
    boot()
    chips()
    glitch()
    footer()
    print("wrote fx svgs")
