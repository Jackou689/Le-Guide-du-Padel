# Pistes d'amélioration (audit du 26 novembre 2026)

## Priorité haute
1. Images propres à chaque article (Open Graph et données structurées). Les 19 pages partagent la même image Open Graph (og-le-guide-du-padel.jpg) et la même image dans le JSON-LD Article. Une image dédiée (1200 × 630 minimum) améliore les partages et l'éligibilité à Google Discover (la balise max-image-preview:large est déjà en place). À faire avec les images des 6 nouveaux articles (prompts à rédiger).
2. Monétisation : les articles n'ont que des emplacements de test ; seule l'accueil contient une vraie balise <ins class="adsbygoogle">. Si l'objectif est des annonces manuelles dans les articles, il faut créer des blocs d'annonces dans AdSense et fournir les identifiants d'emplacement. Sinon, les annonces automatiques suffisent.
3. Maillage interne : liens entrants depuis le contenu des articles : padel-ou-tennis 1, sac-padel-debutant 1, comptage 2, service 2, formes-raquette 2, echauffement 2. Objectif : au moins 3 par article, avec des phrases naturelles.

## Priorité moyenne
4. Contenu : « Combien coûte une partie et comment réserver » (prix à vérifier), comparatif « meilleures raquettes pour débuter » (affiliation), explication des sorties de vitre, padel et enfants. Prioriser avec les requêtes réelles de Search Console (onglet Performances).
5. Liens externes : 38 liens distincts (dont 4 vers ameli.fr). À vérifier à chaque version avec un contrôle automatique.
6. Après mise en production : relancer PageSpeed sur leguidedupadel.fr (l'en-tête noindex n'existe que sur *.workers.dev).

## Vitesse (gains restants, tous modestes)
7. Image principale d'article ≈ 55 à 85 Ko ; police Lora 33 Ko (poids 400/600/700) ; JavaScript AdSense ≈ 150 Ko inutilisé (chargement différé possible, au risque de baisser les revenus : décision à prendre) ; articles.css 136 Ko brut (couche historique, beaucoup de règles redondantes).
8. Durée de cache du CSS et du JS (1 heure) : volontairement non modifiée. Un cache long masquerait les modifications tant que ?v= n'est pas changé, ce qui va à l'encontre de la volonté de voir les erreurs. Gain limité aux visites répétées.
