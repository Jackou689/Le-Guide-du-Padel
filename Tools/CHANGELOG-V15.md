# Changelog v15 (22 novembre 2026)

## Performance mobile (mesures simulées : 4G lente, CPU ×4, Chromium)
- Logos d'en-tête : 4 fichiers (≈ 207 Ko) téléchargés sur chaque page alors que 3 sur 4 restaient cachés. Remplacés par des versions allégées (*-opt.webp, 18 à 35 Ko, rendu identique) et chargés en lazy (variantes sombre/clair et mobile/ordinateur non visibles). Les anciens fichiers restent dans images/brand/ (JSON-LD, anciens liens).
- Accueil (mobile) : 282 → 131 Ko transférés ; LCP simulé 1 560 → ≈ 1 160 ms (v10 : ≈ 1 110 ms).
- Article « Règles » (mobile) : LCP simulé 2 800 → ≈ 1 870 ms par rapport à la v10.
- Reste à traiter : images principales (≈ 140 Ko en 1000w), polices .woff → .woff2 (outil de conversion absent ici), scripts tiers (AdSense : 150 Ko de JS inutilisé, non modifiable).

## Articles étoffés (seuil visé : ≈ 1 250 mots hors encadrés commerciaux)
- sac-padel-debutant : 784 → ≈ 1 170 mots (profils, préparation, saisons, erreurs, FAQ).
- chaussures-padel : 1 097 → ≈ 1 310 (sol du court, entretien, erreurs d'achat).
- raquette-debutant : 1 094 → ≈ 1 270 (erreurs d'achat, entretien).
- formes-raquette-padel : 1 139 → ≈ 1 290 (lire une fiche technique).
- Source corrigée dans le sac : l'adresse Assurance Maladie n'était pas vérifiée ; remplacée par la page « Sport et canicule » du ministère des Sports.
- À surveiller : balles-padel (≈ 1 180) et tactique-filet (≈ 1 240).
