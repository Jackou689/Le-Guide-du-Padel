# Tests d’acceptation du lot 9B

## 9B-01 Cache et scripts
- 14 pages chargent `style.css?v=9B`.
- 14 pages chargent `script.js?v=9B`.
- Le script local porte l’attribut `defer`.

## 9B-02 Images et stabilité
- Toutes les images locales ont des attributs `width` et `height`.
- Toutes les images ont une stratégie de décodage explicite.
- Les images principales ne sont pas chargées en lazy.
- Les images secondaires restent chargées en lazy lorsque prévu.

## 9B-03 SEO
- 13 pages indexables avec canoniques uniques.
- 404 en `noindex, follow` sans canonique.
- Titres et descriptions présents.
- Open Graph et JSON-LD présents sur les pages indexables.
- Sitemap et robots.txt valides.

## 9B-04 Non-régression
- Aucun lien interne cassé.
- Aucun actif local manquant.
- Aucun lien Amazon non conforme.
- Aucun débordement horizontal à 1440, 768, 390 et 320 px.
- Menu, thème et filtres fonctionnels.
