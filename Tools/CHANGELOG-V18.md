# Changelog v18 (25 novembre 2026)

## Replis retirés (demande : voir les erreurs plutôt que les masquer)
- script.js : le bloc « repli AVIF » est supprimé (retour à la taille d'origine, 5,7 Ko). Si un fichier .avif est introuvable, l'image apparaît cassée et la requête 404 est visible (testé).
- style.css : @font-face en WOFF2 uniquement, sans WOFF de secours. Les 3 anciens fichiers .woff sont supprimés du projet.
- Conservé : l'image WebP/JPEG à l'intérieur de <picture>. Ce n'est pas un mécanisme de masquage d'erreur : c'est le format que les navigateurs sans AVIF (anciens Safari, notamment) utilisent normalement.
- Conservé : les logos allégés sous leurs anciens noms de fichier (pas de code de repli).

## Cache
- style.css et script.js passent à ?v=2026-13 dans toutes les pages.

## Vérification
- 19 pages × (ordinateur clair, ordinateur sombre, mobile) : 0 requête en erreur, 0 image cassée, 0 débordement.

## À téléverser : voir Tools/FICHIERS-V18.txt
