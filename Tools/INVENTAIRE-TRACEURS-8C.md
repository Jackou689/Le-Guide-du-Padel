# Inventaire des traceurs — Lot 8C

## Résultat

L’audit statique des 13 pages identifie trois mécanismes actifs et un service futur.

### Préférence de thème

- Technologie : `localStorage`
- Clé : `theme`
- Finalité : mémoriser le mode clair ou sombre choisi par le visiteur
- Portée : appareil et navigateur utilisés
- Domaine tiers : aucun

### Cloudflare Web Analytics

- Technologie : beacon JavaScript `static.cloudflareinsights.com/beacon.min.js`
- Présence : une fois sur chacune des 13 pages
- Finalité : statistiques agrégées de fréquentation et mesure de performance
- Cookies / localStorage : aucun selon la documentation Cloudflare
- Empreinte numérique : non utilisée par Cloudflare pour cette mesure selon sa documentation

### Liens Amazon Partenaires

- Technologie : liens HTTPS classiques contenant l’identifiant partenaire
- Script ou iframe Amazon sur le site : aucun
- Déclenchement : uniquement lors du clic du visiteur vers Amazon
- Signalement : mentions de transparence présentes avant les blocs affiliés

### Google AdSense

- Statut : inactif
- Script `adsbygoogle.js` : absent
- Domaine `googlesyndication.com` : absent
- Domaine `doubleclick.net` : absent
- Emplacements de prévisualisation : placeholders locaux, sans diffusion publicitaire
- Activation future : message de consentement configuré directement dans Google AdSense, sans bandeau artisanal ajouté au site
