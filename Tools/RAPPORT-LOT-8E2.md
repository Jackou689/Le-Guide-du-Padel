# Rapport du lot 8E.2

Cause confirmée : le lot 8E avait copié en fin de CSS global des styles auparavant propres à plusieurs pages. La règle générique `.article-content { max-width: 75ch; margin: 0 auto; }` a rétréci les articles. Le correctif 8E.1 ciblait une classe absente du HTML livré.

Modifications limitées : suppression du bloc global fautif, restauration des largeurs antérieures, ajout de deux hooks uniquement sur la page raquette débutant, correction ciblée du contraste du tableau. CSP, URL, sitemap, Wrangler et publicités inchangés.
