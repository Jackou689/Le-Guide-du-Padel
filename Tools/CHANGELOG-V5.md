# Le Guide du Padel — Refonte v5 : journal détaillé des changements

Chaque changement est décrit en trois temps : **Quoi** (ce qui change), **Pourquoi** (ce qui le justifie), **Par quoi** (comment / avec quoi). Les skills et plugins utilisés : *frontend-design*, *accessibility* et *make-interfaces-feel-better* (ECC), *accessibility-review*, *design-critique* et *ux-copy* (plugin Design), *seo* et *article-writing* (ECC). Le skill d'audit SEO/GEO (plugin SEO) exige le site en ligne et ses propres scripts : à lancer après déploiement.

## 0. Tes consignes, vérifiées par comparaison v4 → v5
| Consigne | Vérification |
|---|---|
| Ne pas toucher à `double.webp` (Tactique) | Fichier identique octet pour octet à la v4, toujours affiché en tête de l'article. |
| Laisser les « Emplacement test » | Conservés à l'identique (1 sur l'accueil, 5 sur Règles, etc.). À vérifier après déploiement en production qu'ils n'apparaissent plus. |
| Ne pas changer les boutons « Disponible sur amazon » | Contenu des boutons identique sur les 14 pages (comparaison automatique). Seuls leur gabarit (hauteur minimale 56 px, coins arrondis à 12 px, largeur maximale 340 px, centrage) et ce qui les entoure (cartes, grilles, notes) changent. |
| Tendinite : garder l'effet médical, ne pas promettre la sûreté | Contexte médical, encadré santé et sources conservés. Les promesses (« protéger », « soulager », « anti-tendinite », « non négociables », « parfaite », « les plus… du marché », « garantissent ») sont remplacées par des formulations mesurées (« ménager », « à privilégier », « visent », « pensée pour »), et une phrase explicite de non-garantie est ajoutée. |

## 1. Identité et design : ce que j'ai décidé
Je n'ai **pas** refait les logos ni la palette : ils sont validés et déjà dans l'en-tête, la favicon et les réseaux. J'ai fait évoluer le **système visuel** autour d'eux (typographie, rythme, composants) pour un rendu plus éditorial et plus premium. Tout est dans un seul fichier, `v5.css`, chargé après `redesign.css`, donc réversible en le retirant.

