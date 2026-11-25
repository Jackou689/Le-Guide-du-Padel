#!/usr/bin/env python3
"""Refonte 2026 : applique en-tête, menu, pied de page, signature, articles liés et
correctifs d'images aux pages du lot 10A.17 sans toucher au contenu éditorial.
À lancer depuis la racine du dépôt, sur la base propre du lot 10A.17 :
    git checkout -- '*.html' script.js _headers && python3 Tools/build_refonte_2026.py
"""
import re, os, subprocess, html
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
V = "2026-1"

def rd(p): return open(p, encoding="utf-8").read()
def wr(p, t): open(p, "w", encoding="utf-8").write(t)

# ---------------------------------------------------------------- métadonnées
CAT = {"materiel": ("Matériel", "materiel"), "regles": ("Règles & tactique", "regles"), "sante": ("Santé & blessures", "sante")}
ART = {  # slug: (catégorie, titre court, titre complet, description)
 "raquette-debutant": ("materiel", "Choisir sa première raquette", "Comment choisir sa raquette de padel quand on débute", "Formes, poids et mousse : les critères pour choisir une raquette adaptée à votre niveau et à votre confort."),
 "regles-padel": ("regles", "Les règles du jeu", "Les Règles du Padel et Comment Jouer : Le Guide Complet", "Dimensions du terrain, service à la cuillère, comptage des points et gestion des vitres : tout est expliqué."),
 "chaussures-padel": ("materiel", "Le guide des chaussures", "Chaussures de Padel : Évitez les erreurs de débutant", "Pourquoi les chaussures de running sont moins adaptées ? Semelles et critères de maintien utiles au padel."),
 "techniques-padel": ("regles", "Les coups techniques", "Les Coups Techniques au Padel : Bandeja, Vibora et Chiquita", "Le vocabulaire indispensable pour comprendre et maîtriser les coups spécifiques de ce sport."),
 "tactique-filet": ("regles", "Dominer le filet", "Tactique de double : Comment dominer le filet au padel", "Volées, occupation de l'espace et prise de filet pour prendre l'avantage en match."),
 "balles-padel": ("materiel", "Le guide des balles", "Balles de padel : Comment choisir et quand les changer ?", "Différences avec le tennis, pression interne, durée de vie utile et astuces pour prolonger leur rebond."),
 "echauffement-padel": ("sante", "L'échauffement en 10 minutes", "S'échauffer au Padel : La routine de 10 minutes avant un match", "Réveil articulaire, mouvements progressifs et routine générale pour préparer la séance."),
 "raquette-tendinite": ("sante", "Prévention tendinite", "Tendinite et Padel : Quelle raquette choisir pour son coude ?", "Épicondylite, confort de frappe et critères de choix d'une raquette en cas de sensibilité du coude."),
}
REL = {
 "raquette-debutant": ["chaussures-padel", "balles-padel", "raquette-tendinite"],
 "chaussures-padel": ["raquette-debutant", "balles-padel", "echauffement-padel"],
 "balles-padel": ["raquette-debutant", "chaussures-padel", "regles-padel"],
 "raquette-tendinite": ["echauffement-padel", "raquette-debutant", "chaussures-padel"],
 "echauffement-padel": ["raquette-tendinite", "techniques-padel", "chaussures-padel"],
 "regles-padel": ["techniques-padel", "tactique-filet", "raquette-debutant"],
 "techniques-padel": ["tactique-filet", "regles-padel", "echauffement-padel"],
 "tactique-filet": ["techniques-padel", "regles-padel", "echauffement-padel"],
}

