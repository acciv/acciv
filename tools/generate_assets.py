"""Генератор анимированных SVG для профиля acciv.

Без JS и внешних файлов: только CSS-анимации и SMIL внутри SVG.
Запуск: python3 tools/generate_assets.py
"""

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets"
OUT.mkdir(parents=True, exist_ok=True)

BG = "#0b0f17"
PANEL = "#0d1420"
GRID = "#16202e"
GREEN = "#00ff9c"
CYAN = "#00e5ff"
RED = "#ff0055"
AMBER = "#ffd166"
TEXT = "#e9edf2"
MUTED = "#6e7681"

FONT = "'JetBrains Mono','Fira Code',Consolas,'Courier New',monospace"

HEAD = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
    'viewBox="0 0 {w} {h}" font-family="{font}" xml:space="preserve">'
)

STYLE = """<style>
.blink{animation:b 1s steps(1) infinite}@keyframes b{50%{opacity:0}}
.flick{animation:f 4s infinite}@keyframes f{0%,97%,100%{opacity:1}98%{opacity:.55}99%{opacity:.85}}
.scan{animation:s 5s linear infinite}@keyframes s{0%{transform:translateY(-20px)}100%{transform:translateY(340px)}}
.sweep{animation:sw 6s linear infinite}@keyframes sw{0%{transform:translateX(-120px)}100%{transform:translateX(940px)}}
.glitch{animation:g 3.5s infinite}@keyframes g{0%,92%,100%{transform:translate(0);opacity:.35}93%{transform:translate(-3px,1px)}95%{transform:translate(3px,-1px)}97%{transform:translate(-2px,0)}}
.pulse{animation:p 2s ease-in-out infinite}@keyframes p{50%{opacity:.35}}
.spin{animation:sp 28s linear infinite;transform-origin:450px 280px}@keyframes sp{to{transform:rotate(360deg)}}
.spin2{animation:sp 40s linear infinite reverse;transform-origin:450px 280px}@keyframes sp2{to{transform:rotate(360deg)}}
.dash{stroke-dasharray:6 8;animation:d 3s linear infinite}@keyframes d{to{stroke-dashoffset:-28}}
.typing{overflow:hidden;white-space:nowrap;animation:t 2.2s steps(38) infinite}@keyframes t{0%{width:0}70%,100%{width:100%}}
</style>"""


def save(name: str, body: str) -> None:
    (OUT / name).write_text(body, encoding="utf-8")
    print(f"  + {name}")


