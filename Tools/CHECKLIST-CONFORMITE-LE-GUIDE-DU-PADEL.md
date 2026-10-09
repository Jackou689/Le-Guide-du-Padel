# Checklist de conformité — Le Guide du Padel

**Version auditée :** lot 7D-4 styles/publicités  
**Date de l’audit :** 8 octobre 2026  
**Statut global :** publication en preview possible ; publication commerciale avec AdSense non recommandée avant correction des points bloquants.

> Cette checklist est une aide opérationnelle fondée sur l’état visible de l’archive et sur les recommandations officielles citées. Elle ne remplace pas une consultation juridique adaptée à la situation de l’éditeur.

## Légende

- [x] Conforme ou déjà présent
- [ ] À faire
- [!] Bloquant avant publication commerciale / AdSense
- [?] Information de l’éditeur nécessaire

---

## 1. Mentions légales

### État constaté

- [x] Page `mentions-legales.html` présente et accessible depuis le pied de page.
- [x] Nom du site et domaine indiqués.
- [x] Hébergeur identifié comme Cloudflare Pages, avec raison sociale et adresse.
- [x] Bureau d’enregistrement du domaine indiqué : IONOS.
- [x] Section propriété intellectuelle présente.
- [x] Section limitation de responsabilité présente.
- [!] L’identité de l’éditeur n’est pas indiquée : la page mentionne seulement une édition « à titre indépendant ».
- [!] L’adresse de l’éditeur n’est pas indiquée.
- [!] Le numéro de téléphone de contact n’est pas indiqué.
- [!] L’adresse électronique de contact n’est pas reproduite dans les mentions légales ; seule la page Contact est liée.
- [?] Déterminer si l’éditeur est une personne physique, une entreprise individuelle, une micro-entreprise, une société ou une association.
- [?] Selon ce statut, compléter les informations d’immatriculation, forme juridique, capital social, SIREN/SIRET, RCS/RNE ou autres mentions applicables.
- [ ] Ajouter le numéro de téléphone de l’hébergeur si requis et disponible dans les informations contractuelles officielles.
- [ ] Vérifier les crédits et droits de chaque image, illustration et photographie utilisée.

### Décision requise

Avant correction, recueillir auprès de l’éditeur :

1. statut juridique exact ;
2. nom et prénom ou dénomination sociale ;
3. adresse à publier selon le cadre applicable ;
4. adresse électronique ;
5. numéro de téléphone ;
6. SIREN/SIRET et informations d’immatriculation, le cas échéant ;
7. identité du directeur ou responsable de publication, si applicable.

---

## 2. Politique de confidentialité

### État constaté

- [x] Page `confidentialite.html` présente et accessible depuis le pied de page.
- [x] Référence générale aux droits d’accès, de rectification et de suppression.
- [x] Point de contact via la page Contact.
- [x] Section affiliation Amazon présente.
- [!] La politique affirme actuellement que le site « utilise Google AdSense », alors que l’archive contient seulement des placeholders et aucun script AdSense actif.
- [!] La politique affirme que des cookies publicitaires et de mesure d’audience sont susceptibles d’être déposés, sans inventaire précis des outils réellement actifs.
- [!] La politique ne décrit pas clairement le responsable de traitement.
- [!] Les finalités, bases légales, catégories de données, destinataires, durées de conservation et éventuels transferts hors UE ne sont pas détaillés.
- [!] Les modalités d’exercice des droits sont trop générales.
- [ ] Ajouter le droit de réclamation auprès de la CNIL.
- [ ] Ajouter une date d’entrée en vigueur et une date de dernière mise à jour.
- [ ] Ajouter une section distinguant clairement les services actifs aujourd’hui des services prévus ultérieurement.
- [?] Confirmer si Cloudflare Analytics, Google Analytics, Search Console, formulaires tiers, journaux de serveur ou autres outils collectent actuellement des données.

### Formulation provisoire recommandée avant activation d’AdSense

Indiquer qu’aucune annonce AdSense n’est actuellement chargée, et que la politique sera mise à jour avant l’activation de la publicité et des traceurs associés.

---

## 3. Cookies, traceurs et consentement

- [x] Le thème clair/sombre utilise `localStorage` pour mémoriser une préférence fonctionnelle.
- [ ] Documenter ce stockage local dans la politique de confidentialité.
- [!] Ne charger aucun traceur publicitaire, analytique non exempté ou tiers soumis au consentement avant le choix de l’utilisateur.
- [!] Prévoir une interface de consentement permettant d’accepter ou refuser avec le même niveau de facilité.
- [!] Prévoir un moyen permanent de modifier ou retirer le consentement.
- [!] Conserver une preuve du choix de consentement selon la solution CMP retenue.
- [!] Pour AdSense dans l’EEE, le Royaume-Uni et la Suisse, choisir une CMP certifiée par Google et compatible TCF.
- [ ] Définir les catégories : nécessaire, mesure d’audience, personnalisation, publicité et partenaires.
- [ ] Vérifier si les liens affiliés Amazon déposent eux-mêmes des traceurs uniquement après clic et adapter l’information.
- [ ] Ne pas précocher les catégories facultatives.
- [ ] Ne pas considérer la poursuite de navigation comme un consentement.