| Quoi | Pourquoi | Par quoi |
|---|---|---|
| Titres en **Poppins** (500/700), accueil et articles | Les titres dépendaient de la police du système (rendu différent selon l'appareil) ; Poppins est géométrique, moderne, cohérent avec le « Style Moderne » validé. | Polices hébergées localement (`/fonts`, sous-ensemble latin en WOFF, 60 Ko au total, licence OFL), `font-display: swap`, préchargement de Poppins 700. Compatible avec la politique de sécurité du site (ressources du même domaine). |
| Phrases d'ouverture et phrases mises en avant en **Lora** | Elles s'affichaient en Times (police serif demandée mais jamais chargée), ce qui détonnait. | Lora variable hébergée localement, appliquée au chapô de chaque article et aux classes `editorial-emphasis`, `impact-word`, `editorial-serif`. |
| Titres de section : pastille bleu nuit à chiffre vert + filet vert | Chaque section avait un bandeau pastel d'une couleur différente (aspect « carnaval ») et le chiffre apparaissait deux fois (pastille + texte). | Un seul gabarit, couleurs de marque ; le chiffre vient du compteur CSS. 37 numéros écrits en double retirés du texte des titres. Mode sombre : pastille verte, chiffre bleu nuit. |
| Sommaire en pastilles blanches bordées | Pastilles de couleurs variées, difficiles à lire. | `v5.css` section 6. |
| Encadrés, modules, cartes de section : mêmes rayons et ombres | Chaque page avait ses rayons, ses ombres et ses barres de couleur. | Rayon 16–18 px, ombre douce unique, bordure fine ; barres de couleur retirées des cartes de section (balles, techniques, échauffement). |
| Tableaux | Rendu inégal selon la page. | En-tête bleu nuit, lignes alternées, coins arrondis, mode sombre géré. |
| Cartes produit : grille régulière | Raquette débutant : 4 produits sur 3 colonnes (une carte orpheline) ; photos de tailles très différentes, agrandies donc floues (ex. 189 px étirés à 280 px). | Grille 2 × 2 (1 colonne sur mobile), images contenues dans une hauteur de 170 px sans agrandissement, cartes tendinite/chaussures en grille auto avec liseré vert, étiquette « choix de la rédaction » en pastille. |
| Boutons Amazon : gabarit uniquement | Demande : ne pas modifier le bouton lui-même. | Hauteur minimale, rayon, largeur maximale et centrage ; aucun changement de texte, de couleur ni de marque. |
| Visuels d'étapes (échauffement) | Images de 310 px à côté d'un grand vide ; étiquette « Étape en image » sans valeur. | Disposition 2 colonnes (image environ 54 % de la largeur, légende à droite), 1 colonne sur mobile ; 4 étiquettes retirées du HTML. |
| Barres latérales : puces vertes à la place des emojis | Emojis rendus différemment selon l'appareil, bruit visuel, lus à voix haute. | 82 emojis retirés du site (titres, boutons, liens) ; puce CSS verte. |
| Illustration « PADEL SHOTS » (techniques) contenue à sa taille réelle | Fichier de 595 px étiré à 857 px (flou). | Largeur maximale 595 px, centrée (en attendant une nouvelle image). |
| Mouvements réduits | Respect de la préférence système. | Les effets de survol sont dans `prefers-reduced-motion: no-preference`. |

## 2. Changements communs aux 14 pages
| Quoi | Pourquoi | Par quoi |
|---|---|---|
| Ajout de `v5.css` et préchargement de la police | Charger la couche de design et éviter un saut de police sur les titres. | Deux balises dans l'en-tête de chaque page, version `?v=2026-5` pour contourner le cache. |
| Chemins d'images et de liens relatifs → absolus | `images/…` et `href="raquette-debutant"` fonctionnent seulement à la racine ; une URL avec barre finale les casserait. | 95 liens internes et tous les `src`/`srcset` d'images passés en `/…`. |
| « Prévention tendinite » → « Raquette et tendinite » (menus, pieds de page, barres latérales) | « Prévention » promettait un effet préventif. | Remplacement sur les 14 pages. |
| Emojis supprimés (82) | Voir ci-dessus. | Retrait ciblé en début de texte. |

## 3. Article par article
### Règles du padel
- **Photo d'ouverture** : `padel.webp` était un aperçu filigrané de la banque d'images MEGAPIXL (filigrane en diagonale + bandeau MEGAPIXL dans le fichier). Remplacée par `hero-court-v16.webp` (photo propre du site, 3 tailles responsives). Les deux fichiers filigranés sont déplacés dans `Tools/a-verifier-droits/` (non déployés, non supprimés). **Provisoire** en attendant ta nouvelle image.
- **Numérotation** : la pastille indiquait « 4 » alors que le titre commençait par « 5. » : numéro retiré du titre et du sommaire.
- **Sources** : bloc « Sources officielles » ajouté (lien FIP déjà utilisé sur l'article des balles ; aucune nouvelle adresse inventée).
- **Liens internes** : « lober » → Techniques ; « balles » → Balles.

### Techniques
- Numéros en double retirés des titres ; illustration d'ouverture contenue ; lien « balles » → Balles ; typographie et cartes harmonisées.

### Tactique au filet
- **Sommaire en double** : la page avait deux sommaires (un stylé, un non stylé qui s'affichait en texte collé) et deux repères `<nav>` de même nom. On garde le stylé, on retire l'autre.
- `double.webp` inchangé. Liens « bandeja » et « volée » → Techniques.

### Raquette débutant
- **Cartes** : grille 2 × 2, noms accessibles uniques (avant : 4 liens au nom identique pour un lecteur d'écran), textes alternatifs précisés.
- **Encart de transparence** : « Comment lire cette sélection » (exemples, ni classement ni test, prix indicatifs).
- **FAQ** : 5 questions (budget, forme, poids, essai, prix) dont les réponses reprennent des informations déjà présentes dans l'article ; section ajoutée au sommaire. +260 mots environ.
- Lien « coude » → Raquette et tendinite.

### Raquette et tendinite
- Réécriture mesurée détaillée en section 0 ; titre : « …pour ménager son coude ? ».
- Emoji ❌ retiré, boutons « L'échauffement parfait » → « L'échauffement en 10 min » et « Étape suivante : Prévenir les blessures » → « …mieux préparer son corps ».
- Encadré santé : « Aucune raquette ne peut garantir l'absence de douleur ou de blessure. »
- 3 cartes modèles en grille régulière, noms accessibles uniques ; lien « échauffer » → Échauffement.

### Balles
- Titre raccourci (67 → moins de 60 caractères) : suffixe de marque retiré du titre et des balises sociales ; numéros en double retirés ; lien « règles » → Règles.

### Chaussures
- **H1** aligné sur la requête : « Chaussures de padel : comment bien choisir (et pourquoi éviter le running) ».
- **3 sections ajoutées** (pointure et ajustement, quand changer ses chaussures, questions fréquentes), rédigées prudemment et sans chiffre inventé : environ 1 000 → 1 300 mots.
- Bouton « Prévention : Éviter la Tendinite » → « Guide : Raquette et tendinite ».

### Échauffement
- 4 étiquettes « Étape en image » retirées ; visuels d'étapes agrandis.

### Détail automatique des modifications par page

#### Règles du padel (`regles-padel.html`)
- Ajout de v5.css (couche éditoriale) et préchargement de la police Poppins 700
- 13 emoji(s) retiré(s) des titres, boutons et liens
- Chemins d'images relatifs (images/…) convertis en absolus (/images/…)
- 12 lien(s) interne(s) relatif(s) convertis en absolus
- Libellé « Prévention tendinite » remplacé par « Raquette et tendinite » (3x)
- 1 titre(s) de section : numéro écrit en double retiré (la pastille le porte déjà)
- Sommaire : « 5. » retiré (la pastille du titre affichait 4 : numérotation incohérente)
- Photo d'ouverture : aperçu filigrané MEGAPIXL (padel.webp) remplacé par hero-court-v16.webp (photo propre du site)
- Bloc « Sources officielles » ajouté (lien FIP déjà utilisé sur le guide des balles)
- Lien interne contextuel : « balles » -> /balles-padel
- Lien interne contextuel : « lober » -> /techniques-padel
- Données structurées : nœud Article ajouté (auteur et éditeur = Le Guide du Padel ; dates volontairement absentes, à fournir)

#### Techniques (`techniques-padel.html`)
- Ajout de v5.css (couche éditoriale) et préchargement de la police Poppins 700
- 8 emoji(s) retiré(s) des titres, boutons et liens
- Chemins d'images relatifs (images/…) convertis en absolus (/images/…)
- 11 lien(s) interne(s) relatif(s) convertis en absolus
- Libellé « Prévention tendinite » remplacé par « Raquette et tendinite » (3x)
- 15 titre(s) de section : numéro écrit en double retiré (la pastille le porte déjà)
- Lien interne contextuel : « balles » -> /balles-padel
- Données structurées : nœud Article ajouté (auteur et éditeur = Le Guide du Padel ; dates volontairement absentes, à fournir)

#### Tactique au filet (`tactique-filet.html`)
- Ajout de v5.css (couche éditoriale) et préchargement de la police Poppins 700
- 8 emoji(s) retiré(s) des titres, boutons et liens
- Chemins d'images relatifs (images/…) convertis en absolus (/images/…)
- 11 lien(s) interne(s) relatif(s) convertis en absolus
- Libellé « Prévention tendinite » remplacé par « Raquette et tendinite » (3x)
- 7 titre(s) de section : numéro écrit en double retiré (la pastille le porte déjà)
- Sommaire en double supprimé : on garde le sommaire stylé de la page (tactics-jump-nav) et on retire la copie non stylée (editorial-jump-nav), qui s'affichait en texte collé ; fin des deux repères <nav> de même nom
- Lien interne contextuel : « volée » -> /techniques-padel
- Lien interne contextuel : « bandeja » -> /techniques-padel
- Données structurées : nœud Article ajouté (auteur et éditeur = Le Guide du Padel ; dates volontairement absentes, à fournir)

#### Raquette débutant (`raquette-debutant.html`)
- Ajout de v5.css (couche éditoriale) et préchargement de la police Poppins 700
- 11 emoji(s) retiré(s) des titres, boutons et liens
- Chemins d'images relatifs (images/…) convertis en absolus (/images/…)
- 12 lien(s) interne(s) relatif(s) convertis en absolus
- Libellé « Prévention tendinite » remplacé par « Raquette et tendinite » (3x)
- 4 titre(s) de section : numéro écrit en double retiré (la pastille le porte déjà)
- 4 cartes produit : nom accessible unique par lien (avant : 4 liens au nom identique)
- Alt des images produit plus précis
- Encart « Comment lire cette sélection » (transparence : exemples, ni classement ni test, prix indicatifs)
- Section « Questions fréquentes » ajoutée (5 questions, réponses fondées sur le contenu déjà présent dans l'article) + entrée au sommaire
- Lien interne contextuel : « coude » -> /raquette-tendinite
- Données structurées : nœud Article ajouté (auteur et éditeur = Le Guide du Padel ; dates volontairement absentes, à fournir)

#### Raquette et tendinite (`raquette-tendinite.html`)
- Ajout de v5.css (couche éditoriale) et préchargement de la police Poppins 700
- 13 emoji(s) retiré(s) des titres, boutons et liens
- Chemins d'images relatifs (images/…) convertis en absolus (/images/…)
- 11 lien(s) interne(s) relatif(s) convertis en absolus
- Libellé « Prévention tendinite » remplacé par « Raquette et tendinite » (3x)
- Titre : « protéger son coude » -> « ménager son coude » (H1, fil d'Ariane, données structurées)
- Introduction : « finissent par enflammer » -> « peuvent, avec le temps, irriter » (effet médical conservé, formulation non absolue)
- Titre 1 : « L'erreur qui aggrave la douleur » -> « Le piège à éviter » (emoji ❌ retiré)
- Paragraphe diamant : « effet de levier énorme / fuyez » -> formulation mesurée
- Titre 2 : « obligatoires / anti-tendinite » -> « à privilégier / plus confortable pour le bras »
- Introduction des critères : « soulager / non-négociables » -> « ménager / à privilégier, sans garantie »
- Critère poids : « impérativement » -> « plutôt »
- Titre 3 : « pour soulager votre bras » -> « orientés confort pour le bras »
- Sélection : « respectant strictement » -> « d'après leurs caractéristiques annoncées »
- Head Zephyr : superlatif « les plus maniables et douces du marché » retiré
- Dunlop : « garantissent / préserve » -> « visent / ménager »
- Adidas Match Light : « Parfaite pour » -> « Pensée pour »
- Résumé : « règles d'or contre la tendinite » -> « 3 repères pour ménager son coude »
- Résumé : impératifs (« ne négligez jamais », « surtout », « toujours ») remplacés + phrase explicite « sans garantir l'absence de douleur »
- Bloc « Étape suivante » : « Prévenir les blessures » -> « mieux préparer son corps »
- Encadré « Information santé » : phrase ajoutée « Aucune raquette ne peut garantir l'absence de douleur ou de blessure »
- 3 cartes modèles : nom accessible unique par lien Amazon
- Bouton « L'échauffement parfait » -> « L'échauffement en 10 min » (superlatif retiré)
- Lien interne contextuel : « échauffer » -> /echauffement-padel
- Données structurées : nœud Article ajouté (auteur et éditeur = Le Guide du Padel ; dates volontairement absentes, à fournir)

#### Balles (`balles-padel.html`)
- Ajout de v5.css (couche éditoriale) et préchargement de la police Poppins 700
- 8 emoji(s) retiré(s) des titres, boutons et liens
- Chemins d'images relatifs (images/…) convertis en absolus (/images/…)
- 11 lien(s) interne(s) relatif(s) convertis en absolus
- Libellé « Prévention tendinite » remplacé par « Raquette et tendinite » (3x)
- 10 titre(s) de section : numéro écrit en double retiré (la pastille le porte déjà)
- Titre de page raccourci : suffixe « | Le Guide du Padel » retiré (1x : title, og:title…) ; avant 67 caractères, désormais sous 60
- Lien interne contextuel : « règles » -> /regles-padel
- Données structurées : nœud Article ajouté (auteur et éditeur = Le Guide du Padel ; dates volontairement absentes, à fournir)

#### Chaussures (`chaussures-padel.html`)
- Ajout de v5.css (couche éditoriale) et préchargement de la police Poppins 700
- 13 emoji(s) retiré(s) des titres, boutons et liens
- Chemins d'images relatifs (images/…) convertis en absolus (/images/…)
- 12 lien(s) interne(s) relatif(s) convertis en absolus
- Libellé « Prévention tendinite » remplacé par « Raquette et tendinite » (3x)
- H1 aligné sur la requête « chaussures de padel » (avant : formulation négative, en décalage avec le titre de page)
- 3 sections ajoutées (pointure et ajustement, quand changer ses chaussures, questions fréquentes) + 3 entrées au sommaire : l'article passe d'environ 1 000 à environ 1 300 mots
- Bouton « Prévention : Éviter la Tendinite » -> « Guide : Raquette et tendinite » (ne promet plus d'éviter une tendinite)
- Données structurées : nœud Article ajouté (auteur et éditeur = Le Guide du Padel ; dates volontairement absentes, à fournir)

#### Échauffement (`echauffement-padel.html`)
- Ajout de v5.css (couche éditoriale) et préchargement de la police Poppins 700
- 8 emoji(s) retiré(s) des titres, boutons et liens
- Chemins d'images relatifs (images/…) convertis en absolus (/images/…)
- 11 lien(s) interne(s) relatif(s) convertis en absolus
- Libellé « Prévention tendinite » remplacé par « Raquette et tendinite » (3x)
- 4 étiquettes « Étape en image » retirées (texte sans valeur, lu à voix haute par les lecteurs d'écran)
- Données structurées : nœud Article ajouté (auteur et éditeur = Le Guide du Padel ; dates volontairement absentes, à fournir)

## 4. SEO, accessibilité, performance
- **Données structurées** : nœud `Article` ajouté aux 8 guides (titre, description, image, auteur et éditeur = Le Guide du Padel, logo). Les **dates sont volontairement absentes** : je n'en invente pas.
- **FAQPage** : volontairement non ajouté. Google en réserve l'affichage enrichi à de rares sites (publics, santé), l'effort de maintenance n'en vaut pas la peine.
- **Accessibilité** (skill accessibility-review) : 0 contraste insuffisant sur 14 pages en clair et en sombre ; focus clavier visible ; 0 débordement à 200 % de zoom ; noms de liens uniques sur les cartes produit ; étiquettes inutiles et emojis retirés.
- **Performance** : polices 60 Ko hébergées localement (aucun appel à un service tiers) ; `style.css` fait 229 Ko, `redesign.css` 22 Ko, `v5.css` 12 Ko.

## 5. Fichiers
- **Ajoutés** : `v5.css`, `fonts/` (3 polices WOFF + `LICENCES.txt`), `Tools/CHANGELOG-V5.md`.
- **Modifiés** : les 14 pages HTML, `_headers` (cache de `/v5.css` et `/fonts/*`).
- **Déplacés (rien n'est supprimé)** : `images/padel.webp` et `images/padel-480w.webp` → `Tools/a-verifier-droits/`.

## 6. Vérifications effectuées (Chromium, local)
28 chargements de pages (14 pages × mobile et bureau) sans erreur ni requête manquante ; 676 liens internes valides ; en-tête qui se masque en descendant et réapparaît en remontant ; polices chargées sans erreur de console ; contraste, structure, clavier et zoom contrôlés ; contenu des boutons Amazon, `double.webp` et « Emplacement test » comparés à la v4.

## 7. Reste à faire et nouveaux constats
**Avant la mise en ligne**
1. **Dates et auteur** : dates de publication et de mise à jour des 8 guides, et nom d'auteur ou de relecteur si tu veux en afficher un. Je les ajouterai au balisage et à l'en-tête.
2. **Images de remplacement** (liste en section 8). Tant qu'elles manquent : l'ouverture de Règles est provisoire ; les guides Raquette débutant (BD avec texte et prix incrustés), Tendinite (schéma « TENNIS ELBOW » en anglais) et Techniques (« PADEL SHOTS ») gardent leurs visuels actuels.
3. **Droits des images** : confirmer l'origine de `bandeja.webp` et des photos produits (`head_evo`, `adipower`, `babolat_contact`, `dunlop_titan`, `wilson_optix`, `asicsgel`). Pour les produits Amazon, utiliser les outils d'images du programme Partenaires.
4. **Produits** : vérifier les noms et les liens. « Asics Gel-Dedicate Clay » et « Asics Gel-Resolution Padel » ressemblent à des modèles de tennis ; seuls les liens Asics pointent vers une fiche précise, les autres sont des recherches Amazon. Dater les prix de l'article Raquette débutant.
5. **Mentions légales** (nom, e-mail), puis Cloudflare : Speed Optimizations, puis Bot Fight Mode 24 à 48 h après.
6. **Production** : confirmer la disparition des « Emplacement test » et brancher les emplacements AdSense.

**Qualité éditoriale (prochaine passe)**
- Lisibilité : Échauffement (indice Flesch français ≈ 37), Chaussures (≈ 40) et Tendinite (≈ 43) ont des phrases moyennes de 23 à 25 mots ; une réécriture changerait ta voix, je ne l'ai pas faite sans ton accord.
- Balles : le bloc d'achat reste générique (« Head Padel Pro ou Bullpadel ») ; il faudrait 2 ou 3 références nommées, que tu choisis.
- Raquette débutant : un tableau comparatif des 4 modèles serait utile (données à valider par toi).
- Techniques : 12 400 px de hauteur ; envisager deux pages (fondamentaux / vitres et coups avancés).
- Schéma anatomique de la tendinite : je peux le redessiner en français (SVG), sans image à fournir.

**Constats nouveaux**
- Les pages `page-tactics-guide` n'ont pas la classe `page-editorial-guide` : c'est ce qui rendait le deuxième sommaire non stylé. À unifier lors d'une future simplification de `style.css` (229 Ko, nombreuses règles par page).
- Les liens Amazon sont majoritairement des pages de recherche : les fiches précises (ASIN) convertissent en général mieux.
- Les pages Contact, Confidentialité et Mentions légales n'ont pas été redessinées (accueil et 8 guides seulement).

## 8. Images à fournir pour la partie suivante
Par ordre de priorité :
1. **Les 11 images d'accueil** (prompt déjà donné) : hero, règles, techniques, tactique, lob, vitre de fond, raquette, balles, chaussures, tendinite, échauffement.
2. **4 images d'étapes d'échauffement** (3:2, 1200 px minimum, sans texte) : mise en mouvement générale, mobilité dynamique, activation des appuis, raquette et balle.
3. **Image d'ouverture de Techniques** pour remplacer « PADEL SHOTS » (16:9, une bandeja photo, sans texte).
4. **Figures de Techniques sans texte incrusté** (3:2, 1200 px minimum) : d'abord bandeja, víbora, smash, chiquita, bajada, puis volée, position d'attente, coup droit/revers, transition fond-filet, double vitre.
5. **Photos produit propres** (fond blanc ou transparent, 800 px minimum) : Head Evo/Flash, Babolat Contact/Drive, Dunlop Titan/Megamax, Wilson Optix/Team, Head Zephyr Ultralight, Dunlop Rapid Control, Adidas Match Light, Adidas Adipower Light, Asics Gel-Dedicate Clay, Bullpadel Beker, Head Revolt Court, Asics Gel-Resolution. À obtenir par les canaux officiels (Partenaires Amazon ou dossiers de presse des marques), pas par génération IA.
