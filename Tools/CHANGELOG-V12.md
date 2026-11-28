# Changelog v12 (20 novembre 2026)

## Rétabli
- Longueur de ligne des articles : retour à l'ancienne largeur (suppression du plafond `--v10-measure`). Les autres réglages de lisibilité (corps 18 px sur ordinateur, interligne, libellés ≥ 12 px) sont conservés.

## Nouveaux articles (règlement FIP, application au 1er janvier 2026)
- `/comptage-points-padel` : 15-30-40, avantage / point en or / Star Point, sets, tie-break, mini-set, super tie-break, changements de côté, FAQ.
- `/service-padel` : placement (ligne de service), geste, fautes, filet et let, ordre de service, relance, conseils, FAQ.
- Ajoutés au menu, à la barre latérale « Tous les guides », au pied de page et au sitemap. Pas encore sur l'accueil (cartes avec images à venir).
- Pas d'image dans ces deux articles pour l'instant (à produire dans le style crayon/encre validé).

## Correction dans « Règles du padel » (regles-padel)
- ERREUR CORRIGÉE : le serveur ne se place pas derrière la ligne de fond mais derrière la ligne de service (6,95 m du filet).
- Dragonne : lâcher la raquette ou casser la dragonne fait perdre le point (règlement FIP).
- Égalité : les trois options FIP (avantage, point en or, Star Point) remplacent la mention « point en or très souvent appliqué ».
- Liens vers les deux nouveaux guides ; bloc « À lire ensuite » mis à jour ; date de mise à jour 20 novembre 2026 ; source FIP (PDF) ajoutée.

## PageSpeed (aperçu workers.dev)
- « L'indexation de la page est bloquée » (x-robots-tag: noindex) : en-tête ajouté par Cloudflare sur les adresses *.workers.dev, pas par le site (`_headers` n'en contient pas). À re-tester sur leguidedupadel.fr une fois en production.
- « Ancien JavaScript » (10 Kio) : uniquement `static.cloudflareinsights.com/beacon.min.js` (script Cloudflare Web Analytics, polyfills Array.prototype.at / findLast). Le code du site n'est pas en cause.
