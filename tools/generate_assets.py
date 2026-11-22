"""Генератор анимированных SVG для профиля acciv в стиле LePhiAnhDev.

Как у референса: широкие панели со встроенными CSS/SMIL-анимациями,
тихий тёмный фон, аккуратная типографика, минимум «кибер-шума».
Без JavaScript и внешних ассетов.

Запуск: python3 tools/generate_assets.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(parents=True, exist_ok=True)
STATS = json.loads((ROOT / "data" / "profile-stats.json").read_text(encoding="utf-8"))

BG = "#0D1117"
PANEL = "#111722"
PANEL2 = "#161C28"
GRID = "#212936"
TEXT = "#E6EDF3"
MUTED = "#8B949E"
GREEN = "#7AA2F7"
CYAN = "#BB9AF7"
RED = "#F7768E"
AMBER = "#E0AF68"
BLUE = "#7DCFFF"

FONT = "-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif"
MONO = "'JetBrains Mono','Fira Code',Consolas,'Courier New',monospace"

HEAD = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
    'viewBox="0 0 {w} {h}" font-family="{font}" xml:space="preserve">'
)

STYLE = """<style>
.k{animation:kb 1.1s steps(1) infinite}@keyframes kb{50%{opacity:0}}
.f{animation:fi 5s infinite}@keyframes fi{0%,96%,100%{opacity:1}98%{opacity:.72}}
.p{animation:pu 3s ease-in-out infinite}@keyframes pu{50%{opacity:.45}}
.s{animation:sl 7s linear infinite}@keyframes sl{0%{transform:translateY(-30px)}100%{transform:translateY(250px)}}
.deg{animation:dg 22s linear infinite;transform-origin:427px 115px}@keyframes dg{to{transform:rotate(360deg)}}
.rv{animation:dg 34s linear infinite reverse;transform-origin:427px 115px}
.ty{overflow:hidden;white-space:nowrap;animation:ty 3s steps(34) infinite}@keyframes ty{0%{width:0}65%,100%{width:100%}}
</style>"""


def save(name: str, body: str) -> None:
    (OUT / name).write_text(body, encoding="utf-8")
    print(f"  + {name}")


def shell(w: int, h: int, inner: str, font: str = FONT) -> str:
    return (
        HEAD.format(w=w, h=h, font=font)
        + STYLE
        + f'<rect width="{w}" height="{h}" fill="{BG}"/>'
        + inner
        + "</svg>"
    )


def header() -> None:
    w, h = 854, 230
    inner = f"""
<defs>
<linearGradient id="hg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="{GREEN}"/><stop offset=".55" stop-color="{CYAN}"/>
  <stop offset="1" stop-color="{BLUE}"/>
</linearGradient>
<linearGradient id="hf" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="{PANEL2}" stop-opacity=".2"/>
  <stop offset="1" stop-color="{BG}" stop-opacity="1"/>
