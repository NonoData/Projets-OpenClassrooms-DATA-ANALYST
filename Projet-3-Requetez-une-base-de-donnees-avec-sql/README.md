# Projet : Requêter une base de données avec SQL

Ce projet présente la méthodologie et la mise en œuvre pratique pour la conception, la création, le chargement et le requêtage d'une base de données relationnelle SQLite contenant des données d'assurance (`Contrat`) et de géographie (`Region`).

---

## 📌 Sommaire
1. [Aperçu de la Méthodologie](#-aperçu-de-la-méthodologie)
2. [Étape 1 : Découverte des données & Dictionnaire de données](#étape-1--découverte-des-données--dictionnaire-de-données)
3. [Étape 2 : Conception du schéma relationnel (MCD/MLD)](#étape-2--conception-du-schéma-relationnel-mcdmld)
4. [Étape 3 : Création et Chargement de la Base de Données](#étape-3--création-et-chargement-de-la-base-de-données)
5. [Étape 4 : Rédaction et Exécution de Requêtes SQL](#étape-4--rédaction-et-exécution-de-requêtes-sql)
6. [Outils Utilisés](#-outils-utilisés)

---

## 🛠 Aperçu de la Méthodologie

Le projet suit une démarche structurée en **4 étapes clés** :
* **Étape 1 :** Prise en main des données brutes (fichiers CSV) et élaboration du dictionnaire de données.
* **Étape 2 :** Modélisation et conception du schéma relationnel sous **SQL Power Architect**.
* **Étape 3 :** Génération du script DDL (SQLite) et chargement des données sous **DBeaver**.
* **Étape 4 :** Écriture et analyse de requêtes d'extraction et d'agrégation SQL.

---

## 📑 Étape 1 : Découverte des données & Dictionnaire de données

L'analyse porte sur deux tables issues de fichiers CSV :
* `Contrat` : contient les informations relatives aux contrats d'assurance (30 335 lignes).
* `Region` : contient les données géographiques et administratives (38 916 lignes).

### Dictionnaire de Données

#### Table `Contrat`
| Nom de colonne | Type de données | Taille | Clé | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Contrat_ID` | `INT` | | Clé primaire | Id unique pour les contrats |
| `No_voie` | `INT` | | | Numéro dans la voie pour l'adresse du logement assuré |
| `B_T_Q` | `VARCHAR` | 1 | | Indicateur éventuel de répétition (Bis, Ter, Quater) |
| `Type_de_voie` | `VARCHAR` | 4 | | Type de voie (rue, av, rte, ...) |
| `Voie` | `VARCHAR` | 50 | | Libellé de la voie |
| `Code_dep_code_commune` | `VARCHAR` | 6 | Clé étrangère | Concaténation code département + code commune |
| `Code_postal` | `VARCHAR` | 5 | | Code postal du logement assuré |
| `Surface` | `INT` | | | Surface du bien assuré |
| `Type_local` | `VARCHAR` | 15 | | Type de bien (appartement, maison...) |
| `Occupation` | `VARCHAR` | 15 | | Statut de la personne ayant le contrat |
| `Type_contrat` | `VARCHAR` | 25 | | Nature de l'usage du logement |
| `Formule` | `VARCHAR` | 15 | | Formule du contrat d'assurance |
| `Valeur_declaree_biens` | `VARCHAR` | 15 | | Valeur des biens au domicile assuré |
| `Prix_cotisation_mensuel`| `VARCHAR` / `INT` | 15 | | Cotisation mensuelle du contrat |

#### Table `Region`
| Nom de colonne | Type de données | Taille | Clé | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Code_dep_code_commune` | `VARCHAR` | 6 | Clé primaire | Concaténation du code département et code commune |
| `reg_code` | `INT` | | | Code de la région |
| `reg_nom` | `VARCHAR` | 40 | | Nom de la région |
| `aca_nom` | `VARCHAR` | 40 | | Nom de l'académie |
| `dep_nom` | `VARCHAR` | 50 | | Nom du département |
| `com_nom_maj_court` | `VARCHAR` | 50 | | Nom de la commune (en majuscules) |
| `dep_code` | `VARCHAR` | | | Code département (ex: 2A, 2B, 92) |
| `dep_nom_num` | `VARCHAR` | 50 | | Nom du département + numéro |

---

## 📐 Étape 2 : Conception du schéma relationnel (MCD/MLD)

Grâce à **SQL Power Architect**, le schéma relationnel a été modélisé en définissant les contraintes d'intégrité référentielle :
* **Clé Primaire (`Region`)** : `Code_dep_code_commune`
* **Clé Primaire (`Contrat`)** : `Contrat_ID`
* **Clé Étrangère (`Contrat`)** : `Code_dep_code_commune` référençant `Region(Code_dep_code_commune)`

```sql
-- Script DDL de création de la table Region
CREATE TABLE Region (
    Code_dep_code_commune VARCHAR(6) NOT NULL,
    reg_code INT NOT NULL,
    reg_nom VARCHAR(40) NOT NULL,
    aca_nom VARCHAR(40) NOT NULL,
    dep_nom VARCHAR(50) NOT NULL,
    com_nom_maj_court VARCHAR(50) NOT NULL,
    dep_code VARCHAR NOT NULL,
    dep_nom_num VARCHAR(50) NOT NULL,
    PRIMARY KEY (Code_dep_code_commune)
);

-- Script DDL de création de la table Contrat
CREATE TABLE Contrat (
    Contrat_ID INT NOT NULL,
    No_voie INT,
    B_T_Q VARCHAR(1),
    Type_de_voie VARCHAR(4),
    Voie VARCHAR(50),
    Code_dep_code_commune VARCHAR(6) NOT NULL,
    Code_postal VARCHAR(5) NOT NULL,
    Surface INT NOT NULL,
    Type_local VARCHAR(15) NOT NULL,
    Valeur_declaree_biens VARCHAR(15) NOT NULL,
    Prix_cotisation_mensuel VARCHAR NOT NULL,
    Occupation VARCHAR(15) NOT NULL,
    Type_contrat VARCHAR(25) NOT NULL,
    Formule VARCHAR(15) NOT NULL,
    CONSTRAINT CONTRAT_PK PRIMARY KEY (Contrat_ID),
    CONSTRAINT Contrat_Region_FK FOREIGN KEY (Code_dep_code_commune) 
        REFERENCES Region(Code_dep_code_commune)
);
```

---

## 🗄 Étape 3 : Création et Chargement de la Base de Données

> ⚠️ **Note Importante sur l'Ordre de Création :**  
> La table `Region` (qui contient la clé primaire parent) **doit obligatoirement être créée avant** la table `Contrat`. Si l'on tente de créer `Contrat` en premier, SQLite renverra une erreur d'intégrité due à la clé étrangère référençant une table inexistante.

Les scripts ont été exécutés et les données importées à l'aide de l'IDE **DBeaver** :
* **Table `Contrat` :** 30 335 lignes importées.
* **Table `Region` :** 38 916 lignes importées.

---

## 🔍 Étape 4 : Rédaction et Exécution de Requêtes SQL

Voici quelques exemples de requêtes rédigées et exécutées sur la base :

### Requête 1 : Lister les contrats et leur surface pour le code postal 92100
```sql
SELECT Contrat_ID, Surface
FROM Contrat
WHERE Code_postal = '92100';
```

### Requête 2 : Lister le nom des différentes régions de France
```sql
SELECT reg_nom
FROM Region
GROUP BY reg_nom;
```

### Requête 3 : Communes ayant plus de 150 contrats souscrits
```sql
SELECT COUNT(*) AS Nombre_de_contrat, Region.com_nom_maj_court
FROM Contrat
JOIN Region ON (Contrat.Code_dep_code_commune = Region.Code_dep_code_commune)
GROUP BY Region.com_nom_maj_court
HAVING Nombre_de_contrat > 150
ORDER BY Nombre_de_contrat DESC;
```

### Requête 4 : Répartition du nombre de contrats par région
```sql
SELECT COUNT(*) AS Nombre_contrats, Region.reg_nom AS Region
FROM Contrat
JOIN Region ON (Contrat.Code_dep_code_commune = Region.Code_dep_code_commune)
GROUP BY Region.reg_nom;
```

---

## 🧰 Outils Utilisés

* **Excel / CSV** : Analyse et structuration initiale des données.
* **SQL Power Architect** : Conception du schéma relationnel et génération automatique du DDL SQLite.
* **DBeaver** : SGBD / Client SQL pour la création des tables, l'import des données CSV et l'exécution des requêtes.
* **SQLite** : Moteur de base de données relationnelle.
