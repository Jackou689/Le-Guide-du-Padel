# Tests d’acceptation du lot 9A

## 9A-01 Structure et navigation
- 14 pages HTML présentes, dont la page 404.
- Aucun lien interne cassé et aucun actif local manquant.
- 13 URL canoniques uniques et sitemap XML valide.

## 9A-02 JavaScript
- Syntaxe du fichier script.js valide.
- Bascule clair/sombre fonctionnelle et persistante après rechargement.
- Menu mobile ouvrable, refermable, fermé par Échap et doté d’un piège de focus.
- Filtres de catégories de l’accueil fonctionnels pour toutes les catégories.

## 9A-03 Responsive
- Contrôles à 1440, 768, 390 et 320 px.
- Aucun débordement horizontal global.
- Une balise h1 unique sur chaque page.

## 9A-04 Médias
- Tous les fichiers images locaux sont décodables.
- Toutes les images possèdent un texte alternatif.
- Les deux images Unsplash renvoyant HTTP 403 ont été remplacées par les variantes locales responsives déjà présentes.

## 9A-05 Accessibilité fonctionnelle
- Aucun identifiant HTML dupliqué.
- Aucun tabindex positif.
- Aucun bouton sans nom accessible.
- Focus visible conservé.

## 9A-06 Publicité et affiliation
- Les placeholders sont masqués hors preview et visibles uniquement en local ou sur workers.dev.
- AdSense reste inactif.
- Tous les liens Amazon détectés portent nofollow sponsored.

## Condition de recette
Le lot 9A est accepté si tous les contrôles ci-dessus passent et si aucun changement esthétique non requis n’est introduit.

## 9A-07 Versionnement du cache
- Les 14 pages référencent exactement `style.css?v=9A`.
- Les 14 pages référencent exactement `script.js?v=9A`.
- Aucun lien vers les anciennes URL non versionnées n’est conservé dans les pages HTML.
