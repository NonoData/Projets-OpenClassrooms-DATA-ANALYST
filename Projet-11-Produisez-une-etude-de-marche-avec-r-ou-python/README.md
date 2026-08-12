# 🐣 Étude de Marché Internationale – La Poule qui Chante

## Présentation du Projet
**"La poule qui chante"** est une entreprise agroalimentaire française spécialisée dans l'élevage et la commercialisation de poulets de haute qualité, certifiés **"Poulet Agriculture Biologique"**. 

Actuellement implantée uniquement sur le marché français, l'entreprise souhaite impulser une nouvelle dynamique de croissance en se développant **à l'international**.

Ce projet s'inscrit dans le cadre d'une étude de marché globale visant à analyser le potentiel d'exportation vers divers pays du monde et à identifier les marchés cibles prioritaires pour la marque.



## Enjeux et Objectifs Stratégiques

L'internationalisation d'une entreprise agroalimentaire spécialisée dans le bio comporte plusieurs défis majeurs :
1. **Identifier les marchés solvables** : Trouver des pays disposant d'un pouvoir d'achat suffisant pour absorber une offre *Premium* (bio).
2. **Cibler les zones dépendantes des importations** : Repérer les pays ayant un besoin structurel d'importation de volaille (faible production locale relative ou forte demande).
3. **Minimiser les risques géopolitiques et opérationnels** : Sélectionner des destinations stables sur le plan politique et économique.
4. **Segmenter le monde de manière scientifique** : Éviter les choix intuitifs en s'appuyant sur des méthodes d'analyse de données avancées (Analyse en Composantes Principales - ACP, et Clustering K-Means / CAH).



## Données Utilisées

Les données proviennent de sources officielles internationales d'une grande fiabilité :
* **FAO (Organisation des Nations unies pour l'alimentation et l'agriculture)**
* **Banque Mondiale**

### Périmètre de l'étude
* **Année de référence** : 2017
* **Couverture** : 134 pays retenus (soit 87 % de la population mondiale)



## 📂 Structure du Répertoire
```text
├── README.md                           <- Présentation générale du projet (ce fichier)
├── data/
│   ├── raw/                            <- Données brutes de la FAO et Banque Mondiale (2017)
│   └── processed/                      <- Données nettoyées et préparées pour l'ACP
├── notebooks/
│   ├── 01_data_cleaning.ipynb          <- Nettoyage et fusion des jeux de données
│   ├── 02_eda_and_pca.ipynb            <- Analyse exploratoire et ACP (Axes F1 à F4)
│   └── 03_clustering_classification.ipynb <- Classification CAH et K-Means (5 clusters)
└── reports/
    └── presentation_marche_volaille.pdf <- Support de présentation de l'étude
```
