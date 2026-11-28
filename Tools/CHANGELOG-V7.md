# Le Guide du Padel — v7 : journal détaillé (validation de la v6)

Schéma : **Quoi**, **Pourquoi**, **Par quoi**. Tout est dans `v5.css` (section « v7 »), dans les 14 pages (références des logos) et dans `Tools/` (documentation de la palette).

## 0. Ta demande → ce qui a été fait
| Demande | Fait |
|---|---|
| Voir la palette validée sur le site, sans casser l'harmonie de la v6 | Les 9 couleurs sont appliquées par rôle (section 3) |
| Logo du mode sombre : reprendre la raquette du logo clair, sans la changer | Raquette copiée pixel pour pixel depuis le logo clair (section 1) |
| Redessiner l'icône de raquette de la barre latérale | Nouvelle icône (section 2) |
| Garder bouton vert, dates, reste de la v6 | Inchangés |
| Valider à chaque étape les skills et plugins adaptés | Tableau en section 4 |

## 1. Logo du mode sombre
- **Quoi** : dans les deux logos sombres (principal et « LGP »), la raquette est celle du logo clair : cadre blanc, face bleu nuit à trous blancs, manche rayé. Texte blanc, balle et trait verts inchangés.
- **Pourquoi** : tu veux garder l'identité du logo clair dans les deux modes ; la raquette bleue de la v6 était une variante que tu ne retiens pas.
- **Par quoi** : fusion de la zone « raquette » du logo clair (pixels d'origine, sans recoloration) dans le logo sombre ; nouveaux fichiers `logo-main-sombre-v3.webp` et `logo-lgp-sombre-v3.webp` (nom versionné pour le cache), 56 références mises à jour sur les 14 pages. Les anciens fichiers restent dans `images/brand/` (rien n'est supprimé).
- **Point d'attention** : sur le fond sombre, la face bleu nuit se fond avec l'en-tête ; la raquette se lit grâce au cadre blanc, aux trous et aux rayures du manche (contrôlé sur fond #0F2540, à taille réelle et en agrandi).

## 2. Icône de raquette de la barre latérale
- **Quoi** : raquette de padel inclinée, tête large perforée, col et manche.
- **Pourquoi** : l'ancienne ressemblait à une loupe ; un premier essai vertical ressemblait à une ampoule.
- **Par quoi** : trois variantes comparées à 84, 41 et 34 px ; retenue : la raquette inclinée sans balle (la balle devenait illisible à petite taille). Dessin SVG intégré au CSS.

## 3. La palette, visible sur le site
| Couleur | Où elle apparaît maintenant |
|---|---|
| **Aqua #18B6A4** | Encadrés « astuce du coach », tags « Santé », icônes Santé de la barre latérale, mots-clés |
| **Corail #E5484D** | Encadrés « piège », prix des produits |
| **Ambre #F59E0B** | Encadrés de transparence (affiliation), séquences, petites mentions d'affiliation |
| **Lime texte #4B6600** | Phrases mises en avant en serif, texte des encadrés « À retenir » et des tags Règles et tactique (nuance #3F5700 sur fond teinté pour garder le contraste) |
| **Lime survol #BEEA45** | Boutons verts (accueil et en-tête) au survol |
| **Bleu court #1A63E0** | Liens dans le texte, encadrés d'information (santé, étape suivante) |
| **Ivoire #FAF8F3** | Fond de tous les guides en mode clair |
| **Nuit profonde #071626, Surface sombre #0F2540** | Fond et cartes du mode sombre |
- **Règle d'harmonie** : un accent par sens (bleu = information, aqua = astuce et santé, lime = à retenir, ambre = transparence, corail = piège). Les violets et oranges disparaissent des encadrés. Même structure, mêmes rayons, mêmes textes qu'en v6.
- **Par quoi** : 14 classes d'encadrés historiques (`coach-tip-box`, `astuce-box`, `erreur-box`, `affiliate-*`, `recap-box`, `health-disclaimer`…) regroupées en 5 familles à 4 variables (`--bx`, `--bx-bg`, `--bx-line`, `--bx-ink`), versions claire et sombre ; tags en bleu, lime et aqua ; fonds par `body:has(main.article-content)` ; liens de texte sur le jeton de lien.
- **Boutons Amazon, `double.webp` et « Emplacement test »** : inchangés. La petite mention « Lien affilié » sous les boutons garde un format discret (ambre léger).

## 4. Skills et plugins choisis à chaque étape
| Étape | Skill ou plugin | Pourquoi lui |
|---|---|---|
| Audit des couleurs avant d'agir | *design-system* (ECC), mode audit | Mesure la cohérence des couleurs et la complétude du mode sombre |
| Documentation de la palette | *design-system* (plugin Design) | `Tools/DESIGN.md` et `design-tokens.json` : règles d'usage et valeurs |
| Choix des familles d'encadrés | *frontend-design-direction* (ECC) | Un accent par sens, hiérarchie visuelle |
| Rayons, bordures, hauteurs d'icône | *make-interfaces-feel-better* (ECC) | Détails de finition |
| Choix de l'icône et jugement du logo sombre | *design-critique* (plugin Design) | Comparaison de variantes sur captures |
| Contrastes des nouveaux encadrés | *accessibility-review* (plugin Design), *accessibility* (ECC) | Mesure sur 14 pages, clair et sombre |
| Non retenus | *ux-copy*, *seo* (aucun texte ni balisage nouveau), plugin d'audit SEO (site en ligne requis), génération d'images | Hors besoin de cette étape |

## 5. Audit des couleurs (skill design-system)
- Le CSS historique `style.css` contient **1 439 usages de 303 couleurs distinctes** ; les couches `redesign.css` et `v5.css` en comptent 50 chacune (hors historique). C'est la principale dette : une palette de 12 couleurs coexiste avec des centaines de teintes en dur.
- Ce qui est maintenant sous palette : en-tête, accueil, sommaire, barre latérale, 14 classes d'encadrés, tags, liens de texte. Ce qui ne l'est pas encore : le reste des règles par page de `style.css` (cartes de section, tableaux secondaires, dégradés d'illustration).
- Suite possible : un chantier de consolidation de `style.css` (229 Ko) vers les jetons.

## 6. Vérifications (Chromium)
28 chargements de pages sans erreur ; 703 liens internes valides ; 0 contraste insuffisant (un faux positif connu : texte blanc sur le dégradé bleu nuit de « Résumé tactique ») ; focus clavier visible ; pas de défilement horizontal à 200 % ; polices sans erreur de console ; numéros du sommaire alignés sur les titres ; en-tête qui se masque et réapparaît.

## 7. Reste à faire
1. **Images** (inchangé) : 11 images d'accueil, 4 étapes d'échauffement, ouverture et figures de Techniques, photos produit propres.
2. Droits des images, noms et liens produits, mentions légales, Cloudflare, AdSense (voir journal v5).
3. Chantier optionnel : consolider `style.css` sur les jetons.
4. Pages Contact, Confidentialité, Mentions légales : seuls les liens et les polices suivent la palette ; leur mise en page n'a pas été refaite.
