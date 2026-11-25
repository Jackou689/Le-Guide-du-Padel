# DESIGN — Le Guide du Padel (v8)

## Principes
- **Marque conservée** : Nuit #0B2A45, Lime #A7E11D, Brume #F1F5F9 (logos, favicon, en-tête). Le logo du mode sombre reprend la raquette du logo clair, sans retouche.
- **Un accent par sens** : bleu = information, action, matériel ; aqua = astuce et confort ; lime = à retenir, règles et tactique ; ambre = transparence et conseils ; corail = pièges, erreurs et **santé & blessures**.
- **Catégories de contenu** : Matériel = bleu (teinte 216°), Règles et tactique = lime (77°), Santé et blessures = corail (4°). Variante de secours si besoin de dissocier santé et pièges : violet #7650B5 (non utilisé).
- **Deux modes complets** : clair (fond ivoire sur les guides, cartes blanches) et sombre (nuit profonde #071626, cartes #0F2540).

## Typographie
| Jeton | Valeur | Usage |
|---|---|---|
| `--font-head` | Poppins 500/700 (hébergée) | tous les titres, boutons, filtres, tags, fil d'Ariane, pied de page |
| `--font-body` | pile système (-apple-system, Segoe UI, Roboto, Helvetica Neue, Arial) | texte courant, listes, tableaux |
| `--font-serif` | Lora variable (hébergée), repli Georgia | chapô et phrases mises en avant |
Graisses : 400, 500, 600, 700 (800 et 900 seulement dans les boutons Amazon, volontairement inchangés).

## Couleurs : règle « zéro hexadécimal en dur »
- Toute couleur d'une règle CSS passe par un jeton : `--lgp-*` (palette), `--c-<teinte>-<clarté>` ou `--slate-<clarté>` (teintes historiques regroupées), `--c-night-*`, `--c-white`, `--c-black`.
- Les valeurs sont définies une seule fois, en tête de `redesign.css` (chargé par toutes les pages ; `style.css` n'est pas chargé par l'accueil).
- Table de correspondance ancienne couleur → jeton : `consolidation-couleurs.json`. Jetons détaillés : `design-tokens.json`.
- Encadrés : une règle commune, quatre variables par famille (`--bx`, `--bx-bg`, `--bx-line`, `--bx-ink`).

## À ne pas faire
- Écrire une couleur en dur dans une règle : créer ou réutiliser un jeton.
- Utiliser le corail ou l'aqua clair pour du petit texte sur fond clair : utiliser les encres #B42318 (`--lgp-coral-ink`) et #0B5F56.
- Modifier le contenu des boutons Amazon.
