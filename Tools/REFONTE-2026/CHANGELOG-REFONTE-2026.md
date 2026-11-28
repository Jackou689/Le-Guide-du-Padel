# Changelog — Refonte 2026 (base : lot 10A.17, branche `redesign-2026`)

## Résumé
- Nouvelle couche de design `redesign.css` (variables, clair/sombre, composants préfixés `.lgp-`), chargée **après** `style.css` (approche additive : aucun composant historique supprimé).
- Nouvel en-tête (logo validé clair/sombre, logo mobile « LGP », slider clair/sombre sans vert), menu mobile accessible, pied de page complet, bouton retour en haut, lien d'évitement.
- Nouvel accueil « Style Moderne » : hero utile, « Par où commencer », bibliothèque filtrable, emplacement publicitaire isolé, section « Notre démarche ».
- Articles : bloc de ligne d'info (catégorie, auteur, temps de lecture), signature « Un article signé », « À lire ensuite », sommaire généré si absent (tactique-filet). Contenu éditorial inchangé.
- Favicons ajoutés (aucune balise favicon n'existait dans le lot 10A.17).
- Images : correction des noms et des associations de la page « techniques ».
- `_headers` : CSP corrigée pour autoriser AdSense / CMP Google (voir rapport).
- `script.js` réécrit (thème, menu, filtre, retour en haut), sans dépendance.
- Mentions légales : « Cloudflare Pages » → « Cloudflare (Workers) » (à confirmer).

## Itération 2 (28/10/2026)
- Logos plus grands et plus nets (en-tête 84 px), liseré clair en mode sombre ; logo mobile centré (grille 3 colonnes).
- Menu mobile corrigé (débordement de padding, `100dvh`, indice de défilement, zone haute collée).
- En-tête masquée au défilement vers le bas, réaffichée vers le haut ; barre de progression de lecture.
- Emphase sur les notions clés des 8 guides (`.lgp-key`) ; sous-titres h4 → `aria-level="3"` (chaussures, tendinite).
- Jeu d'illustrations au style unique (8 cartes d'accueil, hero, 2 schémas d'article) ; schémas lob et jeu après la vitre réinsérés.

## Fichiers ajoutés (cumul depuis le lot 10A.17)
- `Tools/REFONTE-2026/CHANGELOG-REFONTE-2026.md`
- `Tools/REFONTE-2026/RAPPORT-REFONTE-2026.md`
- `Tools/REFONTE-2026/RECOMMANDATIONS-EDITORIALES.md`
- `Tools/REFONTE-2026/illustrations-src/ill-balles.svg`
- `Tools/REFONTE-2026/illustrations-src/ill-chaussures.svg`
- `Tools/REFONTE-2026/illustrations-src/ill-echauffement.svg`
- `Tools/REFONTE-2026/illustrations-src/ill-hero.svg`
- `Tools/REFONTE-2026/illustrations-src/ill-lob.svg`
- `Tools/REFONTE-2026/illustrations-src/ill-raquette.svg`
- `Tools/REFONTE-2026/illustrations-src/ill-regles.svg`
- `Tools/REFONTE-2026/illustrations-src/ill-tactique.svg`
- `Tools/REFONTE-2026/illustrations-src/ill-techniques.svg`
- `Tools/REFONTE-2026/illustrations-src/ill-tendinite.svg`
- `Tools/REFONTE-2026/illustrations-src/ill-vitre-fond.svg`
- `Tools/build_refonte_2026.py`
- `Tools/emphasize_articles.py`
- `Tools/make_illustrations.py`
- `apple-touch-icon.png`
- `favicon-16.png`
- `favicon-32.png`
- `favicon.ico`
- `images/brand/icon-512.png`
- `images/brand/logo-lgp-clair.webp`
- `images/brand/logo-lgp-sombre.webp`
- `images/brand/logo-main-clair.webp`
- `images/brand/logo-main-sombre.webp`
- `images/brand/signature-clair.webp`
- `images/brand/signature-sombre.webp`
- `images/hero-court-v16-1000w.webp`
- `images/hero-court-v16-640w.webp`
- `images/ill-balles-640w.webp`
- `images/ill-balles.webp`
- `images/ill-chaussures-640w.webp`
- `images/ill-chaussures.webp`
- `images/ill-echauffement-640w.webp`
- `images/ill-echauffement.webp`
- `images/ill-hero-640w.webp`
- `images/ill-hero.webp`
- `images/ill-lob-640w.webp`
- `images/ill-lob.webp`
- `images/ill-raquette-640w.webp`
- `images/ill-raquette.webp`
- `images/ill-regles-640w.webp`
- `images/ill-regles.webp`
- `images/ill-tactique-640w.webp`
- `images/ill-tactique.webp`
- `images/ill-techniques-640w.webp`
- `images/ill-techniques.webp`
- `images/ill-tendinite-640w.webp`
- `images/ill-tendinite.webp`
- `images/ill-vitre-fond-640w.webp`
- `images/ill-vitre-fond.webp`
- `redesign.css`

## Fichiers modifiés
- `404.html`
- `_headers`
- `a-propos.html`
- `balles-padel.html`
- `chaussures-padel.html`
- `confidentialite.html`
- `contact.html`
- `echauffement-padel.html`
- `index.html`
- `mentions-legales.html`
- `raquette-debutant.html`
- `raquette-tendinite.html`
- `regles-padel.html`
- `script.js`
- `tactique-filet.html`
- `techniques-padel.html`

## Fichiers renommés
- `images/technique-lob.webp → images/a-verifier-frappe-aerienne.webp`
- `images/technique-bajada.webp → images/padel-bajada.webp`
- `images/technique-vitre-fond.webp → images/padel-bandeja.webp`
- `images/technique-transition-filet.webp → images/padel-chiquita.webp`
- `images/technique-fond-court.webp → images/padel-double-vitre.webp`
- `images/technique-vibora.webp → images/padel-fond-de-court-coup-droit-revers.webp`
- `images/technique-bandeja.webp → images/padel-position-attente-appuis.webp`
- `images/technique-position.webp → images/padel-position-attente.webp`
- `images/technique-smash.webp → images/padel-smash.webp`
- `images/technique-volees.webp → images/padel-transition-fond-filet.webp`
- `images/technique-double-vitre.webp → images/padel-vibora.webp`
- `images/technique-chiquita.webp → images/padel-volee.webp`

## Fichiers supprimés
- (aucun)
