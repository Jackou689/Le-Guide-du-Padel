# Refonte 2026 – livraison 2 (corrections après retours sur la livraison 1)

## Corrigé et vérifié (Chromium, 14 pages x 2 largeurs : 0 erreur, 0 requête 404, 0 débordement horizontal)
- **En-tête mobile** : cause trouvée dans style.css (règle `html,body{overflow-x:hidden}` sous 768 px) qui cassait `position:sticky`.
  Remplacée par `overflow-x:clip` (style.css ligne 759 + garde-fou en fin de redesign.css). L'en-tête se masque en descendant et réapparaît dès qu'on remonte.
- **Logos sombres** (principal + LGP) redessinés : face de raquette bleue (#1E6FE8), cadre et trous blancs, manche bleu. Nouveaux fichiers
  `images/brand/logo-main-sombre-v2.webp` et `logo-lgp-sombre-v2.webp` (nom versionné pour contourner le cache). Halo CSS blanc retiré.
- **Favicon** : symbole recadré au plus près (90 % du carreau au lieu de ~65 %). Régénérés : favicon.ico (16/32/48), favicon-16/32/192.png, apple-touch-icon.png, images/brand/icon-512.png. Liens en `?v=2`.
- **Logo mobile** centré (écart mesuré : 0 px). **Menu burger** : défile (contenu 824 px pour 800 px d'écran), page verrouillée derrière.
- **Liens** : 666 liens internes testés, 0 cassé. Mentions « règles », « raquettes », « chaussures », « s'équiper » (À propos) et « quoi acheter », « comment se placer », « comment éviter de se blesser », « règles officielles » (Notre démarche) rendues cliquables.
- Version CSS : `redesign.css?v=2026-2`.

## Revue d'accessibilité WCAG 2.1 AA (skill accessibility-review, plugin Design)
- **Contraste** : 0 texte sous le seuil sur les 14 pages, clair et sombre (hors éléments décoratifs : glyphe ⌣ Amazon, « 404 », placeholder pub).
  Corrigés : gris #718096 -> #4A5568 (légendes, mentions, fil d'Ariane), accents orange/rouge/bleu/ambre trop clairs, texte foncé sur fond foncé en mode sombre (encadrés « astuce », « piège classique », surlignages), surlignage `.lgp-key`.
- **Structure** : 1 h1 et 1 `<main>` par page (ajouté sur Mentions légales), langue fr, repère « Aller au contenu », ordre de tabulation logique, indicateur de focus visible partout, pas de défilement horizontal à 200 % de zoom.
- **Zones tactiles** : interrupteur clair/sombre et lien « Accueil » du fil d'Ariane agrandis à >= 44 px de zone cliquable sans changer l'aspect.
- Restent (mineurs, contenu) : titre de balles-padel.html à 67 caractères (> 60), 2 sauts de niveau de titre (chaussures-padel, raquette-tendinite), emplacement publicitaire « Emplacement test » encore visible sur l'accueil et 7 autres pages (à remplacer par le code AdSense ou masquer avant mise en ligne).

## En attente de validation : images (non intégrées)
Propositions dans `Tools/propositions-images/` (11 images + variantes 640w, mêmes noms que les illustrations actuelles `ill-*`).
Recadrage et étalonnage communs. Après validation : copier dans `images/` et mettre à jour les attributs `alt` (aujourd'hui « Illustration : … »).

## Reste à traiter
- Emphase des notions importantes dans les articles (classe `.lgp-key` déjà posée : 4 à 12 occurrences par article).
- Mentions légales (nom, e-mail) ; Cloudflare Speed Optimizations puis Bot Fight Mode.