def intro() -> None:
    w, h = 900, 320
    rain = []
    for i in range(26):
        x = 24 + i * 26
        chars = "".join(
            f'<tspan x="{x}" dy="15">{((i * 37 + j * 91) % 256):02X}</tspan>'
            for j in range(24)
        )
        dur = 4 + (i % 7)
        delay = -(i % 9)
        rain.append(
            f'<text y="-360" font-size="10" fill="{GREEN}" opacity="0.10" '
            f'style="animation:rain {dur}s linear {delay}s infinite">'
            f"{chars}</text>"
        )
    rain_style = (
        "@keyframes rain{to{transform:translateY(1000px)}}"
    )
    body = HEAD.format(w=w, h=h, font=FONT) + f"""<defs><style>{rain_style}</style>
<radialGradient id="glow"><stop offset="0" stop-color="{CYAN}" stop-opacity=".35"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{GREEN}"/><stop offset="1" stop-color="{CYAN}"/></linearGradient>
<filter id="blur"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<clipPath id="frame"><rect width="900" height="320" rx="12"/></clipPath></defs>
<g clip-path="url(#frame)">
<rect width="900" height="320" fill="{BG}"/>
<g opacity=".25">{''.join(rain)}</g>
<g stroke="{GRID}" stroke-width="1" opacity=".7">{''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="320"/>' for x in range(0, 901, 50))}{''.join(f'<line x1="0" y1="{y}" x2="900" y2="{y}"/>' for y in range(0, 321, 50))}</g>
<circle cx="160" cy="160" r="130" fill="url(#glow)" class="pulse"/>
<g stroke="url(#edge)" stroke-width="4" filter="url(#blur)" fill="{PANEL}">
<polygon points="160,36 268,98 268,222 160,284 52,222 52,98" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100">
<animate attributeName="stroke-dashoffset" to="0" dur="1.4s" fill="freeze"/></polygon></g>
<polygon points="160,50 255,105 255,215 160,270 65,215 65,105" fill="none" stroke="{GREEN}" stroke-opacity=".3" stroke-dasharray="5 7" class="dash"/>
<g filter="url(#blur)" fill="none" stroke="{CYAN}" stroke-width="7" stroke-linecap="round">
<circle cx="160" cy="140" r="26"/><path d="M160 166v34m-16 0h32m-12 0v16h-8v-16"/></g>
<text x="160" y="250" text-anchor="middle" font-size="12" letter-spacing="5" fill="{GREEN}">ACCIV</text>
<text x="160" y="22" text-anchor="middle" font-size="10" letter-spacing="2" fill="{RED}">SESSION 0x4143434956 · TRACE ACTIVE</text>
<g transform="translate(340 0)">
<text x="0" y="118" font-size="76" font-weight="800" letter-spacing="14" fill="{TEXT}">acciv</text>
<text x="3" y="115" font-size="76" font-weight="800" letter-spacing="14" fill="{CYAN}" class="glitch">acciv</text>
<text x="0" y="156" font-size="15" letter-spacing="3" fill="{GREEN}">API KEYS · AUTH · SECURITY</text>
<text x="0" y="186" font-size="12" letter-spacing="2" fill="{MUTED}">RUST · GO · PYTHON · C++ · JAVA · PHP</text>
<text x="0" y="226" font-size="13" letter-spacing="3" fill="{CYAN}">ACCESS GRANTED <tspan class="blink">█</tspan></text>
</g>
<rect x=".5" y=".5" width="899" height="319" rx="12" fill="none" stroke="{GRID}" stroke-width="1"/>
<rect width="900" height="320" fill="url(#glow)" opacity=".05" class="flick"/>
</g></svg>"""
    save("intro.svg", body)


def terminal() -> None:
    w, h = 900, 430
    lines = [
        ("acciv@keygate:~$ whoami", TEXT, 0.4),
        ("acciv — API keys, auth, security", GREEN, 1.1),
        ("acciv@keygate:~$ ls ~/projects", TEXT, 1.9),
        ("keylens/ apixray/ keygate/ apishadow/ registry/ apifuzz/", CYAN, 2.6),
        ("acciv@keygate:~$ keygate status", TEXT, 3.4),
        ("policy: OK   vault: SEALED   audit: ACTIVE", GREEN, 4.1),
        ("acciv@keygate:~$ apixray inspect token", TEXT, 4.9),
        ("provider: GitHub · segments: 2 · risk: 60", AMBER, 5.6),
        ("acciv@keygate:~$ _", TEXT, 6.4),
    ]
    text_nodes = []
    for i, (line, color, begin) in enumerate(lines):
        text_nodes.append(
            f'<text x="26" y="{54 + i * 38}" font-size="15" fill="{color}" '
            f'opacity="0"><set attributeName="opacity" to="1" begin="{begin}s" fill="freeze"/>'
            f"{line}</text>"
        )
    body = HEAD.format(w=w, h=h, font=FONT) + f"""<defs><style>.cursor{{animation:b 1s steps(1) infinite}}@keyframes b{{50%{{opacity:0}}}}
.scanline{{animation:sl 7s linear infinite}}@keyframes sl{{0%{{transform:translateY(-30px)}}100%{{transform:translateY(430px)}}}}</style></defs>
<rect width="900" height="430" rx="12" fill="{PANEL}" stroke="{GRID}"/>
<rect width="900" height="38" rx="12" fill="{BG}"/><rect y="30" width="900" height="8" fill="{BG}"/>
<circle cx="22" cy="19" r="5" fill="{RED}"/><circle cx="42" cy="19" r="5" fill="{AMBER}"/><circle cx="62" cy="19" r="5" fill="{GREEN}"/>
<text x="450" y="23" text-anchor="middle" font-size="11" letter-spacing="2" fill="{MUTED}">acciv@keygate — session</text>
{''.join(text_nodes)}
<rect x="0" y="0" width="900" height="2" fill="{CYAN}" opacity=".35" class="scanline"/>
<rect x=".5" y=".5" width="899" height="429" rx="12" fill="none" stroke="{GRID}"/></svg>"""
    save("terminal.svg", body)


