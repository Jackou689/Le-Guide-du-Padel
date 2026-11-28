# Changelog v20 (27 novembre 2026)

## CSS en couches (remplace le fichier unique de la v11)
- style.css (58 Ko brut, 13 Ko gzip) : socle commun, seul fichier chargé par l'accueil.
- articles.css (136 Ko brut, 17 Ko gzip) : pages intérieures, chargé avant style.css.
- Accueil : CSS 30,2 → 13,2 Ko gzip ; FCP/LCP simulé 1 080 → 968 ms ; poids total 114 → 97 Ko.
- Pages intérieures : inchangées (écart dans le bruit).
- Vérifié : 76 comparaisons de mise en page (19 pages × 4 configurations) sans différence ; 10 captures pleine page identiques au pixel près (accueil, règles, contact, 404 ; clair/sombre ; mobile/ordinateur).
- Les garde-fous « accueil » (:where(:not(.page-home))) ajoutés en v11 sont retirés : l'accueil ne charge plus la couche historique. L'attribut data-page="home" disparaît de index.html.
- Versions ?v=2026-15. En-têtes de cache ajoutés pour /articles.css.
- Voir Tools/CSS-ARCHITECTURE.md.

## Décisions
- CSS dédié à l'accueil (home.css) : abandonné, il dupliquait des règles dans deux fichiers à synchroniser.
- Cache long du CSS/JS : non appliqué (voir Tools/PISTES-AMELIORATION.md).

## Pistes : Tools/PISTES-AMELIORATION.md
