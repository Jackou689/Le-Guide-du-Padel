#!/usr/bin/env python3
"""Illustrations vectorielles du Guide du Padel — un seul style : fond bleu nuit, lignes de piste en filigrane,
pictogramme central blanc/bleu clair, accent vert (balle, trajectoires), signature « swoosh » vert en bas à gauche.
Sorties : Tools/REFONTE-2026/illustrations-src/*.svg + images/ill-*.webp (1200 px et 640 px).
Usage : python3 Tools/make_illustrations.py"""
import os, math
from playwright.sync_api import sync_playwright
from PIL import Image
import io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "Tools/REFONTE-2026/illustrations-src"); os.makedirs(SRC, exist_ok=True)
NAVY, DEEP, BLUE, SKY, LIME, MIST, WHITE = "#0B2A45", "#08213A", "#0E5FD8", "#8EC2FF", "#A7E11D", "#F1F5F9", "#FFFFFF"

DEFS = f"""<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B2A45"/><stop offset="1" stop-color="#0E4A86"/></linearGradient>
<radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#2F8BFF" stop-opacity=".35"/><stop offset="1" stop-color="#2F8BFF" stop-opacity="0"/></radialGradient>
<radialGradient id="ballg" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#E6FF8A"/><stop offset=".55" stop-color="#A7E11D"/><stop offset="1" stop-color="#7DB10F"/></radialGradient>
<filter id="sh" x="-20%" y="-20%" width="150%" height="150%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#021120" flood-opacity=".45"/></filter>
<pattern id="holes" width="26" height="26" patternUnits="userSpaceOnUse"><circle cx="13" cy="13" r="5.2" fill="#0B2A45" opacity=".55"/></pattern>
</defs>"""

def court_lines(x, y, w, h, rot=0, op=.12, sw=5, glass=True):
    """Piste vue de dessus (20 x 10 m) : bords, filet, lignes de service."""
    nx = x + w / 2; s1 = nx - w * .3475; s2 = nx + w * .3475
    g = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="none" stroke="{SKY}" stroke-width="{sw*2.2}" opacity="{op*.9}"/>' if glass else ""
    lines = (f'<g fill="none" stroke="{WHITE}" stroke-width="{sw}" stroke-linecap="round" opacity="{op}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>'
             f'<line x1="{nx}" y1="{y}" x2="{nx}" y2="{y+h}" stroke-dasharray="14 12"/><line x1="{s1}" y1="{y}" x2="{s1}" y2="{y+h}"/>'
             f'<line x1="{s2}" y1="{y}" x2="{s2}" y2="{y+h}"/><line x1="{s1}" y1="{y+h/2}" x2="{s2}" y2="{y+h/2}"/></g>')
    return f'<g transform="rotate({rot} {nx} {y+h/2})">{g}{lines}</g>'

def ball(x, y, r=40, rot=-25):
    return (f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#sh)"><circle r="{r}" fill="url(#ballg)"/>'
            f'<clipPath id="bc{int(x)}{int(y)}"><circle r="{r}"/></clipPath><g clip-path="url(#bc{int(x)}{int(y)})" fill="none" stroke="{WHITE}" stroke-width="{max(2.5, r*.09)}" opacity=".95">'
            f'<path d="M{-r*1.2},{-r*.25} C{-r*.4},{r*.35} {r*.4},{r*.35} {r*1.2},{-r*.25}"/><path d="M{-r*1.2},{r*.55} C{-r*.4},{-r*.1} {r*.4},{-r*.1} {r*1.2},{r*.55}" opacity="0"/></g></g>')

