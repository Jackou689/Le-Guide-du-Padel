# Changelog v19 (26 novembre 2026)

## Accueil : images du rapport PageSpeed
- Héros (élément LCP mobile) et cartes : variantes 800w ajoutées (WebP) et AVIF 640/800/1200 via <picture>. PageSpeed signalait des images de 1200 px servies pour un affichage de ≈ 665 px (économies estimées : 14,9 à 17,1 Kio par image). Héros : 21,6 Ko (WebP 1200w) → 9 Ko (AVIF 800w) sur mobile.
- Pas de script de repli (demande du 25/11) : un fichier manquant se verra.

## CSS
- picture{display:contents} : les <picture> ne créent aucune boîte. Sans cette règle, la carte « à la une » de l'accueil grandissait de 36 px sur ordinateur (flex + image à 50 %). Vérifié : 76 comparaisons de mise en page (19 pages × 4 configurations) sans aucune différence avec la version d'avant AVIF.
- style.css passe à ?v=2026-14.

## Analyse de la capture PageSpeed (mobile, aperçu)
- Score 81 → 83 ; LCP 4,7 → 3,7 s. FCP 2,2 → 3,2 s : écart attribuable au CSS fusionné (30 Ko au lieu de 15 Ko sur l'accueil) et à la variabilité de PageSpeed ; en simulation locale v17 = v18.
- « Requêtes de blocage du rendu » (150 ms) : le CSS. L'accueil n'en utilise que 10 %. Prototype home.css dans Tools/prototype (non appliqué).
- « Durées de cache » (21 Kio) : style.css et script.js sont servis avec max-age=3600. Possible : max-age long + immutable (URL déjà versionnées par ?v=), à condition de toujours changer ?v= après une modification. Non appliqué.
- « Ancien JavaScript » (10 Kio) : beacon Cloudflare, non modifiable.
- Logo mobile (170×97 affiché pour un fichier de 280×160) : conservé, la taille couvre les écrans 2× et 3×.
