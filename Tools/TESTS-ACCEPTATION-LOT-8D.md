# Tests d’acceptation du lot 8D

## AC-01 — Base
- Le lot repart de 8C sans centre de préférences maison.
- 13 pages existantes conservées plus `404.html`.
- AdSense demeure inactif.

## AC-02 — Page 404
- `404.html` comporte `noindex, follow`.
- Aucun canonical trompeur.
- Liens de retour vers l’accueil, le contact et trois guides.
- Mise en page mobile et sombre.

## AC-03 — Sécurité HTTP
- `_headers` définit nosniff, Referrer-Policy, Permissions-Policy, protection de frame et CSP.
- La CSP autorise les images Unsplash déjà utilisées et le beacon Cloudflare.
- Aucun contenu HTTP non sécurisé.

## AC-04 — Redirections
- `_redirects` redirige `/index.html` vers `/`.
- Les routes sans extension prévues redirigent en 301 vers les pages actuelles.
- Aucune boucle de redirection.

## AC-05 — Contact
- L’adresse `contact@leguidedupadel.fr` reste un lien `mailto:`.
- Aucun service tiers de formulaire ajouté.
- Aucun champ collectant des données personnelles.

## AC-06 — JavaScript
- Le filtre de catégories n’est plus inline.
- `script.js` passe le contrôle syntaxique Node.
- Menu mobile, thème et placeholders de preview conservés.

## AC-07 — SEO et actifs
- Sitemap XML valide.
- Robots.txt présent.
- Tous les actifs locaux référencés existent.
- Tous les liens HTML internes pointent vers un fichier existant ou une ancre existante.
- Les 13 URL canoniques existantes sont uniques.

## AC-08 — Non-régression
- Aucun style inline.
- Liens Amazon avec `nofollow sponsored`.
- Un beacon Cloudflare par page de contenu et sur la page 404.
- Correctifs visuels des lots précédents conservés.
