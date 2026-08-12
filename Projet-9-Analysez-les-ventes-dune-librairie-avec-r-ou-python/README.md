# 📖 Bilan des Ventes & Analyse Comportementale — Librairie Lapage

## Présentation du Projet
Ce projet consiste en une analyse exploratoire et statistique des performances de vente en ligne de la **Librairie Lapage** depuis son ouverture. L'objectif principal est d'analyser l'activité globale, d'évaluer la performance des produits vendus et de mieux comprendre les habitudes d'achat des clients selon leurs caractéristiques démographiques (âge, genre).



## Enjeux et Objectifs
* **Évaluation de la performance globale :** Suivre l'évolution du chiffre d'affaires, du volume de transactions et du nombre de clients uniques au fil du temps.
* **Analyse du catalogue produit :** Identifier les références clés (Top/Flop des ventes en chiffre d'affaires et en volume) ainsi que la répartition des ventes par catégorie.
* **Segmentation et comportement client :** Comprendre l'impact du genre et de l'âge sur le panier moyen, la fréquence d'achat et la typologie de livres achetés.
* **Prise de décision stratégique :** Proposer des préconisations concrètes pour optimiser la fidélisation, cibler la communication et redresser les tendances de vente.



## Jeux de Données Utilisés
L'analyse s'appuie sur une extraction des données du site web de la librairie couvrant la période de **mars 2021 à février 2023**. 

Les données se divident en trois tables principales :

* **`customers`** (8 621 observations) : Informations sur les clients.
  * `client_id` : Identifiant unique du client.
  * `sex` : Sexe du client.
  * `birth` : Année de naissance.
* **`products`** (3 286 observations) : Catalogue des livres.
  * `id_prod` : Identifiant unique du produit.
  * `price` : Prix du livre.
  * `categ` : Catégorie du produit (0, 1 ou 2).
* **`transactions`** (1 048 575 observations brutes / 361 041 valeurs manquantes traitées) : Historique des achats.
  * `id_prod` : Identifiant du produit acheté.
  * `date` : Date et heure de la transaction.
  * `session_id` : Identifiant de la session d'achat.
  * `client_id` : Identifiant de l'acheteur.

> **Remarque sur la préparation des données :** Après nettoyage, gestion des valeurs manquantes et jointure des trois tables, le jeu de données final comprend **687 534 lignes**. Lors du nettoyage, 21 clients et 21 produits non associés à des transactions ont été identifiés. De plus, 4 clients B2B aux volumes atypiques ont été exclus des analyses statistiques pour ne pas biaiser les résultats.


