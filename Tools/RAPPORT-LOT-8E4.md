# Rapport du lot 8E.4

## Cause générale

Le lot 8D contenait des styles de composants dans plusieurs balises `<style>` propres aux pages. Le lot 8E avait supprimé ces balises puis copié les règles sans isolation dans le CSS global. Le lot 8E.2 a retiré ce bloc global pour corriger les largeurs, révélant l’absence des styles de composants sur plusieurs pages.

## Correction générale

Les styles de composants du lot 8D ont été restaurés pour six pages et préfixés par une classe de page. Les règles globales de largeur et de typographie de `.article-content` ont volontairement été exclues.

Pages couvertes : accueil, chaussures, raquette débutant, raquette tendinite, règles du padel et confidentialité.

## Paramètres inchangés

Largeur 1350 px, grille principale 2.5fr/1fr, publicités, CSP, URL, sitemap, Wrangler et contenu éditorial.
