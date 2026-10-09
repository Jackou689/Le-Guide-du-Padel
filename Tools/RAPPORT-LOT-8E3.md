# Rapport du lot 8E.3

La régression concernait uniquement la grille de trois recommandations de `raquette-padel-tendinite.html`. Les styles locaux du lot 8D avaient disparu lors de la centralisation, puis la suppression du bloc global fautif en 8E.2 avait révélé leur absence.

Correction : ajout d’un hook de page et restauration strictement ciblée des styles de `.entry-level-grid`, `.entry-card`, `.entry-tag` et `.btn-amazon-small`, avec leurs variantes sombres.

Inchangés : largeurs 1350 px, grille principale 2.5fr/1fr, publicités, CSP, URL, sitemap, Wrangler, autres pages.

Tests navigateur : trois cartes alignées sur ordinateur, empilées sur mobile, mode sombre valide.