# ---------------------------------------------------------------- images
def fix_images():
    ren = {  # ancien nom -> nouveau nom (contenu réel de l'image). Noms neufs : cache immutable d'un an sur /images/*.
     "technique-position.webp": "padel-position-attente.webp",
     "technique-vibora.webp": "padel-fond-de-court-coup-droit-revers.webp",
     "technique-chiquita.webp": "padel-volee.webp",
     "technique-vitre-fond.webp": "padel-bandeja.webp",
     "technique-double-vitre.webp": "padel-vibora.webp",
     "technique-smash.webp": "padel-smash.webp",
     "technique-transition-filet.webp": "padel-chiquita.webp",
     "technique-fond-court.webp": "padel-double-vitre.webp",
     "technique-bajada.webp": "padel-bajada.webp",
     "technique-volees.webp": "padel-transition-fond-filet.webp",
     "technique-lob.webp": "a-verifier-frappe-aerienne.webp",          # n'illustre pas un lob : retirée de la section 3
     "technique-bandeja.webp": "padel-position-attente-appuis.webp",   # montrait une position d'attente, pas une bandeja
    }
    for a, b in ren.items():
        subprocess.run(["git", "mv", f"images/{a}", f"images/{b}"], check=True)
    t = rd("techniques-padel.html")
    # sections 3 et 9 : on retire la figure dont l'image ne correspond pas au geste (aucune image de remplacement existante)
    for key in ("technique-lob.webp", "technique-position.webp\"/><figcaption>Laissez"):
        pass
    t = re.sub(r'<figure class="technique-specific-visual editorial-section-content"><img alt="Trajectoire haute du lob"[^>]*/><figcaption>[^<]*</figcaption></figure>', "", t)
    t = re.sub(r'<figure class="technique-specific-visual editorial-section-content"><img alt="Placement avant une sortie de vitre"[^>]*/><figcaption>[^<]*</figcaption></figure>', "", t)
    for a, b in ren.items():
        t = t.replace(f"images/{a}", f"images/{b}")
    t = t.replace('alt="Préparation compacte de fond de court"', 'alt="Coup droit et revers de fond de court, deux joueurs frappant de chaque côté"')
    t = t.replace('alt="Balle et raquette lors d’une bandeja au padel"', 'alt="Illustration de deux coups de padel : la bandeja et la víbora"')
    wr("techniques-padel.html", t)
    # alt de la carte d'accueil (régénérée plus bas) ; variantes plus légères du visuel principal et des logos
    im = Image.open("images/hero-court-v16.webp")
    for w in (640, 1000):
        im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(f"images/hero-court-v16-{w}w.webp", "WEBP", quality=80, method=6)
    for n, w in (("logo-main-clair", 300), ("logo-main-sombre", 300), ("logo-lgp-clair", 170), ("logo-lgp-sombre", 170)):
        i = Image.open(f"images/brand/{n}.webp"); i.resize((w, round(i.height * w / i.width)), Image.LANCZOS).save(f"images/brand/{n}.webp", "WEBP", quality=88, method=6)

# ---------------------------------------------------------------- fragments
THEME_JS = "(function(){var d=document.documentElement,t=null;try{t=localStorage.getItem('theme')}catch(e){}if(!t&&window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)t='dark';d.setAttribute('data-theme',t==='dark'?'dark':'light')})();"
HEAD_ADD = f"""<link rel="icon" href="/favicon.ico" sizes="48x48"/>
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png"/>
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png"/>
<link rel="apple-touch-icon" href="/apple-touch-icon.png"/>
<meta name="theme-color" content="#0B2A45"/>
<script>{THEME_JS}</script>
<link href="/redesign.css?v={V}" rel="stylesheet"/>
"""
BODY_ADD = """<a class="lgp-skip" href="#contenu">Aller au contenu</a>
<script>document.body.classList.toggle('dark-mode',document.documentElement.getAttribute('data-theme')==='dark');</script>
"""
SUN = '<svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
MOON = '<svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'

