# Changelog v11 (19 novembre 2026)

## CSS : un seul fichier
- `style.css`, `redesign.css` et `v5.css` fusionnés dans `/style.css?v=2026-11` (ordre de cascade conservé). `redesign.css` et `v5.css` supprimés ; `_headers` mis à jour.
- 255 040 → 200 639 octets (−21 %) ; 40,3 → 30,6 Ko compressé (−24 %) ; 3 requêtes → 1.
- 424 sélecteurs jamais utilisés retirés (liste : `Tools/CSS-SELECTEURS-RETIRES-V11.txt`), `@keyframes` inutilisés et commentaires retirés. Conservés : tout ce qui touche Amazon, h5/h6, `pre`, `img`, titres des encadrés.
- Accueil : il ne chargeait pas l'ancien `style.css`. Ses règles globales (html, body, a, img, svg, `*`, mode sombre) sont désormais limitées aux autres pages via `:where(...)` (spécificité inchangée), et `<html data-page="home">` a été ajouté dans `index.html`.

## Vérifications (v10 → v11)
- 70 captures pleine page (14 pages × mobile/ordinateur × clair/sombre + menu mobile) : 0 pixel de différence.
- 260 états survol / focus clavier : 0 différence.

## À savoir pour la suite
- Un composant qui n'existe aujourd'hui que sur certaines pages (variante mode sombre propre à une page) peut demander une règle dédiée sur un nouvel article.
- Le « vieux JavaScript » de PageSpeed vient très probablement de scripts tiers (AdSense, Cloudflare). `script.js` (5 Ko, ES5) n'est pas en cause.
