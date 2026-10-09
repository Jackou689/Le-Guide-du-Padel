# Rapport d’audit du lot 8E

## Correctifs appliqués

- Suppression durable de `style-src 'unsafe-inline'` après centralisation de cinq blocs `<style>` dans `style.css`.
- Remplacement du changement de style JavaScript du filtre d’accueil par une classe CSS.
- Conservation temporaire de `script-src 'unsafe-inline'` pour les données structurées JSON-LD.
- Harmonisation des liens internes, canoniques, métadonnées sociales, JSON-LD et sitemap vers les URL sans `.html`.
- Configuration explicite de `html_handling: auto-trailing-slash` et `not_found_handling: 404-page`.
- Nettoyage des fichiers `.DS_Store` et ajout de `.gitignore`.
- Ajout de `.assetsignore` pour empêcher la publication des outils, rapports et fichiers de configuration comme actifs publics.
- Ajout d’un audit 8E détectant les balises `<style>`, attributs `style`, scripts fonctionnels inline, URL canoniques incohérentes et liens cassés.

## État CSP

La politique active autorise les ressources nécessaires à la version actuelle :

- scripts locaux et JSON-LD inline ;
- beacon Cloudflare depuis `static.cloudflareinsights.com` ;
- styles locaux uniquement ;
- images locales, `data:` et le domaine historique `images.unsplash.com` ;
- connexions Cloudflare Web Analytics.

`style-src` ne contient plus `'unsafe-inline'`.

## Résultat automatisé

- 14 pages HTML ;
- 13 canoniques uniques ;
- 14 beacons Cloudflare ;
- 0 balise `<style>` ;
- 0 attribut `style` ;
- 0 script fonctionnel inline ;
- 0 actif local manquant ;
- 0 lien interne cassé ;
- 0 lien Amazon sans `nofollow sponsored` ;
- sitemap XML valide ;
- JavaScript syntaxiquement valide.