def heartbeat() -> None:
    w, h = 900, 190
    grid = "".join(
        f'<line x1="{x}" y1="0" x2="{x}" y2="190"/>'
        for x in range(0, 901, 45)
    ) + "".join(f'<line x1="0" y1="{y}" x2="900" y2="{y}"/>' for y in range(0, 191, 45))
    body = HEAD.format(w=w, h=h, font=FONT) + f"""<defs><style>.ecg{{stroke-dasharray:1400;stroke-dashoffset:1400;animation:draw 3.5s linear infinite}}@keyframes draw{{to{{stroke-dashoffset:0}}}}
.beat{{animation:bp 2.2s ease-in-out infinite}}@keyframes bp{{50%{{transform:scale(1.04);opacity:.8}}}}</style>
<filter id="g"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
<rect width="900" height="190" rx="10" fill="{PANEL}" stroke="{GRID}"/>
<g stroke="{GRID}" opacity=".65">{grid}</g>
<text x="20" y="28" font-size="11" letter-spacing="3" fill="{MUTED}">COMMIT SIGNAL · LAST 60 DAYS</text>
<g filter="url(#g)" class="beat">
<path d="M20 120 H140 l18 0 12 -12 14 68 18 -108 16 52 H300 l16 0 12 -16 12 54 16 -82 14 44 H470 l16 0 14 -18 14 62 16 -94 16 50 H640 l18 0 12 -14 14 60 16 -88 16 42 H880"
 fill="none" stroke="{GREEN}" stroke-width="2.5" class="ecg"/></g>
<circle cx="880" cy="120" r="5" fill="{GREEN}" class="blink"/>
<text x="20" y="172" font-size="11" fill="{CYAN}">SIGNAL: LIVE</text>
<text x="880" y="172" text-anchor="end" font-size="11" fill="{MUTED}">REFRESHED DAILY</text></svg>"""
    save("heartbeat.svg", body)


def lab() -> None:
    w, h = 900, 430
    body = HEAD.format(w=w, h=h, font=FONT) + f"""<defs><style>.beam{{animation:bm 4s linear infinite}}@keyframes bm{{0%{{transform:translateX(0)}}100%{{transform:translateX(620px)}}}}
.jit{{animation:j .18s steps(2) infinite}}@keyframes j{{50%{{transform:translate(1px,0)}}}}
.typing{{animation:t 3s steps(24) infinite}}@keyframes t{{0%{{width:0}}60%,100%{{width:100%}}}}</style>
<linearGradient id="beam" x1="0" x2="1"><stop stop-color="{CYAN}" stop-opacity="0"/><stop offset=".5" stop-color="{CYAN}" stop-opacity=".5"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></linearGradient></defs>
<rect width="900" height="430" rx="12" fill="{PANEL}" stroke="{GRID}"/>
<text x="24" y="34" font-size="12" letter-spacing="4" fill="{RED}">[ KEY DISSECTION ]</text>
<text x="24" y="62" font-size="19" fill="{TEXT}">ghp_<tspan fill="{CYAN}">••••••••••••</tspan><tspan fill="{RED}">••••</tspan></text>
<line x1="24" y1="80" x2="876" y2="80" stroke="{GRID}"/>
<g font-size="12">
<rect x="24" y="104" width="170" height="92" rx="6" fill="{BG}" stroke="{GREEN}"/>
<text x="40" y="130" fill="{MUTED}">SEGMENT 00</text><text x="40" y="158" fill="{GREEN}" font-size="17">ghp</text><text x="40" y="180" fill="{MUTED}">prefix</text>
<rect x="212" y="104" width="360" height="92" rx="6" fill="{BG}" stroke="{CYAN}"/>
<text x="228" y="130" fill="{MUTED}">SEGMENT 01</text><text x="228" y="158" fill="{CYAN}" font-size="17">••••••••••••••••</text><text x="228" y="180" fill="{MUTED}">payload · 36 chars</text>
<rect x="590" y="104" width="286" height="92" rx="6" fill="{BG}" stroke="{RED}"/>
<text x="606" y="130" fill="{MUTED}">SEGMENT 02</text><text x="606" y="158" fill="{RED}" font-size="17">TEST</text><text x="606" y="180" fill="{MUTED}">fake marker</text>
</g>
<rect x="24" y="222" width="620" height="3" fill="url(#beam)" class="beam"/>
<g font-size="13">
<text x="24" y="274" fill="{MUTED}">ENTROPY</text><text x="180" y="274" fill="{TEXT}">4.496 bits</text>
<text x="24" y="304" fill="{MUTED}">CHARSET</text><text x="180" y="304" fill="{TEXT}">lower · upper · digit</text>
<text x="24" y="334" fill="{MUTED}">JWT DECODE</text><text x="180" y="334" fill="{TEXT}">alg: HS256 · signature NOT verified</text>
<text x="24" y="364" fill="{MUTED}">VERDICT</text><text x="180" y="364" fill="{AMBER}">test material — rotate if ever exposed</text>
</g>
<rect x="640" y="250" width="236" height="140" rx="8" fill="{BG}" stroke="{GREEN}" class="jit"/>
<text x="758" y="290" text-anchor="middle" font-size="11" fill="{MUTED}">RISK SCORE</text>
<text x="758" y="340" text-anchor="middle" font-size="46" font-weight="700" fill="{GREEN}">60</text>
<text x="758" y="368" text-anchor="middle" font-size="11" fill="{MUTED}">/ 100</text>
<text x="24" y="410" font-size="11" fill="{CYAN}">STRUCTURE ONLY · NO BRUTE FORCE · NO BYPASS</text></svg>"""
    save("lab.svg", body)


