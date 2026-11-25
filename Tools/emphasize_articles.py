#!/usr/bin/env python3
"""Ajoute de l'emphase (balise <strong class="lgp-key">) sur les notions clés des guides.
Ne modifie aucun mot : uniquement des balises autour de texte existant, dans les paragraphes et listes.
Règles : 1re occurrence de chaque notion par article, max 2 par paragraphe, jamais dans titres, liens, légendes,
encadrés d'affiliation, publicités, tableaux, ni dans un texte déjà en gras. À lancer UNE fois sur les pages du lot."""
import re, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
APOS = "['’]"
G = {  # notion (regex) par page, dans l'ordre de priorité
 "raquette-debutant": [r"forme ronde", r"goutte d" + APOS + "eau", r"forme diamant|le diamant", r"point d" + APOS + "équilibre|équilibre", r"mousse souple|mousse dure|mousse", r"contrôle", r"tolérance", r"puissance", r"carbone|fibre de verre", r"poids", r"\d{3}\s?(?:à|et|-)\s?\d{3}\s?grammes|\d{3}\s?g\b", r"surgrip", r"prix|budget"],
 "chaussures-padel": [r"semelle[s]?\s+(?:à|en)\s+chevrons|chevrons", r"adhérence", r"maintien latéral|maintien", r"amorti", r"semelles? de running|running", r"glissades?", r"torsion", r"usure", r"pointure", r"entorse"],
 "balles-padel": [r"pression interne|pression", r"rebond", r"feutre", r"tube pressurisé|pressurisée?s?", r"durée de vie", r"homologu\w+|règlement", r"balle standard", r"balle rapide|balles rapides"],
 "raquette-tendinite": [r"épicondylite|tennis elbow", r"tendinite", r"vibrations?", r"mousse (?:souple|molle)|mousse", r"poids", r"équilibre", r"manche", r"avis médical|médecin|professionnel de santé", r"douleur[s]?", r"repos"],
 "echauffement-padel": [r"mobilité articulaire|mobilité", r"échauffement", r"articulations?", r"poignets?", r"épaules?", r"chevilles?", r"genoux", r"élastique", r"progressi\w+", r"10 minutes|dix minutes", r"15 minutes|quinze minutes", r"étirements?"],
 "regles-padel": [r"service à la cuillère|service", r"sous la ceinture|au niveau de la hanche", r"deux rebonds|double rebond", r"vitres?", r"filet", r"point d" + APOS + "or|golden point", r"jeu décisif|tie-break", r"20\s?m(?:ètres)?\s+(?:de long|sur)|10\s?m(?:ètres)?\s+de large|20 x 10|20 m", r"par équipe|en double|à quatre", r"faute"],
 "techniques-padel": [r"bandeja", r"v[ií]bora", r"chiquita", r"smash", r"bajada", r"\blob\b", r"volée", r"position d" + APOS + "attente", r"double vitre", r"sortie de vitre", r"prise continentale|prise marteau", r"pronation", r"coup droit", r"revers"],
 "tactique-filet": [r"prendre le filet|dominer le filet|filet", r"même ligne", r"diagonale", r"couvrir|couverture", r"communication|communiquer", r"lob", r"volée", r"placement", r"déplacement[s]? synchronis\w+|synchronis\w+", r"pression"],
}
SKIP_TAGS = {"h1","h2","h3","h4","h5","h6","a","strong","b","mark","em_never","figcaption","button","script","style","th","td","summary","svg","time","code","label","select","option","nav"}
SKIP_CLS = re.compile(r"(?:^|\s)(?:ad-|affiliate|amazon|next-step|lgp-|editorial-jump|product|breadcrumb|disclaimer|img-caption|key-phrase|editorial-key|tactic-key|intro-kicker|related|human-note|recap-title|faq-q)")
VOID = {"img","br","hr","input","meta","link","source","wbr"}
MAXPARA = 2

def process(html, rules):
    m0 = html.index("<main"); m1 = html.index("</main>")
    head, body, tail = html[:m0], html[m0:m1], html[m1:]
    toks = re.split(r"(<[^>]+>)", body)
    stack = []; used = set(); out = []; para_hits = 0; hits = []
    for tk in toks:
        if tk.startswith("<"):
            mm = re.match(r"<(/?)([a-zA-Z0-9]+)([^>]*)>", tk)
            if mm:
                close, name, attrs = mm.group(1) == "/", mm.group(2).lower(), mm.group(3)
                if name not in VOID and not attrs.rstrip().endswith("/"):
                    if close:
                        for k in range(len(stack) - 1, -1, -1):
                            if stack[k][0] == name: del stack[k:]; break
                        if name in ("p", "li"): para_hits = 0
                    else:
                        cm = re.search(r'class="([^"]*)"', attrs); stack.append((name, cm.group(1) if cm else ""))
            out.append(tk); continue
        ok = stack and any(n in ("p", "li") for n, _ in stack) and not any(n in SKIP_TAGS or SKIP_CLS.search(c) for n, c in stack)
        if ok and tk.strip():
            for pat in rules:
                if pat in used or para_hits >= MAXPARA: continue
                mt = re.search(r"(?<![\w-])(" + pat + r")(?![\w-])", tk, re.I)
                if mt:
                    s, e = mt.span(1)
                    tk = tk[:s] + f'<strong class="lgp-key">{tk[s:e]}</strong>' + tk[e:]
                    used.add(pat); para_hits += 1; hits.append(mt.group(1)); break
        out.append(tk)
    return head + "".join(out) + tail, hits

if __name__ == "__main__":
    for slug, rules in G.items():
        h = open(f"{slug}.html", encoding="utf-8").read()
        new, hits = process(h, rules)
        open(f"{slug}.html", "w", encoding="utf-8").write(new)
        print(slug, len(hits), hits)
