# Changelog v17 (24 novembre 2026)

## Images principales : AVIF avec repli WebP/JPEG
- Les 6 images de tête d'article (règles, raquette débutant, tactique, balles, échauffement, chaussures) sont servies en AVIF (<picture>), avec l'image WebP/JPEG d'origine en repli. Poids : hero « Règles » 141 → 85 Ko (1000w), « Raquette débutant » 145 → 85 Ko (1200w), « Tactique » 103 → 62 Ko, « Balles » 106 → 66 Ko, « Échauffement » 89 → 56 Ko, « Chaussures » 52 → 19 Ko.
- Rendu : SSIM ≈ 0,96 (équivalent au WebP actuel, 0,97) ; comparaison visuelle à 100 % sans différence notable.
- Repli de sécurité (script.js) : si un fichier .avif est introuvable (téléversement incomplet), l'image retombe automatiquement sur le WebP/JPEG. Testé en supprimant tous les .avif et .woff2.

## Polices : WOFF2 avec repli WOFF
- poppins-500 et poppins-700 : 9,9 → 7,3 Ko ; lora-var : 40,7 → 33,7 Ko. @font-face : woff2 d'abord, woff en repli ; préchargements passés en woff2. Les .woff d'origine sont conservés.

## Mesures (simulation mobile : 4G lente, CPU ×4)
- Article « Règles » : FCP 1 620 → 1 430 ms, LCP 1 860 → 1 600 ms.
- Article « Raquette débutant » : LCP 1 600 → 1 430 ms.
- Mise en page : 76 comparaisons (19 pages × ordinateur/mobile × clair/sombre) : 0 différence de position ou de taille des éléments.

## À téléverser : voir Tools/FICHIERS-V17.txt
