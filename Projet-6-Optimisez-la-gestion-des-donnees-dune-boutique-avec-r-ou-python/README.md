# 🍷 Bottleneck - Analyse des Ventes et Gestion des Stocks

## 📌 Contexte & Vue d'ensemble
**Bottleneck** est un marchand prestigieux spécialisé dans les vins fins et les spiritueux. Face au développement des activités en ligne et en magasin, l'unification des données de ventes et de stocks est devenue essentielle pour la prise de décision opérationnelle et la planification stratégique.

Ce projet propose une analyse exploratoire approfondie des données (EDA), un nettoyage des données, un rapprochement de modèles ainsi qu'une consolidation des ventes et des stocks basée sur les données extraites au **31 octobre 2024**.

---

## 🎯 Objectifs Stratégiques & Défis Majeurs
L'objectif principal est de fournir un reporting d'activité fiable et exploitable à la direction générale. Les principaux défis comprennent :

1. **Unification & Rapprochement des Données** : Associer les systèmes de gestion hors ligne (ERP) aux données e-commerce (CMS Web) via une table de liaison intermédiaire.
2. **Gouvernance des Données & Audit Qualité** : Identifier et corriger les anomalies de saisie (stocks/prix négatifs, SKU non liés, ratios de prix incorrects).
3. **Analyse du Chiffre d'Affaires & du Portefeuille Produits** : Évaluer la performance des ventes, comprendre la répartition de l'offre (gamme principale vs produits prestige/outliers) et mesurer les marges par catégorie.
4. **Optimisation des Stocks & de l'Inventaire** : Détecter les situations de surstock, évaluer la couverture des stocks (mois de stock) et prendre en compte les variations saisonnières (ex. pics de ventes de fin d'année).

---

## 📊 Jeux de Données & Architecture

L'analyse repose sur trois sources de données principales :

| Jeu de données | Observations | Variables | Description | Champs clés |
| :--- | :--- | :--- | :--- | :--- |
| **ERP** | 825 | 6 | Données du système de gestion d'entreprise interne | `product_id`, `price`, `purchase_price`, `stock_quantity`, `stock_status`, `onsale_web` |
| **WEB** | 1 513 | 29 | Extraction de la boutique en ligne e-commerce | `sku`, `total_sales`, `post_date`, `product_type`, `post_title` |
| **Liaison** | 825 | 2 | Table de correspondance manuelle liant produits physiques et en ligne | `product_id`, `id_web` |

### Pipeline d'Intégration des Données
```
+------------------+         +--------------------+         +------------------+
|   Dataset ERP    | ------> |  Table de Liaison  | <------ |   Dataset WEB    |
| (product_id [PK])|         |(product_id, id_web)|         |    (sku [PK])    |
+------------------+         +--------------------+         +------------------+
```
* **ERP ↔ Liaison** : 100 % de conservation des données (825 articles).
* **Intégration Web Consolidation (Inner Join)** : Filtré à 714 références en ligne actives pour analyser les performances e-commerce en direct.

---

## 🧹 Qualité des Données & Inscription de Variables (Feature Engineering)

### Points Forts du Nettoyage & de l'Audit
* **Correction des Valeurs Négatives** : Neutralisation des prix et quantités de stock négatifs.
* **Contrôles d'Intégrité** : Réalignement du `stock_status` avec le comptage réel des stocks.
* **Déduplication Web** : Suppression des doublons web, des colonnes de métadonnées vides, des doublons de fuseaux horaires (GMT) et des SKU non liés.
* **Anomalie de Prix Critique Détectée** : 
  * *ID Produit 4355* : Prix d'achat = **77,48 € HT** vs Prix de vente = **10,54 € HT** (Correction urgente requise).
* **Articles du Catalogue Non Liés** : Identification de 111 produits présents dans l'ERP/Liaison mais non publiés sur le site web, nécessitant un arbitrage commercial (mise en ligne vs déstockage).

### Variables Créées (Feature Engineering)
* **Chiffre d'Affaires (CA)** : `total_sales * price` (143 680 € enregistrés au total).
* **Valeur de l'Inventaire** : Valorisation totale du stock physique (277 328,07 € répartis sur 16 740 articles).
* **Taux de Marge** : Évaluation du taux de marge brute par catégorie de produits.
* **Détection d'Outliers par Z-Score** : Détection statistique des points de prix atypiques.

---

## 📈 Enseignements Clés & Constats Commerciaux

### 1. Structure des Prix & Segment "Prestige"
* **Gamme Principale** : Le prix médian d'une bouteille est de **24,00 €**, avec 50 % du catalogue dont le prix est compris entre **14,00 € et 42,00 €**.
* **Valeurs Atypiques (Prestige)** : Les outliers statistiques (via IQR et Z-Score) ont été validés par les experts métier comme étant des Grands Crus haut de gamme, des Champagnes millésimés et des spiritueux rares (ex. *Egly-Ouriet Grand Cru Millésime 2008* à **225,00 €**, *Frapin VIP XO Cognac* à **176,00 €**).

### 2. Concentration du CA & des Ventes (Analyse de Pareto)
* **Chiffre d'Affaires** : 80 % du chiffre d'affaires total est généré par **60 % des références (433 articles)**.
* **Volume** : 80 % du volume des ventes est porté par **61 % des références (432 articles)**.
* *Bilan* : Une répartition saine des ventes sans dépendance excessive à un seul best-seller.

### 3. Performance des Marges
* **Marges les plus Élevées** : Les spiritueux (Cognac, Whisky, Gin) affichent la meilleure rentabilité (>75-80 %).
* **Cœur de Métier** : Le vin conserve une marge solide de **61,5 %**.
* **Produits d'Appel / Entrée de Gamme** : Le Champagne et l'Huile d'Olive présentent des taux de marge plus faibles.

### 4. Analyse de Corrélation
* **Prix vs Ventes (-0,52)** : Forte corrélation négative — un prix plus élevé entraîne une baisse des ventes unitaires.
* **Stock vs Ventes (+0,44)** : Corrélation positive modérée — le niveau des stocks est bien aligné sur la demande.
* **Stock vs Prix (-0,11)** : Aucune relation significative — le prix unitaire ne dicte pas la stratégie de détention des stocks.

---

## 🚀 Recommandations Actionnables

1. **Gouvernance des Données & Contrôles Système** :
   * Mettre en place des contraintes de saisie dans l'ERP pour empêcher les prix ou quantités négatifs.
   * Automatiser les contrôles de marge pour signaler immédiatement les marges négatives lors de la création de SKU.
2. **Ajustements Commerciaux & Tarifaires** :
   * Corriger immédiatement l'erreur de prix sur l'ID Produit 4355.
   * Statuer sur les 111 articles hors ligne (publication sur la boutique en ligne ou liquidation des stocks).
3. **Gestion des Stocks** :
   * Rééquilibrer les niveaux de stock élevés sur les Champagnes millésimés à faible rotation, tout en anticipant la forte demande des fêtes de fin d'année (Q4).
   * Élargir le suivi au-delà d'un instantané mensuel unique pour prendre en compte la saisonnalité annuelle.
