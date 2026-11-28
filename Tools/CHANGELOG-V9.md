# Le Guide du Padel — v9 : journal détaillé

Schéma : **Quoi**, **Pourquoi**, **Par quoi**. Cette version reprend les correctifs de l'audit (`AUDIT-SITE-V8.md`) qui ne dépendent pas de tes images ni de tes informations.

## 1. Skills et plugins utilisés
| Chantier | Skill ou plugin |
|---|---|
| Formulations et balisage | *seo* (ECC) |
| Vérifications finales | *browser-qa* (ECC) |
| Suivi des corrections | *production-audit* (ECC) |
Aucun nouveau plugin n'était nécessaire pour ces correctifs.

## 2. Corrections
- **Descriptions du site** — *Quoi* : « la prévention des blessures » et « la prévention au padel » deviennent « l'échauffement ». *Pourquoi* : même principe que pour l'article tendinite, ne rien promettre de préventif ; l'aperçu servait encore l'ancienne formule dans la description de l'accueil et dans les données structurées. *Par quoi* : 14 pages (métadonnées, Open Graph, Twitter, JSON-LD).
- **Éditeur du site** — *Quoi* : un nœud `Organization` (nom, adresse web, logo) est ajouté à l'accueil et rattaché au `WebSite` comme éditeur. *Pourquoi* : l'éditeur n'existait que dans le balisage `Article` ; c'est un signal de confiance pour Google et pour les moteurs à réponses générées. *Par quoi* : JSON-LD de `index.html`. Il manque toujours le nom d'un auteur ou d'un relecteur (information à fournir).
- **Maillage dans le texte** — *Quoi* : 2 liens contextuels (« smash » dans Raquette débutant vers Techniques, « placement » dans Balles vers Tactique). *Pourquoi* : l'audit signalait peu de liens vers Tactique, Techniques et Tendinite. *Par quoi* : je n'en ai pas ajouté davantage : chaque guide renvoie déjà vers les guides pertinents, et d'autres liens auraient été artificiels (par exemple « tête de raquette » vers le choix de la raquette). Les cartes « Votre prochain guide » de la barre latérale ajoutent déjà 3 liens contextuels par page.
- **`llms.txt`** — *Quoi* : fichier décrivant le site et ses 8 guides pour les assistants d'IA. *Pourquoi* : recommandation de l'audit (visibilité dans les moteurs à réponses générées). *Par quoi* : généré à partir des vrais titres et descriptions des pages.

## 3. Correction de mon audit
L'audit signalait deux sauts de niveau de titre (Chaussures, Tendinite). C'était un **faux positif** : les titres de modèles de ces pages portent `role="heading"` et `aria-level="3"`, donc il n'y a pas de saut pour un lecteur d'écran. Je ne les ai pas modifiés (changer la balise aurait cassé leur style).

## 4. Vérifications
28 chargements de pages sans erreur ni débordement, polices chargées sans erreur, 705 liens internes valides, JSON-LD valide sur toutes les pages, plus aucune mention de « prévention » dans les en-têtes des pages.

## 5. Restent à traiter
Images (3 reçues : 2 à intégrer, 1 à refaire, 8 attendues) · droits des images et produits · politique de confidentialité (droits des personnes) · hauteur réservée aux annonces AdSense · 35 fichiers inutilisés · CSS (parties non utilisées, `!important`) · lisibilité de 3 guides · auteur ou relecteur pour les guides santé.