FACES = {
    "ronde": "M0,-120 A112,120 0 1 1 0,120 A112,120 0 1 1 0,-120 Z",
    "goutte": "M0,-128 C76,-128 108,-44 94,14 C80,70 42,106 0,110 C-42,106 -80,70 -94,14 C-108,-44 -76,-128 0,-128 Z",
    "diamant": "M0,-130 C74,-130 118,-40 84,24 L28,108 C12,126 -12,126 -28,108 L-84,24 C-118,-40 -74,-130 0,-130 Z",
}
_rid = [0]
def racket(shape, x, y, s=1.0, rot=0, face="#EAF2FB", rim=BLUE, holes=True, handle=True):
    _rid[0] += 1; cid = f"rk{_rid[0]}"; d = FACES[shape]
    hy = {"ronde": 120, "goutte": 108, "diamant": 112}[shape]
    h = (f'<rect x="-17" y="{hy-6}" width="34" height="96" rx="9" fill="{NAVY}" stroke="{SKY}" stroke-width="4"/>'
         f'<g stroke="{SKY}" stroke-width="3" opacity=".7"><line x1="-17" y1="{hy+22}" x2="17" y2="{hy+14}"/><line x1="-17" y1="{hy+42}" x2="17" y2="{hy+34}"/><line x1="-17" y1="{hy+62}" x2="17" y2="{hy+54}"/></g>') if handle else ""
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" filter="url(#sh)">{h}<path d="{d}" fill="{face}" stroke="{rim}" stroke-width="16" stroke-linejoin="round"/>'
            f'<clipPath id="{cid}"><path d="{d}"/></clipPath>' + (f'<rect x="-130" y="-140" width="260" height="270" fill="url(#holes)" clip-path="url(#{cid})"/>' if holes else '') +
            f'<path d="M-40,-96 C-62,-70 -70,-30 -64,10" fill="none" stroke="{WHITE}" stroke-width="7" stroke-linecap="round" opacity=".7"/></g>')

def player(x, y, n="", r=26, c=WHITE):
    t = f'<text x="{x}" y="{y+7}" text-anchor="middle" font-family="system-ui,Arial" font-weight="800" font-size="22" fill="{NAVY}">{n}</text>' if n else ""
    return f'<g filter="url(#sh)"><circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="{BLUE}" stroke-width="6"/>{t}</g>'

def arc(d, color=LIME, w=9, dash="", op=1):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" {"stroke-dasharray=%r" % dash if dash else ""} opacity="{op}"/>'

def arrow_head(x, y, ang, color=LIME, s=16):
    return f'<polygon points="0,0 {-s*1.5},{-s*.8} {-s*1.5},{s*.8}" fill="{color}" transform="translate({x} {y}) rotate({ang})"/>'

def frame(inner, w=1200, h=750, rot=-8, court=(-120, 80, 1000, 520), brand=True):
    cx, cy, cw, ch = court
    sw = (f'<g transform="translate(60 {h-74}) skewX(-28)"><rect width="190" height="14" rx="3" fill="{LIME}"/><rect x="40" y="26" width="110" height="8" rx="3" fill="{LIME}" opacity=".55"/></g>' if brand else "")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{DEFS}<rect width="{w}" height="{h}" fill="url(#bg)"/>'
            f'<ellipse cx="{w*.52}" cy="{h*.5}" rx="{w*.38}" ry="{h*.42}" fill="url(#glow)"/>{court_lines(cx, cy, cw, ch, rot)}{inner}{sw}</svg>')

# ------------------------------------------------------------------ illustrations d'accueil
def ill_raquette():
    return frame(racket("goutte", 600, 330, 1.25, -14) + racket("ronde", 205, 500, .5, -22, face="#CFE4FF", rim="#2F8BFF") + racket("diamant", 995, 500, .5, 20, face="#CFE4FF", rim="#2F8BFF") + ball(820, 590, 38), rot=-6)

def ill_regles():
    # piste vue de dessus, service en diagonale, trajectoire
    x, y, w, h = 150, 150, 900, 450
    nx = x + w / 2
    inner = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{BLUE}" opacity=".55"/>' + court_lines(x, y, w, h, 0, op=.9, sw=6) +
             f'<g fill="{LIME}" opacity=".22"><rect x="{nx}" y="{y+h/2}" width="{w*.3475}" height="{h/2}"/></g>' +
             arc(f"M{x+120},{y+h-70} C{x+380},{y+h*.2} {nx-80},{y+h*.2} {nx+210},{y+h*.78}", LIME, 8, "2 18") + arrow_head(nx + 210, y + h * .78, 62) +
             player(x + 90, y + h - 70, "", 24) + ball(x + 150, y + h - 118, 20))
    return frame(inner, rot=0, court=(-300, 0, 10, 10))