def header(current=""):
    def a(href, label, key=""):
        c = ' aria-current="page"' if key and key == current else ""
        return f'<a href="{href}"{c}>{label}</a>'
    return f"""<header class="lgp-header"><div class="lgp-header-in">
<button class="lgp-burger" id="lgp-burger" type="button" aria-controls="lgp-menu" aria-expanded="false" aria-label="Ouvrir le menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
<a class="lgp-brand" href="/" aria-label="Le Guide du Padel, accueil">
<img class="b-desktop b-light" src="/images/brand/logo-main-clair.webp" width="300" height="149" alt="Le Guide du Padel"/>
<img class="b-desktop b-dark" src="/images/brand/logo-main-sombre.webp" width="300" height="149" alt="" aria-hidden="true"/>
<img class="b-mobile b-light" src="/images/brand/logo-lgp-clair.webp" width="170" height="97" alt="LGP – Le Guide du Padel"/>
<img class="b-mobile b-dark" src="/images/brand/logo-lgp-sombre.webp" width="170" height="97" alt="" aria-hidden="true"/>
</a>
<nav class="lgp-nav" aria-label="Navigation principale">{a('/#commencer','Par où commencer')}{a('/#guides','Tous les guides')}{a('/a-propos','À propos','a-propos')}{a('/contact','Contact','contact')}</nav>
<button class="lgp-switch" id="theme-toggle" type="button" role="switch" aria-checked="false" aria-label="Mode sombre"><span class="k">{SUN}{MOON}</span></button>
</div></header>
<div class="lgp-overlay" id="lgp-overlay" hidden></div>
<aside class="lgp-menu" id="lgp-menu" aria-label="Menu" aria-hidden="true" inert tabindex="-1">
<div class="lgp-menu-top"><a href="/" aria-label="Le Guide du Padel, accueil"><img class="b-light" src="/images/brand/logo-main-clair.webp" width="300" height="149" alt="Le Guide du Padel"/><img class="b-dark" src="/images/brand/logo-main-sombre.webp" width="300" height="149" alt="" aria-hidden="true"/></a><button class="lgp-close" id="lgp-close" type="button" aria-label="Fermer le menu">×</button></div>
<nav aria-label="Navigation"><ul><li><a href="/#commencer">Par où commencer</a></li><li><a href="/#guides">Tous les guides</a></li><li><a href="/a-propos">À propos</a></li><li><a href="/contact">Contact</a></li></ul></nav>
<h2>Matériel</h2><ul><li><a href="/raquette-debutant">Choisir sa première raquette</a></li><li><a href="/chaussures-padel">Le guide des chaussures</a></li><li><a href="/balles-padel">Le guide des balles</a></li></ul>
<h2>Jouer et progresser</h2><ul><li><a href="/regles-padel">Les règles du jeu</a></li><li><a href="/techniques-padel">Les coups techniques</a></li><li><a href="/tactique-filet">Dominer le filet</a></li></ul>
<h2>Santé</h2><ul><li><a href="/echauffement-padel">L’échauffement en 10 minutes</a></li><li><a href="/raquette-tendinite">Prévention tendinite</a></li></ul>
</aside>
"""

FOOTER = """<footer class="lgp-footer">
<div class="lgp-footer-in">
<div><img src="/images/brand/logo-main-sombre.webp" width="300" height="149" alt="Le Guide du Padel" loading="lazy"/><p>Le Guide du Padel est un projet éditorial indépendant, créé avec l’ambition de réunir progressivement des passionnés autour de contenus utiles, accessibles et vérifiés.</p></div>
<nav aria-label="Matériel et santé"><h2>Matériel et santé</h2><ul><li><a href="/raquette-debutant">Première raquette</a></li><li><a href="/chaussures-padel">Chaussures</a></li><li><a href="/balles-padel">Balles</a></li><li><a href="/raquette-tendinite">Prévention tendinite</a></li><li><a href="/echauffement-padel">Échauffement</a></li></ul></nav>
<nav aria-label="Jouer et progresser"><h2>Jouer et progresser</h2><ul><li><a href="/regles-padel">Règles du jeu</a></li><li><a href="/techniques-padel">Coups techniques</a></li><li><a href="/tactique-filet">Tactique au filet</a></li></ul></nav>
<nav aria-label="Le site"><h2>Le site</h2><ul><li><a href="/a-propos">À propos</a></li><li><a href="/contact">Contact</a></li><li><a href="/mentions-legales">Mentions légales</a></li><li><a href="/confidentialite">Confidentialité</a></li></ul></nav>
</div>
<div class="lgp-footer-base"><span>© 2026 Le Guide du Padel · Le padel à portée de tous</span><span>Certains liens sont des liens affiliés Amazon (Partenaire Amazon). Ils ne changent pas le prix pour vous.</span></div>
</footer>
<button class="lgp-top" id="lgp-top" type="button" aria-label="Revenir en haut de la page">↑</button>
"""

