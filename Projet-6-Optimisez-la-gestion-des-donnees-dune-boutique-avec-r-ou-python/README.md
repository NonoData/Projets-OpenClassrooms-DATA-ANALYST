# 🍷 Bottleneck - Analyse des Ventes et Gestion des Stocks

## Contexte & Vue d'ensemble
**Bottleneck** est un marchand prestigieux spécialisé dans les vins fins et les spiritueux. Face au développement des activités en ligne et en magasin, l'unification des données de ventes et de stocks est devenue essentielle pour la prise de décision opérationnelle et la planification stratégique.

Ce projet propose une analyse exploratoire approfondie des données (EDA), un nettoyage des données, un rapprochement de modèles ainsi qu'une consolidation des ventes et des stocks basée sur les données extraites au **31 octobre 2024**.



## Objectifs Stratégiques & Défis Majeurs
L'objectif principal est de fournir un reporting d'activité fiable et exploitable à la direction générale. Les principaux défis comprennent :

1. **Unification & Rapprochement des Données** : Associer les systèmes de gestion hors ligne (ERP) aux données e-commerce (CMS Web) via une table de liaison intermédiaire.
2. **Gouvernance des Données & Audit Qualité** : Identifier et corriger les anomalies de saisie (stocks/prix négatifs, SKU non liés, ratios de prix incorrects).
3. **Analyse du Chiffre d'Affaires & du Portefeuille Produits** : Évaluer la performance des ventes, comprendre la répartition de l'offre (gamme principale vs produits prestige/outliers) et mesurer les marges par catégorie.
4. **Optimisation des Stocks & de l'Inventaire** : Détecter les situations de surstock, évaluer la couverture des stocks (mois de stock) et prendre en compte les variations saisonnières (ex. pics de ventes de fin d'année).



## Jeux de Données

L'analyse repose sur trois sources de données principales :

**ERP** : Données du système de gestion d'entreprise interne.
**WEB** : Extraction de la boutique en ligne e-commerce.
**Liaison** :Table de correspondance manuelle liant produits physiques et en ligne.
