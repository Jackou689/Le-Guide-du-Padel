# Rapport de refonte — Le Guide du Padel (base lot 10A.17)

Livraison : branche `redesign-2026` (historique git inclus dans l'archive de travail), non déployée. Dépôt GitHub non accessible depuis mon environnement (pas de réseau) : travail réalisé sur l'archive `padel_lot10A_17.zip`.

## 1. Ce qui a été reçu et vérifié
- Archive lot 10A.17 : 138 fichiers, 14 pages HTML (accueil, 8 guides, à propos, contact, mentions légales, confidentialité, 404), `style.css` (234 Ko), `script.js`, `wrangler.jsonc`, `_headers`, `_redirects`, `robots.txt`, `sitemap.xml`, `ads.txt`. Kit `brand.zip` (logos clair/sombre, LGP, signature, favicons).
- Version confirmée par `Tools/RAPPORT-LOT-10A17.md`.

## 2. Audit — problèmes trouvés
| # | Constat | Gravité | Traité |
|---|---|---|---|
| 1 | **CSP bloquante** : `script-src` n'autorisait pas `pagead2.googlesyndication.com`, `img-src` / `frame-src` / `connect-src` non plus. Le script AdSense et la CMP Google ne pouvaient donc probablement pas s'exécuter en production. | Élevée | Oui (CSP élargie aux domaines Google, **à valider en conditions réelles**) |
| 2 | **Aucune balise favicon** dans les 14 pages. | Moyenne | Oui |
| 3 | **Images de la page techniques mal nommées** (ex. `technique-chiquita.webp` = volée, `technique-vitre-fond.webp` = bandeja, `technique-double-vitre.webp` = víbora…) ; `technique-bandeja.webp` montrait une position d'attente ; `technique-position.webp` utilisée 2 fois (sections 1 et 9) ; image de la section « lob » = frappe aérienne, pas un lob. | Élevée | Oui (voir §3) |
| 4 | `style.css` : 234 Ko, 425 `!important`, ~1 800 sélecteurs `dark-mode`, couches v15/v16/v17 empilées. Source des régressions passées. | Élevée | Contournée (couche additive) ; nettoyage **volontairement reporté** |
| 5 | Signature « Publié par… » présente sur 4 pages sur 8 seulement. | Faible | Oui |
| 6 | Hébergement : mentions légales parlent de « Cloudflare Pages », le projet utilise Workers. | Faible | Corrigé (à confirmer) |
| 7 | Bouton clair/sombre = emoji, thème appliqué après le premier rendu. | Moyenne | Oui (slider `role="switch"`, thème posé avant rendu) |
| 8 | Contrastes AA insuffisants : fil d'Ariane, légendes, mentions d'affiliation (≈3,8:1) ; page Contact en mode sombre (≈1,4:1) ; boutons « Étape suivante » (≈2,5:1) ; jauges d'équilibre en sombre. | Moyenne | Corrigés par surcharges ciblées |
| 9 | Pas de lien d'évitement, menu mobile sans libellé de zone `main` sur les pages légales. | Faible | Lien d'évitement ajouté |
| 10 | Pas de 403 ni de règle de blocage dans `wrangler.jsonc`/`_headers`/`_redirects` ; `robots.txt` autorise tout ; canonical correctes ; sitemap (13 URL propres) cohérent ; 404 avec `noindex`. | — | Rien à corriger dans le code |
| 11 | AdSense : script présent 1 fois par page, meta `google-adsense-account` présente, `ads.txt` correct. Web Analytics : snippet présent 1 fois, token conservé. Aucun bloc `<ins>` réel : uniquement des emplacements de test (masqués en production). | — | Conservés tels quels |

## 3. Images — correspondances vérifiées visuellement (page techniques)
Nouveaux noms (préfixe `padel-`, jamais réutilisation d'un ancien nom : le dossier `/images/*` est en cache immuable un an) :
- Section 1 → `padel-position-attente.webp` · 2 → `padel-fond-de-court-coup-droit-revers.webp` · 4 → `padel-volee.webp` · 5 → `padel-bandeja.webp` · 6 → `padel-vibora.webp` · 7 → `padel-smash.webp` · 8 → `padel-chiquita.webp` · 10 → `padel-double-vitre.webp` · 11 → `padel-bajada.webp` · 12 → `padel-transition-fond-filet.webp`.
- **Section 3 (lob) et section 9 (jeu après la vitre)** : l'ancienne image ne correspondait pas ; elle a été remplacée à l'itération 2 par deux schémas au style du site (`ill-lob`, `ill-vitre-fond`). Fichiers conservés : `a-verifier-frappe-aerienne.webp` (ex-lob), `padel-position-attente-appuis.webp` (ex-« technique-bandeja »).
- Alt corrigés : section 2, illustration d'en-tête (`bandeja.webp` = planche « Padel Shots »), 8 cartes d'accueil.
- Pages échauffement et tactique : correspondances image/section correctes. `routine-echauffement-visuelle.webp` est identique à `echauffement-padel-guide.webp` (même image deux fois sur la page).

## 4. Tests effectués (réels, Chromium headless, fichiers locaux)
- Intégrité : 0 lien interne cassé, 0 asset ou srcset manquant, 0 id dupliqué, 1 seul H1 par page, 1 script AdSense et 1 beacon Cloudflare par page, canonical / robots / JSON-LD identiques à l'original, **18 liens Amazon strictement identiques** (identifiant `leguidedupade-21` inchangé), aucun mot du contenu éditorial perdu (seules disparitions : « Publié par », menu historique, « Cloudflare Pages »), aucune balise dans un attribut `alt`.
- Débordement horizontal : aucun à 360, 390, 768, 1024 et 1440 px sur les 14 pages.
- Clavier : ouverture du menu mobile à Entrée, focus sur « Fermer », piège de focus (30 Tab), Échap ferme et rend le focus au bouton, `aria-expanded` / `inert` corrects, défilement de fond bloqué. Slider opérable à la barre d'espace.
- Filtre d'accueil OK ; sans JavaScript : 8 cartes visibles, aucun encart publicitaire visible ; 404 renvoie bien un statut 404 + `noindex`.
- Contraste : script maison (clair et sombre, toutes pages). Limite : il produit des faux positifs sur fonds en dégradé/surlignage. Corrections visuelles confirmées (Contact sombre, boutons, jauges).
- Captures avant/après : `captures/avant` (lot 10A.17) et `captures/apres` (accueil, article, légal × desktop/mobile × clair/sombre + menu ouvert).
- **Non réalisés** : Lighthouse (non disponible), validation W3C en ligne, impression (règles `@media print` ajoutées mais non vérifiées), test avec un bloqueur de publicités, tests des en-têtes HTTP réels (Cloudflare), test de la CMP.

## 4 bis. Test du thème au rechargement
Le test automatique a réinitialisé la préférence à chaque chargement (artefact du banc d'essai) ; la logique (localStorage + pré-rendu) est simple mais reste à confirmer à la main.

## 5. Problèmes non résolus / limites
1. **Refonte incomplète côté articles** : les 8 guides gardent leurs composants historiques (`editorial-*`, `affiliate-*`…) servis par `style.css`. Ajoutés : ligne d'info, signature, articles liés, sommaire (tactique-filet). Le catalogue de composants éditoriaux unifiés (encadrés définition/erreur/FAQ/sources, tableaux, etc.) **n'est pas construit** ; il demande de retoucher le contenu article par article.
2. Pages à propos, contact, mentions légales, confidentialité, 404 : nouvel en-tête/pied de page/thème uniquement, pas de nouvelle mise en page.
3. Sidebar des articles (emojis, « Navigation rapide ») conservée.
4. Pas de page catégorie ni de recherche (le filtre d'accueil sert de structure). Pas de « retour à la catégorie ».
5. Nettoyage du code mort **non fait** (volontaire) : `style.css` toujours chargé sur les articles ; ~9 fichiers image non référencés (`bandeja.png`, `banniere-*`, `logo-concept-a.png`, `logo-header.webp`…) ; `Tools/audit_lot8c/8d.py` obsolètes.
6. Les images internes des articles gardent leurs styles d'origine (photos, dessins IA) : seules les cartes d'accueil, le hero et les deux schémas ajoutés suivent le nouveau style.
7. Aucune date de publication/mise à jour n'a été ajoutée (aucune date fiable dans le lot).
8. Poids : l'accueil n'utilise plus `style.css` (≈ 25 Ko de CSS propre) ; les articles chargent encore `style.css` + `redesign.css`.

## 6. Décisions que je n'ai PAS prises seul
URL (inchangées, aucune redirection ajoutée), suppression d'articles ou de liens affiliés (aucune), identité visuelle (reprise de `brand.zip`), mise en production, Cloudflare Speed Optimizations / Bot Fight Mode / Pay Per Crawl, nouvelle demande AdSense. Comportement CMP : non modifié.

## 7. Actions manuelles après déploiement
**À signaler** : la CSP et la mention d'hébergeur sont des modifications de configuration/légal que vous devez valider.

### Checklist Cloudflare
1. Déployer d'abord sur une URL de preview (`preview_urls: true`) ; vérifier que les canonical pointent toujours vers `https://leguidedupadel.fr`.
2. Après mise en production : console du navigateur sur l'accueil et un article → **aucune erreur CSP** (script AdSense, CMP, images d'annonces, iframes).
3. Si des erreurs CSP persistent : passer temporairement l'en-tête en `Content-Security-Policy-Report-Only`, relever les domaines bloqués, compléter, repasser en mode bloquant.
4. Vérifier `ads.txt`, `robots.txt`, `sitemap.xml` servis à la racine (200).
5. Vérifier qu'aucune règle WAF/Security ne renvoie 403 à Googlebot (Security → Events, user agent Googlebot).
6. Puis, séparément : activer Speed Optimizations ; 24-48 h plus tard seulement, Bot Fight Mode, en surveillant Googlebot, AdSense (Mediapartners-Google) et les robots légitimes.
7. Pay Per Crawl : plus tard (plusieurs dizaines d'articles, trafic régulier, volume IA significatif dans AI Crawl Control).

### Checklist Search Console
1. Inspecter l'accueil et 2-3 guides (« Tester l'URL en direct ») : page accessible, pas de 403.
2. Renvoyer `sitemap.xml` ; surveiller « Pages » (indexées / explorées non indexées).
3. Demander l'indexation de l'accueil après déploiement ; ne pas multiplier les demandes.
4. Surveiller la couverture et l'expérience de page sur 2 à 4 semaines.
5. Aucune garantie d'indexation : la qualité et la quantité de contenu comptent autant que la technique.

### Checklist AdSense
1. Contrôler que le message européen (CMP) s'affiche et que sa fermeture vaut toujours refus (comportement existant à ne pas changer).
2. Vérifier qu'aucune annonce n'est servie avant consentement.
3. Pour activer un bloc : insérer `<ins class="adsbygoogle">` dans `.lgp-ad-box` et ajouter `is-live` à `<aside class="lgp-ad">` ; sur les articles, les emplacements historiques `.ad-placeholder` sont conservés.
4. **Ne pas redemander l'examen** avant : ensemble substantiel d'articles solides et indexés (voir recommandations éditoriales), indexation stabilisée.
5. Vérifier la page confidentialité (mention de la mesure d'audience et d'AdSense déjà présente depuis 10A.17).

### Autres
- Valider « Cloudflare (Workers) » dans les mentions légales (SIREN, directeur de la publication et e-mail déjà présents ; rien d'autre ajouté).
- Contact : adresse e-mail seulement (`mailto:`), pas de faux formulaire.


---
# Itération 2 (28/10/2026)

## Retours traités
| Retour | Cause trouvée | Correction |
|---|---|---|
| Logo illisible en mode sombre | Logo trop petit (≈50 px), détails fins de la raquette blanche perdus sur le bleu nuit | Logos recadrés/rééchantillonnés plus nets, hauteur 68 px (56 px en mobile), léger liseré clair en mode sombre ; en-tête 84 px |
| Logo mobile à centrer | Logo aligné à gauche à côté du burger | En-tête mobile en grille 3 colonnes : burger à gauche, logo centré (vérifié : centre = 195 px sur 390 px), slider à droite |
| Menu burger qui ne défile pas | Panneau en `content-box` : sa hauteur dépassait l'écran du padding (≈ 40 px), les derniers liens étaient hors d'atteinte ; pas d'indice de défilement | `box-sizing:border-box`, `100dvh`, `overscroll-behavior:contain`, zone du haut (logo + fermer) collée, dégradé d'indice en bas ; test à 520 px de hauteur : dernier lien atteignable |
| En-tête à masquer en descendant | — | `transform` : masquée en descendant, réapparaît à la moindre remontée, toujours visible en haut de page, menu ouvert ou focus clavier dans l'en-tête ; désactivable par `prefers-reduced-motion` |
| Plus d'emphase sur les notions clés | — | Outil `Tools/emphasize_articles.py` : 4 à 12 notions par guide (poids, mousse, bandeja, semelle…) en gras avec surlignage vert, sans changer un seul mot (vérifié mot pour mot) ; mode sombre adapté ; ajout d'une barre de progression de lecture |
| Images d'accueil incohérentes | Mélange de photos, dessins IA, schémas | 8 illustrations + hero au **même style** (fond bleu nuit, lignes de piste en filigrane, pictogramme blanc/bleu, accent vert, « swoosh » signature). Sources SVG dans `Tools/REFONTE-2026/illustrations-src/`, générateur `Tools/make_illustrations.py` |
| Images supprimées à remplacer | Lob et jeu après la vitre | Deux schémas dans le même style, réinsérés au même emplacement avec alt et légende d'origine |

**Honnêteté sur les images** : elles ont été créées par code (illustrations vectorielles), pas par un générateur d'images IA ni retouchées à la main ; elles sont volontairement simples et schématiques. Elles sont modifiables (SVG source) et remplaçables plus tard par un jeu d'illustrations commandé à un graphiste si vous voulez un rendu plus riche.

## Pistes d'amélioration relevées (non faites)
1. Harmoniser aussi les images internes des guides (≈ 30 visuels de styles différents) avec le même système d'illustrations.
2. Unifier les composants éditoriaux (encadrés astuce/erreur/à retenir) en un jeu cohérent ; aujourd'hui, 3 familles de styles historiques coexistent.
3. Ajouter un résumé « En bref » en tête de chaque guide (à rédiger, pas généré automatiquement).
4. Techniques-padel : 12 sections sur une page, envisager une page par coup (maillage, requêtes précises).
5. Sources : la page tactique cite un fil Reddit ; préférer des sources fédérales ou d'entraîneurs.
6. Hiérarchie des titres : 4 sous-titres produits (h4) sautaient un niveau sur chaussures et tendinite ; corrigés via `aria-level="3"`.
7. Nettoyage CSS (234 Ko) toujours à planifier, de préférence page par page.
8. Test des vrais appareils (Safari iOS notamment : barre d'adresse dynamique, défilement du menu) à faire avant mise en ligne.

## Tests de l'itération 2
Intégrité identique à l'itération 1 (0 lien/asset cassé, 18 liens Amazon inchangés, 1 script AdSense et 1 beacon par page, texte éditorial identique mot pour mot une fois les surlignages retirés), 0 débordement horizontal à 5 largeurs sur 14 pages, 0 erreur JavaScript, comportement de l'en-tête testé (descente → masquée, remontée → visible, haut de page → visible).

## Note de maintenance
`Tools/build_refonte_2026.py` est le script de transformation **initial** (lot 10A.17 → refonte) : ne pas le relancer sur les fichiers actuels, il écraserait `script.js` et les correctifs de l'itération 2. Les évolutions se font directement dans `redesign.css`, `script.js` et les pages.
