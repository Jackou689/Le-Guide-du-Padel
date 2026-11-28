# Le Guide du Padel — v6 : journal détaillé (retours sur la v5)

Chaque point suit le même schéma : **Quoi** (ce qui change), **Pourquoi** (ce qui le justifie), **Par quoi** (comment). Le code est dans `v5.css` (section « v6 »), le script de construction a été rejoué sur la v5 sauvegardée, donc tout est reproductible.

## 0. Ta demande → ce qui a été fait
| Demande | Fait | Où |
|---|---|---|
| Garder le vert des titres, mais mieux centrés et mis en valeur | Bandeau arrondi, pastille verte centrée verticalement avec le titre, titre plus grand, filet vert dessous | Section 1 |
| Navigation rapide plus visible | Sommaire « Dans cet article » refait en cartes numérotées | Section 2 |
| Refaire l'encadré « À propos » de la barre latérale | Remplacé par « Votre prochain guide » (3 liens contextuels) ; « Navigation rapide » remplacée par « Tous les guides » | Section 3 |
| Boutons du header de meilleure qualité | Pastilles, bouton vert pour « Par où commencer », état actif | Section 4 |
| Nouvelle palette | Palette « Court Premium » proposée et appliquée aux jetons | Section 5, `palette-court-premium.png` |
| Dates au 10 octobre 2026 sans retirer « Publié par Le Guide du Padel » | Signature datée sur les 8 guides, balisage, sitemap | Section 6 |
| Analyser les plugins et skills nécessaires | Tableau de choix | Section 7 |

## 1. Titres de section
- **Quoi** : chaque titre numéroté devient un bandeau arrondi : pastille verte (chiffre bleu nuit) alignée au centre du titre, titre en Poppins plus grand, filet vert sous le bandeau.
- **Pourquoi** : en v5 le bandeau gardait un fond sombre à angles droits en mode sombre et le texte restait collé en haut, la pastille plus bas. Le vert plaisait, le centrage et la mise en valeur non.
- **Par quoi** : `display:flex; align-items:center` sur le titre, pastille passée de « absolue » à élément de la ligne, fond dégradé par thème, spécificité renforcée (`:not(#v6)`) pour passer devant les anciennes règles du mode sombre.

## 2. Navigation rapide (« Dans cet article »)
- **Quoi** : cartes blanches (ou bleu nuit en sombre) en grille, chacune avec une pastille verte numérotée, le titre de la section et une flèche ; encadré surmonté d'un liseré vert ; en-tête avec icône.
- **Pourquoi** : les pastilles creuses sans relief n'attiraient pas l'œil ; les numéros doivent correspondre à ceux des titres.
- **Par quoi** : numéros écrits dans les liens retirés (4 pages) et remplacés par un compteur CSS ; vérification automatique : le nᵉ lien du sommaire correspond au nᵉ titre sur les 8 guides.

## 3. Barre latérale
- **Quoi** : l'encadré « À propos » est remplacé par **« Votre prochain guide »** : 3 cartes (icône, titre, raison courte, flèche) choisies pour chaque article. « Navigation rapide / Découvrez nos guides » devient **« Tous les guides »** : 8 liens groupés (Matériel, Jouer et progresser, Santé), icônes, page courante surlignée et signalée « Vous êtes ici ». Une ligne finale garde l'accès à « Qui sommes-nous ? ».
- **Pourquoi** : l'ancien encadré n'apportait pas d'information utile ; la liste plate n'attirait pas l'œil. Les nouveaux blocs ajoutent, sur chaque guide, **3 liens contextuels** avec une raison de cliquer (« Votre prochain guide ») en plus de la liste des guides, au lieu d'une liste identique partout et d'un texte « À propos » sans lien utile.
- **Par quoi** : balisage généré par le script ; 8 icônes dessinées en SVG intégrés au CSS (aucun fichier image) ; textes écrits selon les règles de rédaction d'interface (verbe ou bénéfice, une idée par ligne). Les deux « Emplacement test » de la barre latérale sont conservés à leur place.
- Exemples de maillage : Règles → Raquette débutant, Techniques, Tactique ; Tendinite → Échauffement, Raquette débutant, Chaussures ; Échauffement → Raquette et tendinite, Chaussures, Techniques.