def signature():
    return """<aside class="lgp-signature" aria-label="Signature de l’article">
<span><img class="s-light" src="/images/brand/signature-clair.webp" width="300" height="91" alt="Un article signé Le Guide du Padel" loading="lazy"/><img class="s-dark" src="/images/brand/signature-sombre.webp" width="300" height="91" alt="" aria-hidden="true" loading="lazy"/></span>
<p><strong>Un article signé Le Guide du Padel.</strong> Le Guide du Padel est un projet éditorial indépendant, créé avec l’ambition de réunir progressivement des passionnés autour de contenus utiles, accessibles et vérifiés. Une erreur, une précision à apporter ? <a href="/contact">Écrivez-nous</a>.</p>
</aside>
"""

def related(slug):
    cards = "".join(f'<a href="/{s}"><small>{CAT[ART[s][0]][0]}</small>{html.escape(ART[s][2])}</a>' for s in REL[slug])
    return f'<section class="lgp-related" aria-labelledby="lgp-rel"><h2 id="lgp-rel">À lire ensuite</h2><div class="lgp-related-grid">{cards}</div></section>\n'

def reading_minutes(t):
    m = re.search(r"<main.*?</main>", t, re.S)
    txt = re.sub(r"<(script|style).*?</\1>", " ", m.group(0) if m else t, flags=re.S)
    words = len(re.sub(r"<[^>]+>", " ", txt).split())
    return max(2, round(words / 200))

# ---------------------------------------------------------------- transformation commune
def transform(p, slug):
    t = rd(p)
    # tête
    t = re.sub(r'(<link href="style\.css[^>]*/>)', r"\1\n" + HEAD_ADD.replace("\\", "\\\\"), t, count=1)
    # en-tête + menu
    cur = {"a-propos": "a-propos", "contact": "contact"}.get(slug, "")
    t = re.sub(r'<header class="header">.*?</aside>\n?', lambda m: header(cur), t, count=1, flags=re.S)
    # corps : lien d'évitement + thème
    t = re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + "\n" + BODY_ADD, t, count=1)
    # cible du lien d'évitement
    if "<main" in t:
        t = re.sub(r"<main ", '<main id="contenu" tabindex="-1" ', t, count=1)
    else:
        t = re.sub(r'<div class="container', '<div id="contenu" tabindex="-1" class="container', t, count=1)
    # pied de page + script
    t = re.sub(r'<footer class="footer">.*?</footer>', lambda m: FOOTER, t, count=1, flags=re.S)
    t = re.sub(r'<script defer="" src="script\.js[^"]*"></script>', f'<script defer src="/script.js?v={V}"></script>', t)
    if slug in ART:
        cat = CAT[ART[slug][0]]
        mins = reading_minutes(t)
        byline = f'<div class="lgp-byline"><span class="lgp-tag t-{cat[1]}">{cat[0]}</span><span>Par Le Guide du Padel</span><span>{mins} min de lecture</span></div>'
        t, n = re.subn(r'<p class="editorial-guide-lead"><em>Publié par Le Guide du Padel</em></p>', byline, t)
        if not n:
            t = re.sub(r"(</h1>)", r"\1\n" + byline, t, count=1)
        # fin d'article : signature + articles liés, avant la publicité du bas (qui reste hors des encadrés)
        end = signature() + related(slug)
        if '<div class="ad-banner-bottom' in t:
            t = t.replace('<div class="ad-banner-bottom', end + '<div class="ad-banner-bottom', 1)
        else:
            t = t.replace("</main>", end + "</main>", 1)
        # sommaire manquant (articles longs)
        if "editorial-jump-nav" not in t:
            m = re.search(r"<main.*?</main>", t, re.S)
            h2s = re.findall(r"<h2([^>]*)>(.*?)</h2>", m.group(0), re.S)
            if len(h2s) >= 4:
                links, i = [], 0
                for attrs, inner in h2s:
                    i += 1
                    idm = re.search(r'id="([^"]+)"', attrs)
                    hid = idm.group(1) if idm else f"section-{i}"
                    if not idm:
                        t = t.replace(f"<h2{attrs}>{inner}</h2>", f'<h2{attrs} id="{hid}">{inner}</h2>', 1)
                    links.append(f'<a href="#{hid}">{re.sub("<[^>]+>", "", inner).strip()}</a>')
                toc = f'<nav aria-label="Sommaire de l’article" class="editorial-jump-nav"><strong>Dans cet article</strong><div class="editorial-jump-links">{"".join(links)}</div></nav>\n'
                first = re.search(r"<h2", t[t.index("<main"):])
                pos = t.index("<main") + first.start()
                t = t[:pos] + toc + t[pos:]
    wr(p, t)

