# Tests d’acceptation du lot 8C

## Principe de recette

Le lot 8C prépare le site à une future activation AdSense. Il ne charge pas AdSense et n’ajoute aucun bandeau artisanal. Le message relatif aux réglementations européennes sera configuré directement dans Google AdSense selon la configuration déjà retenue dans le compte.

## AC-01 — Inventaire

- 13 pages HTML analysées.
- Chaque script tiers, stockage local, lien affilié et service futur est documenté.
- Aucune occurrence inexpliquée de cookie, `localStorage`, `sessionStorage`, AdSense ou DoubleClick.

## AC-02 — Cloudflare Web Analytics

- Exactement un beacon Cloudflare par page.
- Aucun Google Analytics supplémentaire.
- La politique de confidentialité décrit le service et son absence déclarée de cookie et de stockage local.

## AC-03 — AdSense reste inactif

- Aucun `adsbygoogle.js`.
- Aucun appel vers `googlesyndication.com`.
- Aucun appel vers `doubleclick.net`.
- Les placeholders restent locaux et ne s’affichent qu’en preview ou en local.

## AC-04 — Configuration AdSense convenue

- Aucun bouton ou texte « Tout refuser » n’est ajouté par le lot 8C.
- Aucun bandeau de consentement artisanal n’est ajouté.
- La checklist renvoie à la configuration du message directement dans AdSense.
- Les tests futurs couvrent « Consentir », « Gérer les options » et la modification ultérieure du choix.

## AC-05 — Politique de confidentialité

- Distingue clairement les services actifs des services futurs.
- Décrit la préférence de thème, Cloudflare Web Analytics, les liens Amazon et AdSense inactif.
- N’annonce aucun script publicitaire comme actif.
- Ne contient aucun SIREN, aucune adresse ou donnée juridique fictive.

## AC-06 — Amazon

- Les liens restent de simples liens externes.
- Aucun script ni iframe Amazon.
- `rel` contient `nofollow sponsored` pour les liens rémunérés.
- Une divulgation est présente avant le premier lien affilié de chaque page concernée.

## AC-07 — Responsive et mode sombre

- Le tableau de confidentialité est consultable à 320, 360, 390 et 430 px sans élargir la page.
- Le tableau défile dans son propre conteneur si nécessaire.
- Les couleurs restent lisibles en mode sombre.
- Aucun débordement horizontal global.

## AC-08 — Accessibilité

- Les en-têtes du tableau utilisent des cellules `th`.
- Les liens possèdent un libellé explicite.
- Le focus clavier reste visible.
- Aucun `tabindex` positif.
- Le mouvement réduit reste respecté.

## AC-09 — Non-régression

- 13 pages conservées.
- Aucun style inline.
- CSS valide.
- JavaScript valide.
- Sitemap valide.
- Tous les actifs locaux existent.
- Menu mobile, mode sombre, correctif Asics, correctif mobile et contraste des raquettes conservés.

## AC-10 — Sortie automatisée minimale

```text
13 pages analysées
0 script AdSense actif
0 ressource DoubleClick active
13 beacons Cloudflare uniques
0 style inline
0 actif local manquant
CSS valide
JavaScript valide
Sitemap valide
```

## Condition de recette

Le lot est accepté si AC-01 à AC-10 passent, si aucune interface « Tout refuser » n’a été ajoutée au site et si l’activation AdSense reste explicitement conditionnée à la configuration faite dans le compte Google.