---

## 4. Google AdSense

### Avant demande ou activation

- [x] Emplacements de maquette présents et responsifs.
- [x] Les placeholders sont identifiés comme « Emplacement test » et ne prétendent plus diffuser une vraie annonce.
- [!] Masquer les placeholders sur le domaine public tant qu’AdSense n’est pas actif, ou les remplacer par les vraies unités au moment de l’intégration.
- [!] Ne pas intégrer le script AdSense avant mise en place de la CMP et mise à jour de la politique.
- [!] Configurer la rubrique « Confidentialité et messages » dans AdSense.
- [!] Choisir les fournisseurs de technologie publicitaire et les paramètres de personnalisation.
- [ ] Créer `ads.txt` uniquement à partir de la ligne exacte fournie dans le compte AdSense.
- [ ] Héberger `ads.txt` à la racine : `https://leguidedupadel.fr/ads.txt`.
- [ ] Vérifier l’accessibilité publique du fichier et attendre sa prise en compte par AdSense.
- [ ] Contrôler que les annonces ne masquent pas le contenu et ne provoquent pas de clics accidentels.
- [ ] Contrôler CLS, LCP et affichage mobile après activation réelle.
- [ ] Vérifier les règles AdSense relatives au contenu et au placement avant publication.

---

## 5. Affiliation Amazon

### État constaté

- [x] Les liens Amazon inspectés comportent `rel="nofollow sponsored"`.
- [x] Les liens affiliés s’ouvrent dans un nouvel onglet.
- [x] L’identifiant d’affiliation `leguidedupade-21` est utilisé dans les liens examinés.
- [x] La page À propos explique le modèle d’affiliation.
- [x] La politique de confidentialité contient la mention Partenaire Amazon.
- [x] Plusieurs articles affichent une mention « Lien affilié (sans surcoût pour vous) » près des liens.
- [!] Harmoniser une divulgation visible avant le premier lien affilié sur chaque article concerné.
- [!] Vérifier que tous les articles avec liens Amazon comprennent la formulation exigée par le programme Partenaires Amazon.
- [ ] Éviter toute garantie absolue de prix, disponibilité, performance ou supériorité produit.
- [ ] Vérifier périodiquement les liens produits et les informations tarifaires.
- [ ] Conserver une séparation éditoriale claire entre recommandations et rémunération.

### Pages avec liens Amazon détectées

- `balles-padel-guide.html`
- `chaussures-padel-guide.html`
- `coups-techniques-padel.html`
- `echauffement-padel.html`
- `guide-raquette-padel-debutant.html`
- `raquette-padel-tendinite.html`
- `regles-du-padel.html`
- `tactique-filet-padel.html`

---

## 6. Contenus santé et sécurité

- [!] Ajouter un avertissement clair sur `raquette-padel-tendinite.html` indiquant que le contenu est informatif et ne remplace pas l’avis d’un professionnel de santé.
- [!] Ajouter un avertissement adapté sur `echauffement-padel.html`.
- [!] Ajouter une recommandation de consulter rapidement en cas de douleur persistante, importante, traumatisme, gonflement ou perte de fonction.
- [!] Réviser les formulations médicales absolues ou non sourcées.
- [!] Éviter de présenter un changement de matériel comme traitement d’une tendinite.
- [!] Éviter les affirmations telles que « absorbe la quasi-totalité des chocs », « référence absolue », « cause numéro un » ou « entorse assurée » sans source fiable.
- [ ] Distinguer prévention, confort, hypothèses mécaniques et prise en charge médicale.
- [ ] Ajouter des sources fiables lorsque des données médicales, biomécaniques ou épidémiologiques sont avancées.
- [ ] Vérifier la cohérence des recommandations de poids, de mousse et d’équilibre avec des sources identifiables.

---

## 7. Exactitude éditoriale et transparence

- [x] Page À propos présente.
- [x] Mission éditoriale et modèle économique expliqués.
- [!] L’expression « notre collectif de passionnés » doit correspondre à une réalité vérifiable ; sinon la remplacer par une formulation exacte.
- [!] Plusieurs pages indiquent « Publié par la Rédaction du Guide du Padel » : vérifier qu’une rédaction identifiable existe réellement.
- [!] Une page indique « Publié le 4 octobre 2026 » : conserver cette date uniquement si elle correspond à la date réelle de publication.
- [ ] Ajouter une politique de correction ou une phrase invitant au signalement des erreurs.
- [ ] Ajouter une date de dernière mise à jour aux articles lorsque le processus éditorial permet de la maintenir.
- [ ] Sourcer les affirmations historiques, réglementaires, médicales et techniques importantes.
- [ ] Vérifier les règles sportives susceptibles d’évoluer, notamment le point décisif, le jeu en simple et les règles de compétition.
- [ ] Vérifier les promesses de prix et descriptions produits, susceptibles de devenir obsolètes.

---

## 8. Contact et droits des utilisateurs

