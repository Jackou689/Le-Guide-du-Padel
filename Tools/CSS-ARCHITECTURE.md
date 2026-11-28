# Architecture CSS (v20)

- **style.css** : socle commun à TOUTES les pages (accueil comprise) : polices, variables, en-tête, menu, pied de page, composants de l'accueil, lisibilité des articles. Seul fichier chargé par l'accueil.
- **articles.css** : couche historique des pages intérieures (articles, contact, mentions, 404). Chargé AVANT style.css (style.css corrige et complète).
- Ordre de chargement sur les pages intérieures : articles.css puis style.css. Ne pas l'inverser.
- Où ajouter une règle ? Composant utilisé par toutes les pages ou par l'accueil : style.css. Composant propre aux articles : style.css si c'est un correctif récent (bloc « v10 » et suivants), articles.css si c'est un complément de la couche historique. Une règle ne vit qu'à un seul endroit : aucune duplication à synchroniser.
- Après toute modification d'un des deux fichiers : changer le numéro ?v= dans les pages (les deux liens) pour invalider le cache.
- <picture> est transparent (display:contents) : il n'affecte pas la mise en page.