def orbit() -> None:
    w, h = 900, 560
    inner = [
        ("API KEYS", 450, 90), ("JWT", 640, 155), ("RUST", 770, 280),
        ("GO", 690, 430), ("PYTHON", 450, 500), ("C++", 200, 440),
        ("TELEGRAM", 120, 280), ("PHP", 220, 140),
    ]
    outer = [
        ("REVERSING", 450, 22), ("THREAT MODEL", 790, 100), ("SECURITY", 878, 280),
        ("CI / CD", 780, 480), ("DOCKER", 450, 548), ("AUDIT", 110, 480),
        ("LINUX", 22, 280), ("JAVA", 110, 100),
    ]
    def dots(items, color):
        return "".join(
            f'<circle cx="{x}" cy="{y}" r="4" fill="{color}"/>'
            f'<text x="{x}" y="{y - 12}" text-anchor="middle" font-size="11" '
            f'letter-spacing="1.5" fill="{color}">{label}</text>'
            for label, x, y in items
        )
    body = HEAD.format(w=w, h=h, font=FONT) + f"""<defs><style>.spin{{animation:sp 34s linear infinite;transform-origin:450px 280px}}@keyframes sp{{to{{transform:rotate(360deg)}}}}
.spin2{{animation:sp 52s linear infinite reverse;transform-origin:450px 280px}}</style></defs>
<rect width="900" height="560" rx="12" fill="{PANEL}" stroke="{GRID}"/>
<circle cx="450" cy="280" r="180" fill="none" stroke="{GRID}" stroke-dasharray="4 8"/>
<circle cx="450" cy="280" r="250" fill="none" stroke="{GRID}" stroke-dasharray="2 10"/>
<g class="spin">{dots(inner, GREEN)}</g>
<g class="spin2">{dots(outer, CYAN)}</g>
<circle cx="450" cy="280" r="92" fill="{BG}" stroke="{GREEN}" stroke-width="2"/>
<circle cx="450" cy="280" r="104" fill="none" stroke="{RED}" stroke-opacity=".35" stroke-dasharray="5 9" class="spin"/>
<text x="450" y="270" text-anchor="middle" font-size="34" font-weight="700" fill="{TEXT}">acciv</text>
<text x="450" y="300" text-anchor="middle" font-size="11" letter-spacing="2" fill="{GREEN}">KEY SYSTEMS</text>
<text x="450" y="324" text-anchor="middle" font-size="10" fill="{MUTED}">Krasnodar · RU</text>
<text x="24" y="30" font-size="11" letter-spacing="4" fill="{RED}">[ OBSESSIONS ]</text></svg>"""
    save("orbit.svg", body)