def ill_chaussures():
    shoe = (f'<g transform="translate(230 170) scale(1.05)" filter="url(#sh)">'
            f'<path d="M40,290 C28,210 46,128 96,96 L186,68 C232,56 266,68 296,98 L330,124 C384,150 452,146 504,170 C600,204 706,230 722,272 C726,286 718,292 704,292 L40,292 Z" fill="#EAF2FB"/>'
            f'<path d="M40,290 C28,210 46,128 96,96 L150,80 C176,150 176,230 170,292 Z" fill="{SKY}" opacity=".55"/>'
            f'<path d="M96,96 L186,68 C232,56 266,68 296,98 L250,112 C220,92 170,96 150,110 Z" fill="{BLUE}"/>'
            f'<g stroke="{BLUE}" stroke-width="9" stroke-linecap="round"><line x1="330" y1="134" x2="352" y2="104"/><line x1="382" y1="150" x2="404" y2="120"/><line x1="434" y1="156" x2="456" y2="128"/></g>'
            f'<path d="M330,300 C420,236 540,226 700,250" fill="none" stroke="{BLUE}" stroke-width="12" stroke-linecap="round" opacity=".0"/>'
            f'<path d="M30,292 L732,292 L732,326 C732,350 714,360 692,360 L70,360 C46,360 30,350 30,326 Z" fill="{LIME}"/>'
            f'<g stroke="{NAVY}" stroke-width="7" stroke-linecap="round" opacity=".55">' + "".join(f'<line x1="{78+i*38}" y1="322" x2="{90+i*38}" y2="344"/>' for i in range(16)) + '</g></g>')
    return frame(shoe + ball(960, 560, 36), rot=-4)

def ill_techniques():
    inner = (f'<g opacity=".95"><rect x="905" y="120" width="26" height="470" rx="6" fill="{SKY}" opacity=".35"/><rect x="905" y="120" width="26" height="470" rx="6" fill="none" stroke="{WHITE}" stroke-width="4" opacity=".6"/></g>'
             f'<line x1="150" y1="590" x2="1050" y2="590" stroke="{WHITE}" stroke-width="6" opacity=".55" stroke-linecap="round"/>'
             f'<g><line x1="570" y1="400" x2="570" y2="590" stroke="{WHITE}" stroke-width="8" opacity=".75"/><line x1="570" y1="400" x2="570" y2="590" stroke="{WHITE}" stroke-width="30" stroke-dasharray="4 8" opacity=".25"/><rect x="560" y="392" width="20" height="10" rx="4" fill="{WHITE}"/></g>' +
             arc("M230,470 C320,160 640,120 880,330", LIME, 10) + arrow_head(880, 330, 55) +
             arc("M230,470 C400,330 650,330 870,500", WHITE, 8, "3 16") + arrow_head(870, 500, 40, WHITE, 14) +
             arc("M230,470 C400,520 600,500 810,545", SKY, 8, "3 16") +
             racket("diamant", 190, 470, .42, -50, face="#EAF2FB") + ball(880, 330, 30))
    return frame(inner, rot=-3)

def ill_tactique():
    x, y, w, h = 200, 120, 800, 540
    nx = x + w / 2
    inner = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{BLUE}" opacity=".45"/>' + court_lines(x, y, w, h, 0, op=.85, sw=6) +
             f'<ellipse cx="{nx-190}" cy="{y+h*.3}" rx="105" ry="75" fill="{LIME}" opacity=".28"/><ellipse cx="{nx-190}" cy="{y+h*.7}" rx="105" ry="75" fill="{LIME}" opacity=".28"/>' +
             arc(f"M{nx-190},{y+h*.3+10} L{nx-190},{y+h*.7-10}", LIME, 6, "2 14") + arrow_head(nx - 190, y + h * .7 - 12, 90) + arrow_head(nx - 190, y + h * .3 + 12, -90) +
             player(nx - 190, y + h * .3, "1") + player(nx - 190, y + h * .7, "2") +
             player(nx + 230, y + h * .3, "", 24, SKY) + player(nx + 230, y + h * .7, "", 24, SKY) + ball(nx + 20, y + h * .5, 22))
    return frame(inner, rot=0, court=(-400, 0, 10, 10))

def ill_balles():
    inner = ball(470, 380, 150, -20) + ball(760, 300, 100, 25) + ball(700, 520, 70, 60) + arc("M180,590 C260,330 330,330 400,590", WHITE, 7, "2 16", .6) + arc("M880,540 C920,420 950,420 990,540", WHITE, 7, "2 16", .5)
    return frame(inner, rot=-10)