# ---------------------------------------------------------------- accueil
def home(p):
    t = rd(p)
    head = t[: t.index("<body")]
    head = re.sub(r'(<link href="style\.css[^>]*/>)', r"\1\n" + HEAD_ADD.replace("\\", "\\\\"), head, count=1)
    head = head.replace('<link href="style.css?v=10A15" rel="stylesheet"/>', "")  # le gabarit d'accueil n'utilise plus les styles historiques
    imgs = {
     "raquette-debutant": ('images/raquette-exemple-800w.webp', 800, 497, "Deux joueurs se passant une raquette de padel au-dessus du filet"),
     "regles-padel": ("images/regles.webp", 968, 524, "Schéma d’une piste de padel vue de dessus avec la trajectoire d’un service"),
     "chaussures-padel": ("images/chaussures-800w.jpg", 800, 437, "Paire de chaussures de sport noires à bandes blanches sur fond noir"),
     "techniques-padel": ("images/bandeja-480w.webp", 595, 375, "Illustration de deux coups de padel : la bandeja et la víbora"),
     "tactique-filet": ("images/double-800w.webp", 800, 533, "Deux joueurs de padel au filet pendant un match en double"),
     "balles-padel": ("images/balle-800w.jpg", 800, 350, "Tas de balles jaunes"),
     "echauffement-padel": ("images/echauffement-800w.webp", 800, 457, "Joueuse étirant la jambe pendant un échauffement"),
     "raquette-tendinite": ("images/epicondylite-800w.webp", 800, 485, "Schéma anatomique de l’épicondylite latérale au niveau du coude"),
    }
    order = ["raquette-debutant", "regles-padel", "chaussures-padel", "techniques-padel", "tactique-filet", "balles-padel", "echauffement-padel", "raquette-tendinite"]
    cards = ""
    for i, s in enumerate(order):
        c = ART[s][0]; src, w, h, alt = imgs[s]
        feat = " is-feature" if i == 0 else ""
        eager = 'fetchpriority="low" loading="lazy"'
        cards += f'''<article class="lgp-card{feat}" data-category="{c}"><img src="/{src}" width="{w}" height="{h}" alt="{alt}" decoding="async" {eager}/><div class="lgp-card-body"><span class="lgp-tag t-{c}">{CAT[c][0]}</span><h3><a href="/{s}">{html.escape(ART[s][2])}</a></h3><p>{html.escape(ART[s][3])}</p><span class="lgp-card-cta" aria-hidden="true">Lire le guide →</span></div></article>\n'''
    def path(title, sub, items):
        li = "".join(f'<li><a href="/{s}">{html.escape(l)}</a></li>' for s, l in items)
        return f'<div class="lgp-path"><h3>{title}</h3><p>{sub}</p><ol>{li}</ol></div>'
    paths = (path("Je débute", "Trois lectures pour comprendre le jeu et partir du bon pied.", [("regles-padel", "Comprendre les règles"), ("raquette-debutant", "Choisir sa première raquette"), ("chaussures-padel", "S’équiper de bonnes chaussures")])
             + path("Je veux progresser", "Des gestes, du placement et une routine pour gagner en confiance.", [("techniques-padel", "Maîtriser les coups clés"), ("tactique-filet", "Prendre le filet en double"), ("echauffement-padel", "Adopter une routine d’échauffement")])
             + path("Je choisis mon matériel", "Raquette, chaussures, balles : de quoi décider sans se tromper.", [("raquette-debutant", "Raquette pour débuter"), ("raquette-tendinite", "Raquette et sensibilité du coude"), ("balles-padel", "Balles : choisir et changer")]))
    body = f'''<body class="page-home lgp-page">
{BODY_ADD}{header()}
<main id="contenu" tabindex="-1" class="lgp-home">
<section class="lgp-hero" aria-labelledby="home-title"><div class="lgp-wrap">
<div><p class="lgp-eyebrow">Le padel à portée de tous</p>
<h1 id="home-title">Mieux comprendre. <em>Mieux choisir.</em> Mieux jouer.</h1>
<p class="lgp-lead">Des guides clairs et indépendants pour maîtriser les règles, choisir un équipement adapté et progresser avec confiance sur la piste.</p>
<div class="lgp-cta"><a class="lgp-btn lgp-btn-primary" href="#guides">Explorer les guides <span aria-hidden="true">→</span></a><a class="lgp-btn lgp-btn-ghost" href="/raquette-debutant">Choisir sa première raquette</a></div>
<ul class="lgp-proof" aria-label="Nos engagements"><li>Conseils concrets</li><li>Lecture rapide</li><li>Liens affiliés signalés</li></ul></div>
<div class="lgp-hero-visual"><img src="/images/hero-court-v16-1000w.webp" srcset="/images/hero-court-v16-640w.webp 640w, /images/hero-court-v16-1000w.webp 1000w" sizes="(max-width:980px) calc(100vw - 32px), 540px" width="1000" height="667" alt="Raquette de padel appuyée contre le filet, balle jaune au sol, piste bleue ensoleillée" fetchpriority="high"/>
<div class="lgp-chip c1"><strong>8 guides</strong>pour bien débuter</div><div class="lgp-chip c2"><strong>3 thèmes</strong>pour progresser</div></div>
</div></section>
<div class="lgp-wrap">
<section class="lgp-sec" id="commencer" aria-labelledby="t-start"><div class="lgp-sec-head"><div><h2 id="t-start">Par où commencer ?</h2><p class="lgp-sec-sub">Choisissez votre point de départ : chaque parcours enchaîne les guides dans un ordre logique.</p></div></div><div class="lgp-paths">{paths}</div></section>
<section class="lgp-sec" id="guides" aria-labelledby="t-all"><div class="lgp-sec-head"><div><h2 id="t-all">Tous nos guides pratiques</h2><p class="lgp-sec-sub">Filtrez par thème pour aller droit à l’essentiel.</p></div></div>
<div class="lgp-filters" role="group" aria-label="Filtrer les guides par thème"><button class="lgp-filter" type="button" data-filter="all" aria-pressed="true">Tous</button><button class="lgp-filter" type="button" data-filter="materiel" aria-pressed="false">Matériel</button><button class="lgp-filter" type="button" data-filter="regles" aria-pressed="false">Règles &amp; tactique</button><button class="lgp-filter" type="button" data-filter="sante" aria-pressed="false">Santé &amp; blessures</button></div>
<div class="lgp-grid">
{cards}</div></section>
</div>
<!-- Emplacement publicitaire isolé : masqué en production tant qu'aucune annonce n'est branchée.
     Pour l'activer : placer le bloc <ins class="adsbygoogle"> dans .lgp-ad-box et ajouter la classe is-live à <aside class="lgp-ad"> -->
<aside class="lgp-ad" aria-label="Publicité"><span class="lgp-ad-label">Publicité</span><div class="lgp-ad-box">Emplacement test : bannière responsive</div></aside>
<div class="lgp-wrap"><section class="lgp-trust" aria-labelledby="t-trust"><h2 id="t-trust">Notre démarche</h2><p class="lgp-sec-sub">Un site indépendant, géré avec une idée simple : expliquer le padel sans jargon et sans promesse miracle.</p>
<div class="lgp-trust-grid"><div><h3>Des guides utiles</h3><p>Chaque guide répond à une vraie question de joueur : quoi acheter, comment se placer, comment éviter de se blesser.</p></div><div><h3>Une information vérifiée</h3><p>Nous nous appuyons sur les règles officielles et sur des sources citées. En cas d’erreur, signalez-la : nous corrigeons.</p></div><div><h3>Une transparence totale</h3><p>Certains liens renvoient vers Amazon et peuvent nous rapporter une commission, sans surcoût pour vous. Les contenus restent clairement séparés des publicités.</p></div></div>
<p class="lgp-trust-note">Le Guide du Padel est un projet éditorial indépendant, créé avec l’ambition de réunir progressivement des passionnés autour de contenus utiles, accessibles et vérifiés. <a href="/a-propos">En savoir plus</a> · <a href="/contact">Nous écrire</a></p></section></div>
<div class="lgp-end"></div>
</main>
{FOOTER}<script defer src="/script.js?v={V}"></script>
<script data-cf-beacon='{{"token":"e73f652447404adfa9c4ad678725f193"}}' src="https://static.cloudflareinsights.com/beacon.min.js" type="module"></script></body>
</html>
'''
    wr(p, head + body)