CARD_STYLE = """<style>.stamp{animation:st 5s ease-in-out infinite}@keyframes st{0%,100%{opacity:.25}50%{opacity:1}}
.blink{animation:b 1s steps(1) infinite}@keyframes b{50%{opacity:0}}
.scan{animation:sc 4s linear infinite}@keyframes sc{0%{transform:translateX(-80px)}100%{transform:translateX(680px)}}</style>"""


def card(filename, name, tag, description, tags, color, glyph):
    w, h = 600, 230
    tagline = "  ".join(tags)
    body = HEAD.format(w=w, h=h, font=FONT) + f"""<defs>{CARD_STYLE}
<linearGradient id="fade" x1="0" x2="1"><stop stop-color="{color}" stop-opacity="0"/><stop offset=".5" stop-color="{color}" stop-opacity=".45"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></linearGradient></defs>
<rect width="600" height="230" rx="10" fill="{PANEL}" stroke="{GRID}"/>
<rect x="0" y="0" width="6" height="230" fill="{color}"/>
<text x="26" y="40" font-size="11" letter-spacing="2" fill="{color}">CASE · {tag}</text>
<text x="26" y="94" font-size="34" font-weight="700" fill="{TEXT}">{name}</text>
<text x="26" y="126" font-size="13" fill="{MUTED}">{description}</text>
<line x1="26" y1="146" x2="574" y2="146" stroke="{GRID}"/>
<text x="26" y="176" font-size="12" fill="{color}">{tagline}</text>
<text x="26" y="208" font-size="11" fill="{GREEN}">OPEN REPO <tspan class="blink">→</tspan></text>
<g class="stamp" fill="none" stroke="{color}" opacity=".25"><circle cx="520" cy="66" r="42" stroke-width="2"/><circle cx="520" cy="66" r="52" stroke-dasharray="4 7"/></g>
<text x="520" y="80" text-anchor="middle" font-size="38" fill="{color}" class="stamp">{glyph}</text>
<rect x="0" y="0" width="80" height="230" fill="url(#fade)" class="scan"/></svg>"""
    save(filename, body)


def bodycount() -> None:
    w, h = 900, 180
    stats = [
        ("06", "PROJECTS", GREEN),
        ("07", "LANGUAGES", CYAN),
        ("CI", "GREEN", GREEN),
        ("00", "KEYS LEAKED", AMBER),
    ]
    cells = []
    for i, (value, label, color) in enumerate(stats):
        x = 30 + i * 218
        cells.append(
            f'<rect x="{x}" y="30" width="196" height="116" rx="8" fill="{BG}" stroke="{GRID}"/>'
            f'<text x="{x + 98}" y="92" text-anchor="middle" font-size="40" font-weight="700" '
            f'fill="{color}">{value}</text>'
            f'<text x="{x + 98}" y="124" text-anchor="middle" font-size="11" letter-spacing="2" '
            f'fill="{MUTED}">{label}</text>'
        )
    body = HEAD.format(w=w, h=h, font=FONT) + f"""<defs><style>.flick{{animation:f 5s infinite}}@keyframes f{{50%{{opacity:.75}}}}</style></defs>
<rect width="900" height="180" rx="10" fill="{PANEL}" stroke="{GRID}"/>
{''.join(cells)}
<text x="24" y="24" font-size="10" letter-spacing="3" fill="{RED}">[ BODY COUNT ]</text>
<text x="876" y="168" text-anchor="end" font-size="10" fill="{MUTED}" class="flick">NO SECRETS WERE HARMED</text></svg>"""
    save("bodycount.svg", body)