</linearGradient>
</defs>
<g opacity=".55" stroke="{GRID}" stroke-width="1">
  {''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>' for x in range(0, w + 1, 42))}
  {''.join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}"/>' for y in range(0, h + 1, 38))}
</g>
<circle cx="427" cy="115" r="105" fill="none" stroke="{GRID}" stroke-dasharray="3 9" class="deg"/>
<circle cx="427" cy="115" r="135" fill="none" stroke="{GRID}" stroke-dasharray="2 12" class="rv"/>
<rect x="36" y="36" width="782" height="158" rx="14" fill="url(#hf)" stroke="{GRID}"/>
<rect x="36" y="36" width="4" height="158" rx="2" fill="url(#hg)"/>
<text x="64" y="94" font-size="66" font-weight="700" fill="{TEXT}" letter-spacing="3">acciv</text>
<rect x="64" y="112" width="186" height="1" fill="url(#hg)"/>
<text x="64" y="144" font-size="21" fill="{GREEN}">API keys · auth · security</text>
<text x="64" y="173" font-size="12" fill="{MUTED}" letter-spacing="1">Rust · Go · Python · C++ · Java · PHP</text>
<text x="790" y="66" text-anchor="end" font-size="10" fill="{RED}" letter-spacing="2">STATUS: ACTIVE <tspan class="k">█</tspan></text>
<g transform="translate(690 132)" class="p">
  <circle cx="0" cy="0" r="26" fill="none" stroke="{CYAN}" stroke-opacity=".5"/>
  <circle cx="0" cy="0" r="17" fill="none" stroke="{GREEN}" stroke-dasharray="4 6"/>
  <circle cx="0" cy="0" r="5" fill="{CYAN}"/>
</g>
<rect x="0" y="0" width="{w}" height="2" fill="url(#hg)" opacity=".55" class="f"/>
"""
    save("header.svg", shell(w, h, inner))


def typing() -> None:
    w, h = 854, 80
    phrases = [
        "API keys, schemas, contract tests",
        "Rust cores, Go services, Python reports",
        "Structure first. No brute force.",
        "6 projects · 7 languages · 191 commits",
    ]
    texts = []
    for i, phrase in enumerate(phrases):
        texts.append(
            f'<text x="54" y="46" font-size="17" fill="{TEXT if i == 0 else MUTED}" '
            f'opacity="0"><set attributeName="opacity" to="1" begin="{i * 3}s" fill="freeze"/>'
            f'<set attributeName="opacity" to="0" begin="{(i + 1) * 3}s" fill="freeze"/>{phrase}</text>'
        )
    inner = f"""
<rect x="20" y="14" width="814" height="52" rx="10" fill="{PANEL}" stroke="{GRID}"/>
<text x="28" y="46" font-size="15" fill="{GREEN}">$</text>
{''.join(texts)}
<text x="54" y="46" font-size="17" fill="{TEXT}" class="ty">API keys, schemas, contract tests</text>
<text x="822" y="46" text-anchor="end" font-size="11" fill="{MUTED}" class="k">_</text>
"""
    save("typing.svg", shell(w, h, inner, MONO))


def about() -> None:
    w, h = 854, 190
    inner = f"""
<rect x="20" y="16" width="814" height="158" rx="12" fill="{PANEL}" stroke="{GRID}"/>
<text x="44" y="50" font-size="11" fill="{GREEN}" letter-spacing="3">ABOUT</text>
<text x="44" y="84" font-size="17" fill="{TEXT}">Делаю инструменты вокруг API: ключи, схемы, контракты, трафик.</text>
<text x="44" y="112" font-size="14" fill="{MUTED}">Смотрю на структуру и форматы, а не на взлом и обход авторизации.</text>
<text x="44" y="140" font-size="14" fill="{MUTED}">В репозиториях — тесты, демо и понятный вывод. тестовые ключи — фейковые.</text>
<circle cx="790" cy="96" r="30" fill="none" stroke="{GRID}" stroke-dasharray="4 7" class="deg"/>
<circle cx="790" cy="96" r="8" fill="{GREEN}" class="p"/>
"""
    save("about.svg", shell(w, h, inner))


def about_narrow() -> None:
    w, h = 854, 220
    inner = f"""
<rect x="20" y="16" width="814" height="188" rx="12" fill="{PANEL}" stroke="{GRID}"/>
<text x="44" y="50" font-size="11" fill="{GREEN}" letter-spacing="3">ABOUT</text>
<text x="44" y="86" font-size="17" fill="{TEXT}">Инструменты вокруг API: ключи, схемы, контракты, трафик.</text>
<text x="44" y="116" font-size="14" fill="{MUTED}">Структура и форматы вместо взлома и обхода авторизации.</text>
<text x="44" y="144" font-size="14" fill="{MUTED}">В репозиториях — тесты, демо и понятный вывод.</text>
<text x="44" y="172" font-size="14" fill="{MUTED}">тестовые ключи всегда фейковые.</text>
<g class="p"><circle cx="790" cy="108" r="25" fill="none" stroke="{CYAN}" stroke-opacity=".55"/>
<circle cx="790" cy="108" r="6" fill="{CYAN}"/></g>
"""
    save("about-narrow.svg", shell(w, h, inner))


def stack() -> None:
    w, h = 854, 120
    items = ["Rust", "Go", "Python", "C ++", "Java", "PHP", "C ABI", "OpenAPI", "Docker"]
    cells = []
    for i, label in enumerate(items):
        x = 20 + i * 92
        cells.append(
            f'<rect x="{x}" y="28" width="82" height="64" rx="8" fill="{PANEL2}" stroke="{GRID}"/>'
            f'<text x="{x + 41}" y="66" text-anchor="middle" font-size="12" '
            f'fill="{GREEN if i % 2 == 0 else CYAN}">{label}</text>'
        )
    inner = f"""
<text x="20" y="20" font-size="10" fill="{MUTED}" letter-spacing="3">STACK</text>
{''.join(cells)}
"""
    save("stack.svg", shell(w, h, inner, MONO))


def footer() -> None:
    w, h = 854, 120
    inner = f"""
<rect x="20" y="16" width="814" height="88" rx="12" fill="{PANEL}" stroke="{GRID}"/>
<text x="427" y="54" text-anchor="middle" font-size="12" fill="{MUTED}" letter-spacing="3">jumpscout@proton.me · Krasnodar</text>
<text x="427" y="82" text-anchor="middle" font-size="12" fill="{GREEN}" letter-spacing="2">NO BRUTE FORCE <tspan class="k">█</tspan></text>
"""
    save("footer.svg", shell(w, h, inner, MONO))


def heading(text: str, color: str = GREEN) -> str:
    return (
        f'<text x="20" y="30" font-size="11" fill="{color}" letter-spacing="3" '
        f'font-family="{MONO}">{text}</text>'
    )


def stats() -> None:
    w, h = 854, 170
    cells = [
        (str(STATS["public_repos"]), "REPOS", GREEN),
        (str(STATS["commits"]), "COMMITS", CYAN),
        (str(len(STATS["languages"])), "LANGUAGES", BLUE),
        (str(STATS["activity_total"]), "COMMITS / 12 WEEKS", AMBER),
    ]
    items = []
    for i, (value, label, color) in enumerate(cells):
        x = 20 + i * 207
        items.append(
            f'<rect x="{x}" y="48" width="193" height="100" rx="10" fill="{PANEL}" stroke="{GRID}"/>'
            f'<text x="{x + 96}" y="100" text-anchor="middle" font-size="34" font-weight="700" fill="{color}">{value}</text>'
            f'<text x="{x + 96}" y="128" text-anchor="middle" font-size="10" fill="{MUTED}" letter-spacing="1.5">{label}</text>'
        )
    inner = heading("[ ACTIVITY ]", RED) + "".join(items)
    save("stats.svg", shell(w, h, inner, MONO))


def languages() -> None:
    w, h = 854, 300
    colors = [GREEN, CYAN, BLUE, AMBER, RED, "#9ECE6A", "#FF9E64"]
    lang_items = STATS["languages"][:10]
    total = sum(size for _, size in STATS["languages"]) or 1
    bars, labels = [], []
    y = 58
    for i, (lang, size) in enumerate(lang_items):
        pct = size / total
        width = max(3, int(690 * pct))
        color = colors[i % len(colors)]
        bars.append(
            f'<rect x="132" y="{y}" width="{width}" height="14" rx="4" fill="{color}" opacity=".85">'
            f'<animate attributeName="width" from="0" to="{width}" dur="0.8s" begin="{i * 0.12}s" fill="freeze"/></rect>'
        )
        labels.append(
            f'<text x="20" y="{y + 12}" font-size="11" fill="{TEXT}">{lang}</text>'
            f'<text x="834" y="{y + 12}" text-anchor="end" font-size="10" fill="{MUTED}">{pct * 100:.1f}%</text>'
        )
        y += 25
    inner = heading("[ LANGUAGES ]", CYAN) + "".join(labels) + "".join(bars)
    save("languages.svg", shell(w, h, inner, MONO))


def projects() -> None:
    w, h = 854, 610
    names = ["keylens", "apixray", "keygate", "apishadow", "schema-registry", "apifuzz"]
    counts = STATS.get("commits_by_repo", {})
    descs = [
        "поиск утекших ключей в файлах",
        "разбор структуры ключей и JWT",
        "gateway для ключей с политиками и аудитом",
        "зеркало API-трафика и поиск расхождений",
        "версии API-схем и проверка совместимости",
        "запросы из OpenAPI и проверка контракта",
    ]
    tags = [
        "PY · RUST · C++",
        "RUST · C ABI · PY",
        "GO · RUST · SDK",
        "GO · RUST · PY",
        "GO · RUST · PY",
        "RUST · GO · PY",
    ]
    rows = []
    for i, name in enumerate(names):
        x = 20 + (i % 2) * 414
        y = 48 + (i // 2) * 180
        color = GREEN if i % 2 == 0 else CYAN
        rows.append(
            f'<rect x="{x}" y="{y}" width="400" height="164" rx="10" fill="{PANEL}" stroke="{GRID}"/>'
            f'<rect x="{x}" y="{y}" width="4" height="164" rx="2" fill="{color}"/>'
            f'<text x="{x + 20}" y="{y + 36}" font-size="19" font-weight="700" fill="{TEXT}">{name}</text>'
            f'<text x="{x + 20}" y="{y + 62}" font-size="12" fill="{MUTED}">{descs[i]}</text>'
            f'<text x="{x + 20}" y="{y + 98}" font-size="10" fill="{color}" letter-spacing="1">{tags[i]}</text>'
            f'<text x="{x + 20}" y="{y + 136}" font-size="10" fill="{MUTED}">COMMITS: {counts.get(name, 0)}</text>'
            f'<text x="{x + 378}" y="{y + 136}" text-anchor="end" font-size="10" fill="{GREEN}">OPEN <tspan class="k">→</tspan></text>'
            f'<rect x="{x}" y="{y}" width="400" height="2" fill="{color}" opacity=".0" class="f"/>'
        )
    inner = heading("[ PROJECTS ]", GREEN) + "".join(rows)
    save("projects.svg", shell(w, h, inner, MONO))


if __name__ == "__main__":
    print("assets:")
    header()
    typing()
    about()
    about_narrow()
    stack()
    stats()
    languages()
    projects()
    footer()