SCRIPT = r"""/* Le Guide du Padel — script 2026 : thème, menu mobile, filtre d'accueil, retour en haut. Sans dépendance. */
(function () {
  var d = document, root = d.documentElement;
  function ready(f) { d.readyState !== 'loading' ? f() : d.addEventListener('DOMContentLoaded', f); }
  ready(function () {
    /* Thème : slider (role=switch) */
    var sw = d.getElementById('theme-toggle');
    function apply(dark) {
      root.setAttribute('data-theme', dark ? 'dark' : 'light');
      d.body.classList.toggle('dark-mode', dark);
      if (sw) sw.setAttribute('aria-checked', String(dark));
    }
    apply(root.getAttribute('data-theme') === 'dark');
    if (sw) sw.addEventListener('click', function () {
      var dark = root.getAttribute('data-theme') !== 'dark';
      apply(dark);
      try { localStorage.setItem('theme', dark ? 'dark' : 'light'); } catch (e) {}
    });

    /* Menu mobile accessible */
    var b = d.getElementById('lgp-burger'), m = d.getElementById('lgp-menu'), o = d.getElementById('lgp-overlay'), c = d.getElementById('lgp-close');
    if (b && m && o && c) {
      var last = null;
      var close = function () {
        m.classList.remove('is-open'); o.hidden = true;
        m.setAttribute('aria-hidden', 'true'); m.setAttribute('inert', '');
        b.setAttribute('aria-expanded', 'false'); b.setAttribute('aria-label', 'Ouvrir le menu');
        root.classList.remove('lgp-lock');
        if (last) last.focus();
      };
      var open = function () {
        last = d.activeElement; o.hidden = false; m.classList.add('is-open');
        m.setAttribute('aria-hidden', 'false'); m.removeAttribute('inert');
        b.setAttribute('aria-expanded', 'true'); b.setAttribute('aria-label', 'Fermer le menu');
        root.classList.add('lgp-lock'); c.focus();
      };
      b.addEventListener('click', function () { m.classList.contains('is-open') ? close() : open(); });
      c.addEventListener('click', close); o.addEventListener('click', close);
      m.addEventListener('click', function (e) { if (e.target.closest('a')) close(); });
      d.addEventListener('keydown', function (e) {
        if (!m.classList.contains('is-open')) return;
        if (e.key === 'Escape') { e.preventDefault(); close(); }
        if (e.key === 'Tab') {
          var q = m.querySelectorAll('a[href],button:not([disabled])'), f = q[0], l = q[q.length - 1];
          if (e.shiftKey && d.activeElement === f) { e.preventDefault(); l.focus(); }
          else if (!e.shiftKey && d.activeElement === l) { e.preventDefault(); f.focus(); }
        }
      });
      window.addEventListener('resize', function () { if (innerWidth > 860 && m.classList.contains('is-open')) close(); });
    }

    /* Filtre des guides (accueil) */
    var bar = d.querySelector('.lgp-filters');
    if (bar) {
      var cards = [].slice.call(d.querySelectorAll('.lgp-card[data-category]')), btns = [].slice.call(bar.querySelectorAll('.lgp-filter'));
      bar.addEventListener('click', function (e) {
        var btn = e.target.closest('.lgp-filter'); if (!btn) return;
        var f = btn.getAttribute('data-filter');
        btns.forEach(function (x) { x.setAttribute('aria-pressed', String(x === btn)); });
        cards.forEach(function (card) { card.hidden = !(f === 'all' || card.getAttribute('data-category') === f); });
      });
    }

    /* Emplacements de test visibles uniquement en local / preview */
    var h = location.hostname;
    d.body.classList.toggle('preview-mode', h === 'localhost' || h === '127.0.0.1' || /\.workers\.dev$/.test(h));

    /* Retour en haut */
    var top = d.getElementById('lgp-top');
    if (top) {
      var tick = false;
      window.addEventListener('scroll', function () {
        if (tick) return; tick = true;
        requestAnimationFrame(function () { top.classList.toggle('is-on', window.scrollY > 900); tick = false; });
      }, { passive: true });
      top.addEventListener('click', function () {
        var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
        window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
      });
    }
  });
})();
"""