def infection() -> None:
    w, h = 908, 200
    cells = []
    for row in range(7):
        for col in range(53):
            x, y = 22 + col * 17, 34 + row * 20
            v = (row * 53 + col * 17) % 11
            if v < 2:
                color, op = GRID, ".55"
            elif v < 6:
                color, op = RED, ".75"
            elif v < 9:
                color, op = GREEN, ".8"
            else:
                color, op = CYAN, ".7"
            cells.append(f'<rect x="{x}" y="{y}" width="12" height="12" rx="2" fill="{color}" opacity="{op}"/>')
    body = HEAD.format(w=w, h=h, font=FONT) + f"""<defs><style>.sweep{{animation:sw 8s linear infinite}}@keyframes sw{{0%{{transform:translateX(-60px)}}100%{{transform:translateX(920px)}}}}
.clr{{animation:cl 8s linear infinite}}@keyframes cl{{0%,30%{{opacity:0}}45%,80%{{opacity:1}}100%{{opacity:0}}}}</style>
<linearGradient id="swg" x1="0" x2="1"><stop stop-color="{CYAN}" stop-opacity="0"/><stop offset=".5" stop-color="{CYAN}" stop-opacity=".35"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></linearGradient></defs>
<rect width="908" height="200" rx="10" fill="{PANEL}" stroke="{GRID}"/>
<text x="22" y="24" font-size="10" letter-spacing="3" fill="{MUTED}">CONTRIBUTION FIELD · SCAN AND CLEAN</text>
{''.join(cells)}
<rect x="0" y="28" width="70" height="150" fill="url(#swg)" class="sweep"/>
<g class="clr">{''.join(f'<rect x="{22 + col * 17}" y="34" width="12" height="12" rx="2" fill="{GREEN}" opacity=".6"/>' for col in range(53))}</g>
<text x="886" y="192" text-anchor="end" font-size="10" fill="{GREEN}">SIGNAL CLEAN</text></svg>"""
    save("infection.svg", body)


def footer() -> None:
    w, h = 900, 140
    body = HEAD.format(w=w, h=h, font=FONT) + f"""<defs><style>.blink{{animation:b 1s steps(1) infinite}}@keyframes b{{50%{{opacity:0}}}}
.dash{{stroke-dasharray:8 10;animation:d 3s linear infinite}}@keyframes d{{to{{stroke-dashoffset:-36}}}}</style></defs>
<rect width="900" height="140" rx="10" fill="{BG}" stroke="{GRID}"/>
<line x1="40" y1="70" x2="330" y2="70" stroke="{GREEN}" stroke-opacity=".5" class="dash"/>
<line x1="570" y1="70" x2="860" y2="70" stroke="{GREEN}" stroke-opacity=".5" class="dash"/>
<text x="450" y="62" text-anchor="middle" font-size="15" letter-spacing="5" fill="{TEXT}">ACCIV</text>
<text x="450" y="88" text-anchor="middle" font-size="10" letter-spacing="3" fill="{RED}">CONNECTION TERMINATED <tspan class="blink">█</tspan></text>
<text x="450" y="120" text-anchor="middle" font-size="10" fill="{MUTED}">jumpscout@proton.me · Krasnodar</text></svg>"""
    save("footer.svg", body)


if __name__ == "__main__":
    print("assets:")
    intro()
    terminal()
    heartbeat()
    lab()
    orbit()
    card("case-keylens.svg", "keylens", "001", "Находит утекшие ключи в файлах.",
         ["PYTHON", "SCANNER", "CI"], GREEN, "01")
    card("case-apixray.svg", "apixray", "002", "Разбирает структуру ключей и JWT.",
         ["RUST", "C ABI", "PYTHON / C++"], CYAN, "02")
    card("case-keygate.svg", "keygate", "003", "Gateway для ключей с политиками и аудитом.",
         ["GO", "RUST POLICY", "SDK x4"], AMBER, "03")
    card("case-apishadow.svg", "apishadow", "004", "Зеркалит API-трафик и ищет расхождения.",
         ["GO PROXY", "RUST", "PYTHON DIFF"], CYAN, "04")
    card("case-schema-registry.svg", "schema-registry", "005", "Хранит версии API-схем и ловит breaking changes.",
         ["GO API", "RUST CORE", "PYTHON CLI"], GREEN, "05")
    card("case-apifuzz.svg", "apifuzz", "006", "Гоняет API по OpenAPI и ищет расхождения.",
         ["GO RUNNER", "RUST GEN", "PY REPORT"], AMBER, "06")
    bodycount()
    infection()
    footer()
