# DATAImmo — Création et Exploitation de la Base de Données Immobilières

[![Projet](https://img.shields.io/badge/Projet-DATAImmo-blue.svg)](#)
[![Auteur](https://img.shields.io/badge/Auteur-Arnaud_MELOEN-orange.svg)](#)
[![Organisation](https://img.shields.io/badge/Entreprise-Laplace_Immo-red.svg)](#)
[![Technos](https://img.shields.io/badge/Tech-SQL%20%7C%20Relational%20DB%20%7C%20Data%20Analysis-brightgreen.svg)](#)

---

## 📌 1. Présentation du Projet

**DATAImmo** est une initiative stratégique portée par le réseau immobilier national **Laplace Immo**. 

L'objectif principal du projet est de transformer le réseau d'agences en un **leader technologique de l'immobilier** grâce à une exploitation rigoureuse et centralisée des données de transactions immobilières françaises.

Pour tout nouvel utilisateur ou collaborateur n'ayant pas de contexte préalable, ce projet consiste à :
1. **Centraliser et structurer** des millions d'informations d'achats/ventes de biens immobiliers sur le territoire français.
2. **Concevoir un système d'information décisionnel** capable de répondre avec précision aux besoins d'analyses stratégiques locales et nationales.
3. **Préparer le terrain pour l'innovation technologique** (notamment le développement futur de modèles d'intelligence artificielle / Machine Learning pour l'estimation automatique du prix de vente des biens).

---

## 🎯 2. Enjeux Stratégiques et Métier

Dans un marché immobilier très concurrentiel, la donnée est devenue l'actif le plus précieux pour guider la décision des acquéreurs, vendeurs et conseillers immobiliers.

* **Modernisation & Centralisation :** Refonte globale et structuration d'une base de données relationnelle unique regroupant les transactions immobilières nationales.
* **Aide à la décision & Intelligence de marché :** Fournir aux agences régionales du réseau Laplace Immo des outils d'analyse pointus pour suivre les tendances de prix au mètre carré, la typologie des ventes et le dynamisme territorial.
* **Innovation & Modélisation prédictive :** Créer un socle de données fiable et nettoyé destiné à alimenter des algorithmes prédictifs capables d'estimer avec précision la valeur d'un bien en fonction de ses caractéristiques physiques et démographiques.
* **Conformité & Sécurité :**
  * **Conformité RGPD :** Suppression systématique des noms d'acquéreurs et vendeurs pour garantir l'anonymat et l'absence de données personnelles sensibles.
  * **Stratégie de sauvegarde :** Mise en place de protocoles de sauvegardes régulières (sauvegardes externes / sécurisées) pour assurer la pérennité de la base de données.

---

## 📊 3. Origine et Nature des Données

La base de données rassemble et croise trois sources d'informations publiques et officielles (Open Data) :

1. **DVF (Demandes de Valeurs Foncières) :** Publiées par la DGFiP (Direction Générale des Finances Publiques), ces données répertorient l'ensemble des transactions immobilières (mutations) réalisées en France, incluant la date de vente, la valeur foncière, la surface réelle, le nombre de pièces, etc.
2. **INSEE (Institut National de la Statistique et des Études Économiques) :** Résultats des recensements de la population permettant d'enrichir la base avec le nombre total d'habitants par commune.
3. **data.gouv.fr (Référentiel géographique national) :** Données administratives officielles permettant de lier chaque commune à son département et à sa région.

---

## 🗄️ 4. Architecture et Schéma Relational (MCD / MLD)

Pour éviter la redondance d'informations et garantir les performances des requêtes, les données ont été modélisées de manière relationnelle normalisée (3ème Forme Normale).

```
[ Region ] (1,N) <---- (1,1) [ Departement ] (1,N) <---- (1,1) [ Commune ]
                                                                   |
                                                                 (1,N)
                                                                   |
                                                                 (1,1)
                                 [ Ventes ] (1,1) ----> (1,N) [ Biens ]
```

### Structure des tables principales :

* **`Region`** :
  * `reg_code` (PK, VARCHAR) : Code unique de la région.
  * `reg_nom` (VARCHAR) : Nom officiel de la région.
* **`Departement`** :
  * `dep_code` (PK, VARCHAR) : Code du département (ex: '75', '13', '06').
  * `reg_code` (FK, VARCHAR) : Lien vers la région d'appartenance.
  * `dep_nom` (VARCHAR) : Nom du département.
* **`Commune`** :
  * Clé primaire composite (`dep_code`, `com_code`) pour garantir l'unicité au niveau national.
  * `com_nom` (VARCHAR) : Nom de la commune.
  * `population` (INTEGER) : Population totale de la commune (INSEE).
* **`Biens`** :
  * `id_bien` (PK, INTEGER AUTOINCREMENT) : Identifiant unique du bien immobilier.
  * `adresse` (VARCHAR) : Adresse complète (concaténation du numéro, type et nom de voie).
  * `surface` (REAL) : Surface réelle bâtie en m² (choix de la surface réelle au lieu de la surface Carrez).
  * `nb_piece` (INTEGER) : Nombre de pièces principales.
  * `type_local` (INTEGER) : Type de bien (1 = Maison, 2 = Appartement).
  * `1er_lot` (INTEGER) : Premier lot de copropriété (permet de différencier les appartements d'un même immeuble).
  * `dep_code`, `com_code` (FK) : Localisation du bien.
* **`Ventes`** :
  * `id_vente` (PK, INTEGER AUTOINCREMENT) : Identifiant unique de la transaction.
  * `id_bien` (FK, INTEGER) : Clé étrangère pointant vers le bien vendu.
  * `date_mutation` (DATE) : Date de la vente (ex: YYYY/MM/DD).
  * `valeur_fonciere` (NUMERIC/REAL) : Montant de la transaction en euros.

---

## 🔎 5. Exemples d'Analyses et Requêtes SQL Clés

Le projet inclut une série de requêtes complexes permettant d'extraire des indicateurs clés pour la direction générale et les agences régionales :

* **Volume de ventes :** Calcul du nombre total d'appartements vendus en France au 1er semestre 2020 (ex: 31 378 appartements).
* **Répartition géographique :** Ventilation des ventes d'appartements par région (l'Île-de-France arrivant largement en tête avec plus de 13 900 ventes).
* **Analyse par typologie de bien :** Répartition des ventes en fonction du nombre de pièces (ex: les T2 et T3 représentent plus de 59% du marché des appartements).
* **Prix au m² par département :** Top 10 des départements les plus chers de France (Paris, Hauts-de-Seine, Val-de-Marne, Alpes-Maritimes, etc.).
* **Indicateurs de valeur :**
  * Prix moyen au m² d'une maison en Île-de-France.
  * Impact de la typologie sur la valeur : Écart de prix au m² entre un T2 et un T3 (-13.13%).
  * Prix au m² des grands appartements (> 4 pièces) par région.
* **Dynamisme immobilier local :** Top 20 des communes de plus de 10 000 habitants présentant le plus fort taux de transactions pour 1 000 habitants.
* **Suivi temporel :** Analyse de l'évolution du volume des transactions entre le 1er trimestre et le 2d trimestre 2020 (+3.68%).

---

## 🚀 6. Guide d'Installation et Exécution

### Prérequis
* Un SGBD compatible SQL (SQLite, PostgreSQL, MySQL ou MariaDB).
* Un outil d'administration de base de données (ex: DBeaver, DB Browser for SQLite, pgAdmin).

### Étapes de mise en place

1. **Création de la base et import du schéma :**
   Exécuter le script SQL principal de création des tables et contraintes de clés étrangères :
   ```sql
   -- Exemple d'exécution du fichier script
   SOURCE P5_creation_table_et_insertions_donnees.sql;
   ```

2. **Alimentation des données :**
   Les données brutes chargées depuis les fichiers DVF, INSEE et Geofla sont intégrées et transformées dans les tables normalisées (`Region`, `Departement`, `Commune`, `Biens`, `Ventes`).

3. **Exécution des requêtes d'analyse :**
   Exécuter les requêtes analytiques contenues dans les fichiers SQL dédiés pour générer les rapports d'activité.

---

## 👨‍💻 Auteur & Crédits

* **Auteur :** Arnaud MELOEN
* **Projet réalisé pour :** Laplace Immo
* **Année :** 2026
