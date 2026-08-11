# Analyse Sociodémographique des Étudiants d'OpenClassrooms (Parcours Data)

## 📌 À propos du projet

Ce projet consiste en une analyse exploratoire et comparative du profil sociodémographique des étudiants inscrits aux parcours Data chez OpenClassrooms sur la période **2022 à 2025**[cite: 17]. 

L'objectif est d'étudier l'évolution des profils des étudiants (selon le genre, la tranche d'âge et la région d'origine)[cite: 17] et de mettre ces données en perspective avec les statistiques démographiques nationales françaises[cite: 17].

---

## 🎯 Enjeux et Objectifs

* **Comprendre l'évolution des inscriptions :** Analyser les tendances d'attractivité des parcours Data au fil des 4 dernières années[cite: 17].
* **Mesurer la diversité et la parité :** Évaluer la représentation des femmes et des différentes tranches d'âge dans ces formations[cite: 17, 17].
* **Inclusion territoriale :** Identifier les régions sous-représentées par rapport à la population réelle[cite: 17, 17].
* **Aide à la décision stratégique :** Proposer des recommandations ciblées pour renforcer la mixité, le rajeunissement du public et la couverture régionale[cite: 17, 17].

---

## 📊 Sources de Données

Le projet croise deux sources de données principales :

1. **Données internes OpenClassrooms (2022-2025)**[cite: 17]
   * **Périmètre :** Inscriptions aux parcours Data Analyst (4 647 inscriptions brutes / 4 010 étudiants uniques)[cite: 17].
   * **Variables clés :** `USER_ID`, `PATH_CATEGORY_NAME`, `AGE_GROUP`, `GENDER`, `REGION`, `YEAR_PATH_STARTED`[cite: 17].

2. **Données publiques INSEE (2022-2025)**[cite: 17]
   * **Périmètre :** Référentiel annuel de la population démographique régionale française[cite: 17].
   * **Variables clés :** `ANNEE`, `REGION`, `SEXE`, `AGE`, `POPULATION`[cite: 17].

---

## ⚙️ Pipeline Technique & Infrastructure Data

Le traitement, le nettoyage et la modélisation des données s'appuient sur une architecture Modern Data Stack :

```text
Data Brutes (OC + INSEE) ──> Snowflake (Ingestion/Raw) ──> dbt Cloud (Transformation/Pipeline) ──> Table Finale (Mart)
```[cite: 17]

* **Snowflake :** Entrepôt de données (Data Warehouse) pour l'ingestion des tables brutes (`raw_data`)[cite: 17, 17].
* **dbt Cloud :** Structuration du pipeline en 4 couches successives[cite: 17] :
  1. `RAW` : Données brutes[cite: 17].
  2. `STAGING` : Nettoyage, gestion des valeurs manquantes (`NULL` → *'Non renseigné'*) et normalisation[cite: 17].
  3. `INTERMEDIATE` : Harmonisation des tranches d'âge et des noms de régions[cite: 17].
  4. `MART` : Génération de la table finale pour analyse (`mart_population_etudiants`)[cite: 17].

---

## 🔒 Conformité RGPD et Qualité

* **Minimisation des données :** Aucune donnée directement identifiante (nom, prénom, email) n'est conservée[cite: 17].
* **Anonymisation :** Les données sont analysées par tranches d'âge et agrégées[cite: 17].
* **Qualité automatisée :** Intégration de tests dbt automatiques (`unique`, `not_null`, `accepted_values`) garantissant l'intégrité des résultats[cite: 17].

---

## 💡 Principaux Constats & Recommandations

* **Profil Type :** Majoritairement masculin, résidant en Île-de-France, et âgé de 25 à 39 ans[cite: 17].
* **Objectifs Stratégiques :**
  * *Féminisation :* Porter la part des femmes au-delà de 40 % à court terme (target parité à 50/50 à moyen terme) via des partenariats ciblés[cite: 17].
  * *Territoires :* Développer des partenariats régionaux (ex: GRETA, régions) pour dynamiser les zones sous-représentées[cite: 17].
  * *Rajeunissement :* Renforcer la présence auprès des universités et lycées[cite: 17].
