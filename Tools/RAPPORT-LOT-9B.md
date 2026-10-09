# Rapport du lot 9B

## Objet
Optimisation prudente des performances et du SEO technique à partir du lot 9A, sans modification esthétique.

## Modifications
- versionnement des ressources en `style.css?v=9B` et `script.js?v=9B` sur les 14 pages ;
- ajout de `defer` au script fonctionnel local ;
- ajout des dimensions intrinsèques manquantes sur les images locales ;
- ajout de `decoding="async"` aux images qui ne le précisaient pas ;
- conservation de `loading="eager"` et `fetchpriority="high"` sur les images principales des articles ;
- conservation du chargement différé des images secondaires ;
- ajout des dimensions et du type de l’image Open Graph 1200 x 630 ;
- suppression des métadonnées macOS `.DS_Store` de l’artefact ;
- validation des titres, descriptions, canoniques, Open Graph, JSON-LD, sitemap et robots.txt.

## Décisions de prudence
Le CSS n’a pas été réécrit ni dédupliqué dans ce lot afin de ne pas provoquer de nouvelle régression visuelle. Les mesures réelles LCP, INP et CLS devront être confirmées sur la preview puis en production dans PageSpeed Insights et Search Console.

## Références de recette
Objectifs Core Web Vitals : LCP <= 2,5 s, INP < 200 ms et CLS < 0,1.
