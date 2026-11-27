# Benchmark accueil mobile (méthode du skill « benchmark »)
Simulation : Chromium, viewport 412×823, 4G lente (1,6 Mbit/s, 150 ms), CPU ×4, scripts AdSense/Cloudflare bloqués, médiane de 4 à 5 passages. Valeurs simulées, pas celles de PageSpeed (qui varient de ±5 à 10 points d'un passage à l'autre).

| Version | FCP | LCP | CSS (Ko gzip) | Poids total (Ko) | Requêtes |
|---|---|---|---|---|---|
| v10 (3 CSS) | 1 056 ms | 1 388 ms | 15,5 | 268 | 13 |
| v16 | 1 168 ms | 1 168 ms | 30,1 | 131 | 10 |
| v17 | 1 176 ms | 1 176 ms | 30,1 | 126 | 10 |
| v18 | 1 168 ms | 1 168 ms | 30,1 | 126 | 10 |
| v19 (images 800w + AVIF) | 1 012 ms | 1 012 ms | 30,2 | 114 | 10 |
| v19 + home.css (prototype, non appliqué) | 960 ms | 960 ms | 7,4 | 91 | 12 |

Constat : v17 et v18 sont identiques (écart de 8 ms = bruit). L'accueil n'utilise que 10 % du CSS qu'il charge (20 Ko sur 196 Ko).
Prototype : Tools/prototype/home.css (26 Ko brut, 7 Ko gzip) rend l'accueil pixel pour pixel identique (4 captures). Pour l'adopter : dans index.html, remplacer /style.css?v=… par /home.css?v=… et déposer home.css à la racine. Contrepartie : deux fichiers CSS à maintenir.