## 4. En-tête (boutons de navigation)
- **Quoi** : liens en pastilles (Poppins 500) ; **« Par où commencer »** devient un bouton vert lime à texte bleu nuit ; survol en pastille douce ; la rubrique courante (« Tous les guides » sur un guide, « À propos », « Contact ») a une pastille et un petit trait vert. Menu mobile : même logique, premier lien en bouton vert, flèches à droite, textes lisibles.
- **Pourquoi** : de simples textes bleus gras, sans état de survol ni indication de la page courante.
- **Par quoi** : CSS + attribut `aria-current` sur les liens (lu aussi par les lecteurs d'écran) ; focus clavier conservé ; contraste du bouton vert 9,4:1.

## 5. Nouvelle palette « Court Premium » (voir `palette-court-premium.png`)
Je conserve les couleurs des logos (Nuit #0B2A45, Lime #A7E11D, Brume #F1F5F9) et j'affine l'interface autour :
| Rôle | Avant | Après |
|---|---|---|
| Bleu des liens et actions | #0E5FD8 | **#1A63E0** (5,4:1 sur blanc) |
| Survol des boutons lime | — | **#BEEA45** |
| Petit texte vert sur fond clair | — | **#4B6600** (6,6:1) |
| Accent secondaire (santé, confort) | — | **Aqua #18B6A4** |
| Fond éditorial chaud | — | **Ivoire #FAF8F3** |
| Alertes | divers | **Ambre #F59E0B**, **Corail #E5484D** (icônes et bordures seulement) |
| Fond du mode sombre | #0A1B2D | **#071626** |
| Cartes du mode sombre | #12263D | **#0F2540** |
| Liens en mode sombre | #7DB8FF | **#8CC2FF** |
- **Par quoi** : variables CSS (`--lgp-*`) redéfinies ; tout composant qui les utilise (header, accueil, barre latérale, sommaire) en profite aussitôt.
- **À savoir** : Aqua, Ivoire, Ambre, Corail et Lime texte sont **déclarés mais pas encore appliqués** aux anciens encadrés colorés (astuce, piège, transparence) : c'est l'étape suivante si tu valides la palette.

## 6. Dates et signature
- **Quoi** : « Publié par Le Guide du Padel · le 10 octobre 2026 » sous le titre de **chaque** guide. 3 pages avaient déjà la mention (Règles, Tendinite, Chaussures) : conservée, date ajoutée. 5 pages n'en avaient pas : ajoutée.
- **Pourquoi** : signal de fraîcheur pour les lecteurs et les moteurs, surtout pour les deux guides santé.
- **Par quoi** : balise `<time datetime="2026-10-10">`, `datePublished` et `dateModified` dans les données structurées (Article et WebPage), `article:published_time` et `article:modified_time` pour les réseaux sociaux, `lastmod` dans `sitemap.xml` pour les 8 guides.
- **À savoir** : `dateModified` est identique à la date de publication, comme demandé. À mettre à jour à chaque vraie modification.

## 7. Skills et plugins : analyse du besoin
| Besoin | Skill ou plugin retenu | Ce qu'il a apporté |
|---|---|---|
| Direction visuelle (en-tête, titres, sommaire) | *frontend-design-direction* (ECC), *frontend-design* | Décider d'une direction avant de coder, états des composants, hiérarchie |
| Palette, jetons, cohérence | *design-system* (plugin Design) | Passage par des jetons plutôt que des couleurs en dur, contrôle des contrastes, documentation de la palette |
| Critique des rendus | *design-critique* (plugin Design) | Lecture de tes captures : titres décentrés, sommaire discret |
| Textes de la barre latérale | *ux-copy* (plugin Design) | Intitulés, raisons courtes, « Vous êtes ici » |
| Finitions (survol, zones tactiles, mouvement réduit) | *make-interfaces-feel-better* (ECC) | Zones cliquables, transitions respectant `prefers-reduced-motion` |
| Dates, balisage, sitemap, maillage | *seo* (ECC) | Article daté, `lastmod`, liens contextuels |
| Accessibilité | *accessibility-review* (plugin Design), *accessibility* (ECC) | Contraste, clavier, `aria-current`, noms de liens |
| Non retenus | *SEO/GEO Site Audit* (exige le site en ligne), skills d'animation React, génération d'images | Hors besoin ou impossible ici |

## 8. Vérifications (Chromium)
28 chargements de pages sans erreur ; 703 liens internes valides ; 0 contraste insuffisant (un faux positif connu : texte blanc sur le dégradé bleu nuit de l'encadré « Résumé tactique ») ; focus clavier visible partout ; pas de défilement horizontal à 200 % ; polices chargées sans erreur de console ; en-tête qui se masque et réapparaît ; numéros du sommaire alignés sur les titres ; boutons Amazon, `double.webp` et « Emplacement test » inchangés.

## 9. Reste à faire et points à valider
1. **Palette** : valider ; si oui, je rattache les encadrés colorés historiques aux nouveaux jetons.
2. **Bouton vert « Par où commencer »** : à confirmer (il met l'accent sur le parcours débutant).
3. **Icône « raquette »** de la barre latérale : à cette taille elle ressemble à une loupe ; je peux la redessiner.
4. **Maintenance** : les 3 liens « Votre prochain guide » sont écrits en dur par article ; à mettre à jour quand un guide s'ajoute.
5. **Inchangé depuis la v5** : images (liste dans `CHANGELOG-V5.md`, section 8), droits des images, vérification des produits, mentions légales, Cloudflare, AdSense, réécriture de lisibilité.

## Détail automatique par page

#### `regles-padel.html`
- Version du CSS passée à 2026-6 (cache)
- En-tête : « Tous les guides » signalé comme page/rubrique courante (aria-current) pour l'état actif du menu
- Barre latérale : encadré « À propos » remplacé par « Votre prochain guide » (3 liens contextuels avec raison) ; « Navigation rapide / Découvrez nos guides » remplacé par « Tous les guides » (8 liens groupés avec icônes, page courante signalée, lien « Qui sommes-nous ? »). Emplacements publicitaires inchangés
- Signature : « Publié par Le Guide du Padel » conservée, date « 10 octobre 2026 » ajoutée
- Balises Open Graph article:published_time et article:modified_time = 2026-10-10
- Données structurées : datePublished et dateModified = 2026-10-10 (Article et WebPage)

#### `techniques-padel.html`
- Version du CSS passée à 2026-6 (cache)
- En-tête : « Tous les guides » signalé comme page/rubrique courante (aria-current) pour l'état actif du menu
- Barre latérale : encadré « À propos » remplacé par « Votre prochain guide » (3 liens contextuels avec raison) ; « Navigation rapide / Découvrez nos guides » remplacé par « Tous les guides » (8 liens groupés avec icônes, page courante signalée, lien « Qui sommes-nous ? »). Emplacements publicitaires inchangés
- Sommaire « Dans cet article » : numéros écrits retirés des liens (numérotation par compteur CSS, identique aux pastilles des titres)
- Signature ajoutée sous le titre : « Publié par Le Guide du Padel le 10 octobre 2026 » (cette page n'en avait pas)
- Balises Open Graph article:published_time et article:modified_time = 2026-10-10
- Données structurées : datePublished et dateModified = 2026-10-10 (Article et WebPage)

#### `tactique-filet.html`
- Version du CSS passée à 2026-6 (cache)
- En-tête : « Tous les guides » signalé comme page/rubrique courante (aria-current) pour l'état actif du menu
- Barre latérale : encadré « À propos » remplacé par « Votre prochain guide » (3 liens contextuels avec raison) ; « Navigation rapide / Découvrez nos guides » remplacé par « Tous les guides » (8 liens groupés avec icônes, page courante signalée, lien « Qui sommes-nous ? »). Emplacements publicitaires inchangés
- Sommaire « Dans cet article » : numéros écrits retirés des liens (numérotation par compteur CSS, identique aux pastilles des titres)
- Signature ajoutée sous le titre : « Publié par Le Guide du Padel le 10 octobre 2026 » (cette page n'en avait pas)
- Balises Open Graph article:published_time et article:modified_time = 2026-10-10
- Données structurées : datePublished et dateModified = 2026-10-10 (Article et WebPage)

#### `raquette-debutant.html`
- Version du CSS passée à 2026-6 (cache)
- En-tête : « Tous les guides » signalé comme page/rubrique courante (aria-current) pour l'état actif du menu
- Barre latérale : encadré « À propos » remplacé par « Votre prochain guide » (3 liens contextuels avec raison) ; « Navigation rapide / Découvrez nos guides » remplacé par « Tous les guides » (8 liens groupés avec icônes, page courante signalée, lien « Qui sommes-nous ? »). Emplacements publicitaires inchangés
- Sommaire « Dans cet article » : numéros écrits retirés des liens (numérotation par compteur CSS, identique aux pastilles des titres)
- Signature ajoutée sous le titre : « Publié par Le Guide du Padel le 10 octobre 2026 » (cette page n'en avait pas)
- Balises Open Graph article:published_time et article:modified_time = 2026-10-10
- Données structurées : datePublished et dateModified = 2026-10-10 (Article et WebPage)

#### `raquette-tendinite.html`
- Version du CSS passée à 2026-6 (cache)
- En-tête : « Tous les guides » signalé comme page/rubrique courante (aria-current) pour l'état actif du menu
- Barre latérale : encadré « À propos » remplacé par « Votre prochain guide » (3 liens contextuels avec raison) ; « Navigation rapide / Découvrez nos guides » remplacé par « Tous les guides » (8 liens groupés avec icônes, page courante signalée, lien « Qui sommes-nous ? »). Emplacements publicitaires inchangés
- Signature : « Publié par Le Guide du Padel » conservée, date « 10 octobre 2026 » ajoutée
- Balises Open Graph article:published_time et article:modified_time = 2026-10-10
- Données structurées : datePublished et dateModified = 2026-10-10 (Article et WebPage)

#### `balles-padel.html`
- Version du CSS passée à 2026-6 (cache)
- En-tête : « Tous les guides » signalé comme page/rubrique courante (aria-current) pour l'état actif du menu
- Barre latérale : encadré « À propos » remplacé par « Votre prochain guide » (3 liens contextuels avec raison) ; « Navigation rapide / Découvrez nos guides » remplacé par « Tous les guides » (8 liens groupés avec icônes, page courante signalée, lien « Qui sommes-nous ? »). Emplacements publicitaires inchangés
- Sommaire « Dans cet article » : numéros écrits retirés des liens (numérotation par compteur CSS, identique aux pastilles des titres)
- Signature ajoutée sous le titre : « Publié par Le Guide du Padel le 10 octobre 2026 » (cette page n'en avait pas)
- Balises Open Graph article:published_time et article:modified_time = 2026-10-10
- Données structurées : datePublished et dateModified = 2026-10-10 (Article et WebPage)

#### `chaussures-padel.html`
- Version du CSS passée à 2026-6 (cache)
- En-tête : « Tous les guides » signalé comme page/rubrique courante (aria-current) pour l'état actif du menu
- Barre latérale : encadré « À propos » remplacé par « Votre prochain guide » (3 liens contextuels avec raison) ; « Navigation rapide / Découvrez nos guides » remplacé par « Tous les guides » (8 liens groupés avec icônes, page courante signalée, lien « Qui sommes-nous ? »). Emplacements publicitaires inchangés
- Signature : « Publié par Le Guide du Padel » conservée, date « 10 octobre 2026 » ajoutée
- Balises Open Graph article:published_time et article:modified_time = 2026-10-10
- Données structurées : datePublished et dateModified = 2026-10-10 (Article et WebPage)

#### `echauffement-padel.html`
- Version du CSS passée à 2026-6 (cache)
- En-tête : « Tous les guides » signalé comme page/rubrique courante (aria-current) pour l'état actif du menu
- Barre latérale : encadré « À propos » remplacé par « Votre prochain guide » (3 liens contextuels avec raison) ; « Navigation rapide / Découvrez nos guides » remplacé par « Tous les guides » (8 liens groupés avec icônes, page courante signalée, lien « Qui sommes-nous ? »). Emplacements publicitaires inchangés
- Signature ajoutée sous le titre : « Publié par Le Guide du Padel le 10 octobre 2026 » (cette page n'en avait pas)
- Balises Open Graph article:published_time et article:modified_time = 2026-10-10
- Données structurées : datePublished et dateModified = 2026-10-10 (Article et WebPage)