def ill_echauffement():
    cx, cy, r = 600, 365, 205
    ticks = "".join(f'<line x1="{cx+(r-4)*math.sin(math.radians(a))}" y1="{cy-(r-4)*math.cos(math.radians(a))}" x2="{cx+(r-24)*math.sin(math.radians(a))}" y2="{cy-(r-24)*math.cos(math.radians(a))}" stroke="{WHITE}" stroke-width="7" stroke-linecap="round" opacity=".8"/>' for a in range(0, 360, 30))
    end = (cx + r * math.sin(math.radians(240)), cy - r * math.cos(math.radians(240)))
    inner = (f'<g filter="url(#sh)"><circle cx="{cx}" cy="{cy}" r="{r+34}" fill="{NAVY}" stroke="{SKY}" stroke-width="12"/><rect x="{cx-26}" y="{cy-r-80}" width="52" height="30" rx="8" fill="{SKY}"/></g>'
             f'<path d="M{cx},{cy-r} A{r},{r} 0 1 1 {end[0]},{end[1]}" fill="none" stroke="{LIME}" stroke-width="26" stroke-linecap="round"/>' + ticks +
             f'<line x1="{cx}" y1="{cy}" x2="{cx+130*math.sin(math.radians(240))}" y2="{cy-130*math.cos(math.radians(240))}" stroke="{WHITE}" stroke-width="12" stroke-linecap="round"/><circle cx="{cx}" cy="{cy}" r="16" fill="{WHITE}"/>' +
             arc("M180,520 C230,430 290,430 340,520 S450,610 500,520", SKY, 8, "2 16", .8) + arc("M700,520 C750,430 810,430 860,520 S970,610 1020,520", SKY, 8, "2 16", .8) + ball(1010, 250, 34))
    return frame(inner, rot=-6)

def ill_tendinite():
    # bras plié (épaule -> coude -> main) avec articulation du coude mise en évidence
    inner = (f'<g filter="url(#sh)" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M330,540 L560,330 L820,420" stroke="{MIST}" stroke-width="64"/><path d="M330,540 L560,330 L820,420" stroke="{SKY}" stroke-width="64" opacity=".35"/></g>'
             f'<circle cx="560" cy="330" r="92" fill="{LIME}" opacity=".16"/><circle cx="560" cy="330" r="66" fill="{LIME}" opacity=".28"/><circle cx="560" cy="330" r="40" fill="{LIME}" stroke="{WHITE}" stroke-width="8"/>' +
             racket("goutte", 905, 470, .55, 100, face="#CFE4FF", rim=BLUE) +
             f'<g fill="none" stroke="{LIME}" stroke-width="8" stroke-linecap="round"><path d="M640,230 q40,-30 70,-6" opacity=".9"/><path d="M660,196 q56,-44 100,-8" opacity=".6"/></g>')
    return frame(inner, rot=-5)

def ill_hero():
    # piste en perspective, filet, vitre de fond, raquette et balle au premier plan
    inner = (f'<polygon points="140,430 1060,430 1180,740 20,740" fill="{BLUE}" opacity=".75"/>'
             f'<g stroke="{WHITE}" stroke-width="6" fill="none" opacity=".85"><line x1="140" y1="430" x2="20" y2="740"/><line x1="1060" y1="430" x2="1180" y2="740"/><line x1="600" y1="430" x2="600" y2="740" stroke-dasharray="14 12"/><line x1="360" y1="430" x2="270" y2="740"/><line x1="840" y1="430" x2="930" y2="740"/><line x1="300" y1="560" x2="900" y2="560"/></g>'
             f'<rect x="140" y="170" width="920" height="260" rx="10" fill="{SKY}" opacity=".18"/><rect x="140" y="170" width="920" height="260" rx="10" fill="none" stroke="{WHITE}" stroke-width="5" opacity=".5"/>'
             f'<g stroke="{WHITE}" stroke-width="3" opacity=".35"><line x1="450" y1="170" x2="450" y2="430"/><line x1="750" y1="170" x2="750" y2="430"/></g>'
             f'<g><rect x="100" y="330" width="1000" height="10" fill="{WHITE}" opacity=".9"/><g stroke="{WHITE}" stroke-width="2" opacity=".35">' + "".join(f'<line x1="{100+i*25}" y1="340" x2="{100+i*25}" y2="440"/>' for i in range(41)) + '</g></g>' +
             f'<path d="M780,95 L1040,60" stroke="{SKY}" stroke-width="3" opacity="0"/>' +
             racket("diamant", 360, 520, 1.15, 14) + ball(560, 690, 44))
    return frame(inner, w=1200, h=750, rot=0, court=(-500, 0, 10, 10))