HEADERS_CSP = ("default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'self'; "
 "script-src 'self' 'unsafe-inline' https://static.cloudflareinsights.com https://pagead2.googlesyndication.com https://*.googlesyndication.com https://fundingchoicesmessages.google.com https://*.adtrafficquality.google https://partner.googleadservices.com https://www.googletagservices.com https://*.google.com; "
 "style-src 'self' 'unsafe-inline'; "
 "img-src 'self' data: https:; "
 "font-src 'self'; "
 "connect-src 'self' https://cloudflareinsights.com https://*.cloudflareinsights.com https://pagead2.googlesyndication.com https://*.googlesyndication.com https://fundingchoicesmessages.google.com https://*.adtrafficquality.google https://*.google.com https://*.doubleclick.net; "
 "frame-src https://googleads.g.doubleclick.net https://*.doubleclick.net https://*.googlesyndication.com https://fundingchoicesmessages.google.com https://*.google.com https://*.adtrafficquality.google; "
 "form-action 'self' mailto:; upgrade-insecure-requests")

def main():
    fix_images()
    for p in sorted(f for f in os.listdir(".") if f.endswith(".html")):
        slug = p[:-5]
        if slug == "index":
            home(p)
        else:
            transform(p, slug)
    wr("script.js", SCRIPT)
    h = rd("_headers")
    h = re.sub(r"  Content-Security-Policy:.*", "  Content-Security-Policy: " + HEADERS_CSP, h, count=1)
    h = h.replace("/style.css\n", "/redesign.css\n  Cache-Control: public, max-age=3600, must-revalidate\n\n/style.css\n", 1)
    wr("_headers", h)
    # mentions légales : l'hébergement réel est Cloudflare Workers (wrangler.jsonc), pas Cloudflare Pages
    ml = rd("mentions-legales.html")
    ml = ml.replace("Cloudflare Pages", "Cloudflare (Workers)")
    wr("mentions-legales.html", ml)
    print("ok")

if __name__ == "__main__":
    main()
