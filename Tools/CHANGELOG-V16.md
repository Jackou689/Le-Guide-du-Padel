# Changelog v16 (23 novembre 2026)

## Logo cassé sur l'aperçu : cause et correction
- Cause la plus probable : la v15 référençait 4 NOUVEAUX fichiers (images/brand/*-opt.webp). Les pages HTML ont été mises à jour sur l'aperçu, mais pas ces 4 images : le navigateur affichait une image cassée. L'archive v15 contenait bien les fichiers ; ils n'étaient pas exclus par .gitignore, .assetsignore ni wrangler.jsonc.
- Correction durable : les logos allégés reprennent les ANCIENS noms de fichier (logo-main-clair.webp, logo-main-sombre-v3.webp, logo-lgp-clair.webp, logo-lgp-sombre-v3.webp). Un téléversement incomplet ne peut plus casser l'affichage : au pire, l'ancien logo (plus lourd) reste servi. Les fichiers *-opt.webp n'existent plus (à supprimer du dépôt s'ils y sont).
- Vérification locale : 19 pages × (ordinateur clair, ordinateur sombre, mobile) : 0 requête en erreur, 0 image cassée, 0 débordement horizontal.

## Articles étoffés
- balles-padel : ≈ 1 180 → ≈ 1 390 mots (reconnaître une balle usée, combien de balles prévoir).
- tactique-filet : ≈ 1 240 → ≈ 1 530 mots (communiquer à deux, lire l'adversaire, trois situations types).

## Typographie
- Espace insécable avant « : ? ! ; » et autour des guillemets dans tous les titres (h1 à h3) : plus de ligne qui commence par un deux-points.

## Fichiers à téléverser depuis la v15 : voir Tools/FICHIERS-V16.txt