- [x] Page Contact présente.
- [x] Adresse `contact@leguidedupadel.fr` affichée.
- [ ] Rendre l’adresse cliquable avec un lien `mailto:`.
- [ ] Vérifier que la boîte électronique est active, surveillée et sécurisée.
- [ ] Définir une procédure pour traiter les demandes RGPD.
- [ ] Documenter les durées de conservation des échanges par courriel.
- [ ] Éviter de promettre un délai de réponse de 48 à 72 heures si ce délai ne peut pas être tenu régulièrement.

---

## 9. Propriété intellectuelle

- [!] Dresser l’inventaire des images : origine, licence, auteur, preuve d’autorisation et conditions d’attribution.
- [!] Vérifier particulièrement les images chargées depuis Unsplash et les photographies de produits.
- [ ] Ajouter les crédits obligatoires lorsque les licences l’exigent.
- [ ] Vérifier les droits d’utilisation des logos, marques et visuels de produits.
- [ ] Conserver les preuves de licence et les fichiers sources.
- [ ] Vérifier que les textes ne reprennent pas de contenu protégé provenant de fabricants ou d’autres médias.

---

## 10. Sécurité et infrastructure

- [x] Site prévu en HTTPS via Cloudflare.
- [x] `robots.txt` et `sitemap.xml` présents.
- [x] Configuration de preview Wrangler présente.
- [ ] Vérifier les en-têtes de sécurité en production : CSP, `X-Content-Type-Options`, `Referrer-Policy`, protection contre l’intégration en iframe.
- [ ] Vérifier qu’aucun secret, jeton ni identifiant privé n’est commité dans le dépôt.
- [ ] Supprimer `.DS_Store` du dépôt et l’ajouter à `.gitignore`.
- [ ] Vérifier les dépendances tierces et les scripts externes avant chaque intégration.
- [ ] Prévoir une sauvegarde et une procédure de restauration.

---

## 11. Accessibilité

- [x] Navigation mobile avec attributs ARIA et gestion clavier.
- [x] Focus visible et préférence de réduction des animations.
- [x] Textes alternatifs présents pour les images inspectées.
- [ ] Tester le contraste de toutes les nouvelles classes, en particulier en mode sombre.
- [ ] Vérifier les titres et la hiérarchie au lecteur d’écran.
- [ ] Tester menu, filtres et thème uniquement au clavier.
- [ ] Vérifier le zoom à 200 % et 400 %.
- [ ] Vérifier les tableaux du guide raquette sur petit écran et au lecteur d’écran.
- [ ] Ajouter `aria-current="page"` aux navigations principale et mobile lorsque pertinent.
- [ ] Tester avec VoiceOver sur macOS/iOS et NVDA sur Windows.

---

## 12. SEO et publication

- [x] Canonical, métadonnées sociales et JSON-LD présents.
- [x] Sitemap présent et cohérent avec les principales pages éditoriales.
- [x] Open Graph et X/Twitter configurés.
- [ ] Vérifier le domaine public définitif dans toutes les URL absolues.
- [ ] Soumettre le sitemap dans Google Search Console après ouverture publique.
- [ ] Tester les données structurées après publication.
- [ ] Vérifier les aperçus sociaux après purge éventuelle des caches.
- [ ] Mesurer Lighthouse et le LCP après mise en ligne de la preview stable.
- [ ] Vérifier qu’aucune page de preview n’est indexée par erreur.

---

## 13. Nettoyage avant production

- [!] Masquer ou retirer les placeholders « Emplacement test » avant ouverture publique sans AdSense.
- [ ] Retirer les anciens rapports `.md` de l’artefact public, ou les conserver hors du dossier servi.
- [ ] Mettre à jour `LISEZMOI.txt`, qui mentionne encore Netlify et des tâches déjà réalisées.
- [ ] Supprimer `.DS_Store`.
- [ ] Vérifier qu’aucun fichier de travail, capture ou archive ZIP n’est servi publiquement.
- [ ] Vérifier l’absence de liens de preview dans les pages publiques.
- [ ] Effectuer un crawl final des liens internes et externes.

---

# Ordre recommandé

## Bloquants avant publication publique commerciale

1. Compléter les mentions légales avec l’identité et les coordonnées correspondant au statut réel.
2. Corriger la politique de confidentialité pour refléter les services réellement actifs.
3. Ajouter les avertissements santé et neutraliser les affirmations trop absolues.
4. Harmoniser la divulgation d’affiliation sur les huit articles concernés.
5. Auditer les droits des images.
6. Masquer les placeholders de test sur le domaine public.

## Bloquants avant AdSense

1. Mettre en place une CMP certifiée Google et compatible TCF.
2. Bloquer les traceurs soumis au consentement avant le choix.
3. Mettre à jour la politique de confidentialité avec les traitements réels.
4. Ajouter `ads.txt` avec la référence exacte du compte.
5. Remplacer les placeholders par les vraies unités publicitaires.
6. Tester consentement, refus, retrait, mobile, CLS et LCP.

## Améliorations après ouverture

1. Politique de correction et dates de mise à jour.
2. Sources éditoriales plus systématiques.
3. Tests d’accessibilité avancés.
4. En-têtes de sécurité.
5. Mesure continue des Core Web Vitals.