# ------------------------------------------------------------------ illustrations d'article (760 x 460, même style)
def frame_small(inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 460" width="1200" height="726">{DEFS}<rect width="760" height="460" fill="url(#bg)"/>'
            f'<ellipse cx="400" cy="230" rx="300" ry="190" fill="url(#glow)"/>{inner}'
            f'<g transform="translate(34 424) skewX(-28)"><rect width="120" height="9" rx="2" fill="{LIME}"/><rect x="26" y="16" width="70" height="5" rx="2" fill="{LIME}" opacity=".55"/></g></svg>')

def lab(x, y, t, anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="system-ui,Arial" font-weight="700" font-size="17" fill="{WHITE}" opacity=".92">{t}</text>'

def ill_lob():
    inner = (f'<rect x="30" y="360" width="700" height="8" rx="4" fill="{WHITE}" opacity=".55"/><rect x="706" y="70" width="14" height="298" rx="5" fill="{SKY}" opacity=".35"/>'
             f'<line x1="380" y1="250" x2="380" y2="360" stroke="{WHITE}" stroke-width="5" opacity=".8"/><line x1="380" y1="250" x2="380" y2="360" stroke="{WHITE}" stroke-width="22" stroke-dasharray="3 6" opacity=".22"/>' +
             player(560, 322, "", 24, SKY) + player(120, 322, "", 24) +
             arc("M148,300 C190,40 560,10 640,330", LIME, 8) + arrow_head(640, 330, 78) +
             arc("M148,300 C250,250 440,250 540,300", WHITE, 5, "2 12", .6) +
             f'<circle cx="400" cy="62" r="7" fill="{WHITE}"/>' + lab(400, 44, "Trajectoire haute") + lab(380, 392, "Filet") + lab(560, 392, "Adversaire au filet", "middle") + lab(120, 392, "Vous") + ball(148, 296, 16))
    return frame_small(inner)

def ill_vitre():
    # vue de dessus : la balle rebondit sur la vitre du fond puis revient vers le joueur placé en retrait
    inner = (f'<rect x="60" y="60" width="640" height="320" rx="8" fill="{BLUE}" opacity=".45"/>' + court_lines(60, 60, 640, 320, 0, op=.85, sw=5, glass=False) +
             f'<rect x="660" y="60" width="26" height="320" rx="6" fill="{SKY}" opacity=".55"/><rect x="660" y="60" width="26" height="320" rx="6" fill="none" stroke="{WHITE}" stroke-width="3"/>' +
             arc("M140,300 C320,260 520,190 662,150", LIME, 7) + arc("M662,150 C560,120 400,170 250,260", LIME, 7, "2 12") + arrow_head(250, 260, 150) + arrow_head(662, 150, -20) +
             f'<circle cx="662" cy="150" r="14" fill="none" stroke="{WHITE}" stroke-width="5"/>' + player(140, 300, "", 22) + player(240, 262, "", 22, SKY) +
             ball(140, 262, 14) + lab(670, 410, "Vitre du fond", "middle") + lab(140, 340, "Frappe") + lab(262, 208, "Reprise"))
    return frame_small(inner)

HOME = {"ill-raquette": ill_raquette, "ill-regles": ill_regles, "ill-chaussures": ill_chaussures, "ill-techniques": ill_techniques,
        "ill-tactique": ill_tactique, "ill-balles": ill_balles, "ill-echauffement": ill_echauffement, "ill-tendinite": ill_tendinite, "ill-hero": ill_hero}
ART = {"ill-lob": ill_lob, "ill-vitre-fond": ill_vitre}

def render():
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, fn in {**HOME, **ART}.items():
            svg = fn(); open(f"{SRC}/{name}.svg", "w", encoding="utf-8").write(svg)
            is_art = name in ART; W, H = (1200, 726) if is_art else (1200, 750)
            pg = b.new_page(viewport={"width": W, "height": H}); pg.set_content('<body style="margin:0">' + svg.replace('width="1200" height="%d"' % (726 if is_art else 750), 'width="1200" height="%d"' % H) + '</body>')
            png = pg.screenshot(clip={"x": 0, "y": 0, "width": W, "height": H}); pg.close()
            im = Image.open(io.BytesIO(png)).convert("RGB")
            for w in (1200, 640):
                o = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
                o.save(f"{ROOT}/images/{name}-{w}w.webp" if w != 1200 else f"{ROOT}/images/{name}.webp", "WEBP", quality=84, method=6)
            print(name, "ok")
        b.close()

if __name__ == "__main__":
    render()
