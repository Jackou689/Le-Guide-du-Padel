# Checklist de déploiement Cloudflare — Lot 8D

## Avant publication

- [ ] Terminer la micro-entreprise puis le lot 8B.
- [ ] Vérifier les mentions légales définitives.
- [ ] Déployer le contenu du dossier `padel_lot8a2`.
- [ ] Vérifier que `_headers`, `_redirects` et `404.html` sont publiés.
- [ ] Ne pas activer AdSense avant validation de la configuration prévue dans le compte.

## Contrôles après publication

- [ ] `https://leguidedupadel.fr/` répond en HTTPS.
- [ ] `/index.html` redirige vers `/` en 301.
- [ ] Une URL inconnue retourne la page 404 personnalisée avec un statut HTTP 404.
- [ ] Les URL sans extension définies dans `_redirects` redirigent en 301.
- [ ] Les en-têtes de sécurité sont présents.
- [ ] Les images locales possèdent un cache long.
- [ ] Le HTML reste revalidé afin que les corrections soient rapidement visibles.
- [ ] Le menu mobile et le mode sombre fonctionnent.
- [ ] La page Contact ouvre correctement le logiciel de messagerie.
- [ ] Le sitemap et le fichier robots sont accessibles.
- [ ] Aucun placeholder publicitaire n’est visible sur le domaine de production.
