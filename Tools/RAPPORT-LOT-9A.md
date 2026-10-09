# Rapport du lot 9A

## Objet
Recette fonctionnelle de la base 8E.6, sans reprise des détails esthétiques reportés.

## Anomalie corrigée
Deux images héro externes servies par Unsplash renvoyaient HTTP 403 dans Chromium :
- chaussures-padel-guide.html ;
- raquette-padel-tendinite.html.

Les deux URL externes ont été remplacées par les images locales responsives déjà incluses dans l’archive. Cette correction supprime une dépendance réseau et ne modifie ni le contenu, ni la structure, ni l’identité visuelle des pages.

## Résultats
- 14 pages testées ;
- 56 combinaisons page/largeur contrôlées à 1440, 768, 390 et 320 px ;
- menu mobile, thème persistant et filtres d’accueil validés ;
- zéro débordement horizontal ;
- zéro lien interne cassé ;
- zéro actif local manquant ;
- zéro lien Amazon non conforme ;
- zéro image locale invalide ;
- zéro identifiant dupliqué ;
- zéro bouton sans nom accessible ;
- JavaScript et audit 8E validés.

## Points non testables hors Cloudflare
Le statut HTTP réel de la page 404, les redirections automatiques sans extension et les en-têtes HTTP doivent être confirmés sur une preview Cloudflare, car un serveur statique local ne reproduit pas le moteur Assets de Cloudflare.

## Décision
Lot 9A accepté. Cette version devient la base pour le lot 9B.

## Versionnement des ressources statiques
Toutes les pages chargent désormais :
- `style.css?v=9A` ;
- `script.js?v=9A`.

Ce changement force les navigateurs à demander les ressources de la version 9A au lieu de réutiliser une ancienne copie associée à une URL identique. Les règles actuelles de cache de 3 600 secondes pour le CSS et le JavaScript sont conservées.
