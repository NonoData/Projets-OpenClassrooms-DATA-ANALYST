# Bilan des Ventes & Analyse Comportementale — Librairie Lapage

## Présentation du Projet
Ce projet consiste en une analyse exploratoire et statistique des performances de ventes en ligne de la **Librairie Lapage** depuis son ouverture[cite: 18]. L'objectif principal est d'analyser l'activité globale, d'évaluer la performance des produits vendus et de mieux comprendre les habitudes d'achat des clients selon leurs caractéristiques démographiques (âge, genre)[cite: 18].

---

## Enjeux et Objectifs
* **Évaluation de la performance globale :** Suivre l'évolution du chiffre d'affaires, du volume de transactions et du nombre de clients uniques au fil du temps[cite: 18].
* **Analyse du catalogue produit :** Identifier les références clés (Top/Flop des ventes en chiffre d'affaires et en volume) ainsi que la répartition des ventes par catégorie[cite: 18].
* **Segmentation et comportement client :** Comprendre l'impact du genre et de l'âge sur le panier moyen, la fréquence d'achat et la typologie de livres achetés[cite: 18].
* **Prise de décision stratégique :** Proposer des préconisations concrètes pour optimiser la fidélisation, cibler la communication et redresser les tendances de ventes[cite: 18].

---

## Jeux de Données Utilisés
L'analyse s'appuie sur une extraction des données du site web de la librairie couvrant la période de **mars 2021 à février 2023**[cite: 18]. 

Les données se divisent en trois tables principales[cite: 18] :

* **`customers`** (8 621 observations) : Informations sur les clients[cite: 18].
  * `client_id` : Identifiant unique du client[cite: 18].
  * `sex` : Sexe du client[cite: 18].
  * `birth` : Année de naissance[cite: 18].
* **`products`** (3 286 observations) : Catalogue des livres[cite: 18].
  * `id_prod` : Identifiant unique du produit[cite: 18].
  * `price` : Prix du livre[cite: 18].
  * `categ` : Catégorie du produit (0, 1 ou 2)[cite: 18].
* **`transactions`** (1 048 575 observations brutes / 361 041 valeurs manquantes traitées) : Historique des achats[cite: 18].
  * `id_prod` : Identifiant du produit acheté[cite: 18].
  * `date` : Date et heure de la transaction[cite: 18].
  * `session_id` : Identifiant de la session d'achat[cite: 18].
  * `client_id` : Identifiant de l'acheteur[cite: 18].

> **Remarque sur la préparation des données :** Après nettoyage, gestion des valeurs manquantes et jointure des trois tables, le jeu de données final comprend **687 534 lignes**[cite: 18]. Lors du nettoyage, 21 clients et 21 produits non associés à des transactions ont été identifiés[cite: 18]. De plus, 4 clients BtoB aux volumes atypiques ont été exclus des analyses statistiques pour ne pas biaiser les résultats[cite: 18].

---

## Principaux Constats

* **Évolution des Ventes :** Le chiffre d'affaires progresse de façon continue jusqu'au début de l'année 2022 avant de devenir plus instable, marqué par une chute nette en février 2023[cite: 18].
* **Répartition par Catégorie :** Les catégories 0 et 1 représentent près de **77 % du chiffre d'affaires total**[cite: 18].
* **Concentration du CA (Gini) :** L'indice de Gini s'élève à **0.398**, traduisant une concentration du chiffre d'affaires sur une partie des clients[cite: 18].
* **Impact de l'Âge :**
  * *Genre :* Peu de différences constatées dans la répartition des catégories achetées entre hommes et femmes[cite: 18].
  * *Catégories :* La catégorie 2 touche un public jeune (moyenne de 22,8 ans), la catégorie 0 concerne les adultes (moyenne de 42,7 ans), et la catégorie 1 attire un public plus âgé (moyenne de 49,8 ans)[cite: 18].
  * *Comportement :* Les moins de 30 ans présentent un panier moyen nettement plus élevé[cite: 18], tandis que la tranche 30–50 ans réalise des achats plus fréquents[cite: 18].

---

## Recommendations Strategiques
1. **Investigation requise :** Identifier rapidement la cause exacte de la baisse brutale de clients, de transactions et de chiffre d'affaires observée en février 2023[cite: 18].
2. **Fidélisation des < 30 ans :** Mettre en place un programme ciblé pour encourager cette tranche d'âge, qui a un panier moyen élevé, à acheter plus fréquemment[cite: 18].
3. **Optimisation pour les 30–50 ans :** Développer des mécanismes de recommandation ou d'offres combinées pour inciter ce segment très actif à augmenter son panier moyen[cite: 18].
