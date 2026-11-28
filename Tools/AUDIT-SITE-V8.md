# Audit complet du site — v8 (format production-audit)

**Verdict : 82/100. Prêt pour l'aperçu et pour une mise en ligne, aucun bloquant technique ; 6 points à traiter avant d'ouvrir à Google et à AdSense, dont 3 dépendent de toi (images, droits des images, informations d'auteur).**

Périmètre : 14 pages, 3 feuilles de style, 1 script, 114 fichiers d'images et de polices, en-têtes et robots. Méthode : captures dans Chromium (clair, sombre, mobile, bureau, 320 à 1440 px), mesures de performance locales, analyse statique du HTML et du CSS. Skills : *production-audit*, *seo*, *accessibility-review*, *design-critique*, *design-system*, *benchmark*, *browser-qa*.

## Bloquants
Aucun bloquant technique. Points de lancement à lever (ils ne cassent rien mais exposent à un risque) :
1. **Droits des images** : confirmer l'origine de `bandeja.webp` et des photos produit (`head_evo`, `adipower`, `babolat_contact`, `dunlop_titan`, `wilson_optix`, `asicsgel`). Une image filigranée d'une banque d'images a déjà été retirée de l'article Règles ; il faut s'assurer qu'il n'en reste pas d'autre.
2. **Visuels de remplacement** : 11 illustrations d'accueil et les visuels incrustés de texte (Raquette débutant, Tendinite, Techniques) sont toujours ceux d'avant la refonte.
3. **Emplacements publicitaires** : les « Emplacement test » doivent avoir disparu en production (ils ne sont affichés que sur les adresses `workers.dev` et `localhost`).

## Correctifs à forte valeur, par ordre
1. **Images** (les tiens) : remplacer les visuels, puis ajouter des tailles responsives (`srcset`) aux 6 images servies trop grandes (gain estimé : environ 0,7 Mo).
2. **Identité éditoriale (E-E-A-T)** : ajouter un nœud `Organization` au niveau du site et, pour les deux guides santé, un relecteur ou une mention de méthode. Aujourd'hui l'éditeur n'existe que dans le balisage `Article`.
3. **Produits** : vérifier les noms et les liens (18 liens Amazon : 16 vers des recherches, 2 vers une fiche précise) ; « Asics Gel-Dedicate Clay » et « Asics Gel-Resolution Padel » ressemblent à des modèles de tennis.
4. **Politique de confidentialité** : elle cite AdSense, Cloudflare, les cookies et Amazon, mais pas explicitement les droits des personnes (accès, rectification, suppression), la durée de conservation ni le contact pour les exercer.
5. **Publicité réelle** : réserver la hauteur des emplacements AdSense (hauteur minimale) pour éviter un décalage de mise en page quand les annonces s'affichent en production.
6. **Dépôt allégé** : 35 fichiers non référencés (3,9 Mo) dont `logo-concept-a.png` (1,7 Mo) et 2 groupes de doublons exacts ; à retirer après ton accord (rien n'a été supprimé).
7. **CSS** : 61 % de `style.css` n'est pas utilisé dans l'état par défaut (hors survol, menu, mode sombre) ; ≈ 770 `!important` empilés ; aucune minification. Suite possible : test avec états, couche unique, minification au déploiement.
8. **Maillage dans le corps des articles** : Tactique (3), Techniques (4), Tendinite (4) et À propos (1) reçoivent peu de liens depuis le texte ; viser 6 à 8.
9. **Lisibilité** : Échauffement, Chaussures et Tendinite ont des phrases de 23 à 25 mots en moyenne ; réécriture à décider avec toi.
10. **Détails** : 2 sauts de niveau de titre (Chaussures, Tendinite) ; `llms.txt` absent ; `lastmod` absent de 5 URL du sitemap ; en-tête HSTS absent du fichier `_headers` (à activer côté Cloudflare).

## Scores par domaine
| Domaine | Score | Preuves principales |
|---|---|---|
| SEO technique | 17/20 | 13 pages indexables toutes dans le sitemap ; titres ≤ 60 caractères et descriptions de 70 à 160, sans doublon ; canoniques absolus ; image sociale 1200×630 présente ; JSON-LD valide sur 14 pages, `Article` daté sur les 8 guides ; `robots.txt`, `ads.txt` et `_redirects` présents. Manques : `Organization`, `llms.txt`, maillage dans le corps |
| Accessibilité | 14/15 | 0 contraste insuffisant (clair et sombre, 14 pages) ; focus visible partout ; aucun défilement horizontal de 320 à 1440 px et à 200 % ; menu mobile : `aria-expanded`, Échap ferme et rend le focus, contenu inerte quand fermé ; bascule de thème au rôle `switch` ; lien d'évitement fonctionnel ; filtres avec `aria-pressed`. Manque : essai avec un vrai lecteur d'écran |
| Performance | 12/15 | CLS 0 ; LCP local ≤ 0,33 s ; page médiane 582 Ko (13 requêtes) ; polices 60 Ko préchargées. Manques : CSS ≈ 250 Ko bruts sans minification, images trop grandes, pas de format AVIF |
| Contenu | 11/15 | 8 guides de 1 100 à 1 750 mots, FAQ ajoutées, dates, sources santé ; formulations de santé mesurées. Manques : 3 pages d'achat encore courtes, lisibilité, visuels à remplacer |
| Légal et confiance | 12/15 | Mention d'affiliation sur toutes les pages avec liens Amazon ; 18 liens `rel="sponsored"` ; mentions légales complètes ; CSP, `nosniff`, politique de référent et de permissions en place. Manques : droits RGPD, auteur nommé, droits des images |
| Design et UX | 8/10 | Typographie en 3 familles, palette sur jetons, 14 pages cohérentes en clair et en sombre, 0 régression visuelle. Manques : 141 jetons historiques à réduire, 155 couleurs `rgba()` en dur, pages légales moins travaillées |
| Exploitation | 8/10 | Jeux d'en-têtes de sécurité, cache versionné, 404 non mise en cache. Manques : HSTS, fichiers inutiles, vérification de la production |
**Total : 82/100.**

## Critique de design (skill design-critique)
- **Ce qui fonctionne** : hiérarchie nette (bandeaux de titres, sommaire en cartes, barre latérale utile), couleurs à sens unique, mode sombre complet, bouton vert d'appel à l'action cohérent avec le logo.
- **Ce qui reste faible** : les illustrations vectorielles de l'accueil (hors sujet des visuels attendus), les visuels de texte incrusté, trois produits sans photo dans Tendinite, les pages Contact, Confidentialité et Mentions légales, simples.
- **Défaut trouvé et corrigé pendant l'audit** : texte souligné transformé en pastille ronde sur la page Tactique.

## Preuves examinées
56 captures avant et après chaque étape ; mesures de performance sur 14 pages en bureau et mobile ; analyse de 3 feuilles de style (1 412 règles, 303 couleurs avant consolidation) ; rendu réel des polices par glyphe ; 14 pages en clair et en sombre à 5 largeurs ; liens internes (703) et sortants (18 Amazon, Ameli, FIP, FFT, CNIL…) ; en-têtes, sitemap, robots, redirections, JSON-LD.

## Preuves manquantes
Audit en ligne par le plugin SEO et GEO (il lit le site déployé) ; mesures réelles de vitesse (PageSpeed, données de terrain) ; Search Console ; essai avec VoiceOver ou NVDA ; vérification des liens externes (hors connexion) ; relecture des règles du programme Partenaires Amazon et d'AdSense ; justificatifs de droits des images.

## Prochaine action
Envoie-moi les images (liste dans le journal de la v5) et colle l'adresse de l'aperçu en texte dans le chat : j'intègre les visuels, puis je lance l'audit en ligne et je traite les points 1 à 4.
