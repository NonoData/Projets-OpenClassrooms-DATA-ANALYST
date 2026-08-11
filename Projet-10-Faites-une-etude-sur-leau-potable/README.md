# 🚰 DWFA — Drinking Water For All
### Tableau de bord décisionnel pour l'accès mondial à l'eau potable

Bienvenue sur le dépôt du projet **Drinking Water For All (DWFA)**. 

Ce document a été conçu pour vous expliquer clairement **ce qu'est le projet**, **les enjeux humanitaires et stratégiques auxquels il répond**, ainsi que **les données utilisées**, de manière simple et accessible à tous, même sans compétences techniques préalables.

---

## 🎯 1. Qu'est-ce que ce projet ?

**Drinking Water For All (DWFA)** est un projet d'analyse de données et d'aide à la décision. Il s'appuie sur la création d'un **tableau de bord interactif développé sur Power BI** [cite: 9].

### L'objectif principal
L'objectif est d'**identifier et de prioriser les pays qui ont le plus besoin d'aide** en matière d'accès à l'eau potable [cite: 9], afin de guider les investissements, les interventions humanitaires ou les prestations de conseil gouvernemental [cite: 9].

### Les 3 domaines d'expertise visés
Pour répondre aux besoins spécifiques de chaque région, l'analyse classe les opportunités selon 3 axes d'action [cite: 9] :
1. **Création de services** : Déployer de nouvelles infrastructures là où l'accès à l'eau est critique ou inexistant [cite: 9].
2. **Modernisation des services** : Améliorer et pérenniser les réseaux existants (notamment face à l'urbanisation) [cite: 9].
3. **Consulting gouvernemental** : Accompagner les gouvernements dans la mise en place de politiques publiques efficaces et stables [cite: 9].

---

## 💡 2. Quels sont les enjeux ?

L'accès à une eau propre et sûre est un droit humain fondamental. Pourtant, des centaines de millions de personnes en sont encore privées, entraînant de graves conséquences sanitaires et économiques [cite: 9].

### Les grands défis :
* **🏥 Un enjeu de santé publique** : L'eau insalubre est directement responsable de maladies graves et de décès prévitables, en particulier chez les populations les plus vulnérables [cite: 9].
* **🌍 Un enjeu de justice géographique** : Il existe de fortes disparités d'accès à l'eau entre les continents, les zones urbaines et les zones rurales [cite: 9].
* **🏛️ Un enjeu de gouvernance et de stabilité** : Les projets d'infrastructure nécessitent un contexte politique stable pour être pérennes et efficaces [cite: 9].
* **📊 Un enjeu d'aide à la décision** : Il est souvent difficile pour une organisation de savoir *où* investir ses ressources en priorité. Ce tableau de bord permet de croiser santé, géographie et politique pour décider de manière objective [cite: 9].

---

## 🗂️ 3. Les Données Utilisées

Pour obtenir une vision globale et précise, nous croisons des données officielles provenant d'organisations internationales reconnues (FAO, OMS, Banque Mondiale) sur une période allant de **2000 à 2018** [cite: 9].

### A. Les sources de données
1. **Population (FAO — 2000 à 2018)** : Permet de connaître le nombre d'habitants par pays, ainsi que la répartition entre zones urbaines et rurales [cite: 9].
2. **Accès à l'eau potable (OMS — 2000 à 2017)** : Mesure la proportion de la population disposant d'un accès à une eau gérée en toute sécurité, d'un service basique ou n'ayant aucun accès [cite: 9].
3. **Mortalité liée à l'eau (OMS — 2016)** : Donne le taux de mortalité et le nombre de décès dus aux services d'eau, d'assainissement et d'hygiène insalubres (WASH) [cite: 9].
4. **Stabilité politique (Banque Mondiale — 2000 à 2018)** : Évalue la stabilité du gouvernement et la gouvernance locale [cite: 9].

---

## 🛠️ 4. Préparation et Traitement des Données

Afin de pouvoir analyser ces données ensemble de manière cohérente, plusieurs étapes de nettoyage et de préparation ont été réalisées [cite: 9] :
* **Harmonisation des noms de pays** : Correction des divergences d'écriture entre les bases de données (ex: *Republic of North Macedonia* remplaçant *North Macedonia*, nettoyage des parenthèses dans des noms comme *Iran* ou *Bolivie*) [cite: 9].
* **Pondération des chiffres** : Conversion des effectifs de population (exprimés initialement en milliers) en nombres réels pour garantir la justesse des calculs [cite: 9].
* **Clé de jointure unique (`country_year`)** : Création d'une identifiant combinant le nom du pays et l'année pour pouvoir relier précisément toutes les sources de données [cite: 9].
* **Modélisation en étoile** : Structuration des tables (`df_water_clean`, `df_pop_clean`, `df_mortality_clean`, `df_stability_clean`, `df_geo_clean`) reliées autour d'une architecture claire pour optimiser les performances d'affichage [cite: 9].

---

## 📈 5. Indicateurs Clés de Performance (KPIs)

Le tableau de bord permet de suivre en temps réel plusieurs indicateurs majeurs [cite: 9] :
* **Population mondiale** (en milliards) et répartition ville/campagne [cite: 9].
* **Taux d'accès à l'eau potable** (% ayant un service sûr/basique) [cite: 9].
* **Taux de population sans accès à l'eau potable** [cite: 9].
* **Taux de mortalité lié à l'eau insalubre** (nombre de décès pour 100 000 habitants) et nombre total de morts [cite: 9].
* **Indice de stabilité & efficacité politique** [cite: 9].

---

## 🖥️ 6. Vues du Tableau de Bord Power BI

Le tableau de bord offre **3 échelles de lecture complémentaires** [cite: 9] :
1. **Vue Mondiale** : Cartes et graphiques globaux montrant les disparités entre les continents [cite: 9].
2. **Vue Continentale** : Analyse comparative des régions pour observer l'évolution de l'accès à l'eau et de la stabilité politique [cite: 9].
3. **Vue Nationale / Pays** : Zoom détaillé par pays pour guider le choix parmi les 3 axes d'intervention (Création, Modernisation, Consulting) [cite: 9].

---

## 🚀 7. Pourquoi Power BI ?

Le choix de l'outil **Microsoft Power BI** s'est imposé pour deux raisons majeures [cite: 9] :
* **Intégration facile** dans l'écosystème applicatif des entreprises [cite: 9].
* **Ergonomie et simplicité d'utilisation** permettant à des décideurs non-techniciens de manipuler les cartes et graphiques de manière intuitive [cite: 9].

---

### 🌐 Lien vers le livrable
Les différents documents et la restitution complète du projet sont consultables directement sur la page suivante :  
👉 [**Livrable DWFA**](https://nonodata.github.io/)
