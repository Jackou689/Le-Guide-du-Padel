# Benchmark accueil mobile (méthode du skill « benchmark »)
Simulation : Chromium, viewport 412×823, 4G lente (1,6 Mbit/s, 150 ms), CPU ×4, scripts AdSense/Cloudflare bloqués, médiane de 4 à 5 passages. Valeurs simulées, pas celles de PageSpeed (qui varient de ±5 à 10 points d'un passage à l'autre).

| Version | FCP | LCP | CSS (Ko gzip) | Poids total (Ko) | Requêtes |
|---|---|---|---|---|---|
| v10 (3 CSS) | 1 056 ms | 1 388 ms | 15,5 | 268 | 13 |
| v16 | 1 168 ms | 1 168 ms | 30,1 | 131 | 10 |
| v17 | 1 176 ms | 1 176 ms | 30,1 | 126 | 10 |
| v18 | 1 168 ms | 1 168 ms | 30,1 | 126 | 10 |
| v19 (images 800w + AVIF) | 1 012 ms | 1 012 ms | 30,2 | 114 | 10 |
| v19 + home.css (prototype, abandonné : fichier dupliqué) | 960 ms | 960 ms | 7,4 | 91 | 12 |
| **v20 (CSS en couches : accueil = style.css seul)** | 968 ms | 968 ms | 13,2 | 97 | 10 |

Constat : v17 et v18 sont identiques (écart de 8 ms = bruit). L'accueil n'utilise que 10 % du CSS qu'il charge (20 Ko sur 196 Ko).
Décision : le CSS dédié à l'accueil dupliquait des règles dans deux fichiers à synchroniser. La séparation par couches (v20) donne presque le même gain (968 ms contre 960 ms) sans aucune duplication : articles.css (pages intérieures) + style.css (socle commun, seul fichier chargé par l'accueil).

Pages intérieures (article « Règles ») : v19 FCP 1 376 / LCP 1 520 ms ; v20 FCP 1 400 / LCP 1 560 ms (écart dans le bruit, une requête CSS de plus en parallèle).
