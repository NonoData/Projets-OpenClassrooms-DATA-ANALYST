# Étude de Marché Internationale – La Poule qui Chante

## 📌 Présentation du Projet
**"La poule qui chante"** est une entreprise agroalimentaire française spécialisée dans l'élevage et la commercialisation de poulets de haute qualité, certifiés **"Poulet Agriculture Biologique"**. 

Actuellement implantée uniquement sur le marché français, l'entreprise souhaite impulser une nouvelle dynamique de croissance en se développant **à l'international**.

Ce projet s'inscrit dans le cadre d'une étude de marché globale visant à analyser le potentiel d'exportation vers divers pays du monde et à identifier les marchés cibles prioritaires pour la marque.

---

## 🎯 Enjeux et Objectifs Stratégiques

L'internationalisation d'une entreprise agroalimentaire spécialisée dans le bio comporte plusieurs défis majeurs :
1. **Identifier les marchés solvables** : Trouver des pays disposant d'un pouvoir d'achat suffisant pour absorber une offre *Premium* (bio).
2. **Cibler les zones dépendantes des importations** : Repérer les pays ayant un besoin structurel d'importation de volaille (faible production locale relative ou forte demande).
3. **Minimiser les risques géopolitiques et opérationnels** : Sélectionner des destinations stables sur le plan politique et économique.
4. **Segmenter le monde de manière scientifique** : Éviter les choix intuitifs en s'appuyant sur des méthodes d'analyse de données avancées (Analyse en Composantes Principales - ACP, et Clustering K-Means / CAH).

---

## 📊 Données Utilisées

Les données proviennent de sources officielles internationales d'une grande fiabilité :
* **FAO (Organisation des Nations unies pour l'alimentation et l'agriculture)**
* **Banque Mondiale**

### Périmètre de l'étude
* **Année de référence** : 2017
* **Couverture** : 134 pays retenus (soit 87 % de la population mondiale)

### Variables retenues (13 indicateurs clés)
Les variables sont structurées en 4 catégories stratégiques :

| Catégorie | Variable | Unité / Description | Rôle stratégique |
| :--- | :--- | :--- | :--- |
| **Économique** | **PIB** | Millions USD | Taille totale du marché |
| **Économique** | **PIB par habitant** | USD | Pouvoir d'achat individuel |
| **Social** | **Population** | Habitants | Volume de consommateurs potentiels |
| **Social** | **Accès à une alimentation saine (%)** | % population | Indicateur du marché adressable *Premium* |
| **Social** | **Précarité alimentaire (%)** | % population | Population n'ayant pas les moyens d'une alimentation saine |
| **Social** | **Disponibilité alimentaire** | kg/pers/an | Niveau de consommation locale de volaille |
| **Social** | **Disponibilité intérieure** | Milliers de tonnes | Volume global de volailles disponible |
| **Technique** | **Production** | Milliers de tonnes | Mesure de la concurrence intérieure |
| **Technique** | **Production par habitant** | kg/habitant | Productivité locale relative |
| **Économique** | **Importations** | Milliers de tonnes | Ouverture actuelle du marché |
| **Économique** | **Exportations** | Milliers de tonnes | Identification des pays concurrents / pivots |
| **Économique** | **Taux de dépendance** | % | Dépendance structurelle à l'importation |
| **Légal/Politique**| **Stability Score** | Indice | Évaluation des risques géopolitiques |

---

## 🛠️ Méthodologie & Traitement des Données

1. **Nettoyage et Préparation** :
   * Filtrage des données spécifiques à la filière volaille.
   * Pivotement des tables pour obtenir un profil unique par pays.
   * Traitement des valeurs manquantes (imputation / nettoyage).
   * Appariement par codes ISO3 (retrait de la France, marché d'origine).

2. **Analyse en Composantes Principales (ACP)** :
   * Réduction des 13 variables en **4 axes synthétiques (F1 à F4)** expliquant plus de 80 % de la variance totale :
     * **F1 – Puissance Économique** : Taille du marché, PIB total et volume de production.
     * **F2 – Développement humain et social** : Niveau de vie, pouvoir d'achat (PIB/hab) vs. précarité.
     * **F3 – Mode d'approvisionnement** : Autonomie locale vs. dépendance aux importations.
     * **F4 – Contraste démographique et vulnérabilités** : Pression démographique et marché intérieur.

3. **Segmentation (Clustering)** :
   * Combinaison de la **Classification Ascendante Hiérarchique (CAH)** et de l'algorithme des **K-Means**.
   * Découpage optimal en **5 clusters de pays**.

---

## 💡 Résultats et Typologie des Marchés (5 Clusters)

* **Cluster 0 – Les Émergents** (*ex. Russie, Afrique du Sud, Turquie, Colombie*) : Marchés en croissance avec une assiette économique solide et un niveau de vie intermédiaire.
* **Cluster 1 – Les Économies vulnérables / en développement** (*ex. Nigéria, Pakistan, Bangladesh, Éthiopie*) : Forte pression démographique et précarité élevée.
* **Cluster 2 – Les Géants démographiques d'Asie** (*Inde, Chine*) : Très forts volumes mais spécificités locales et marchés intérieurs massifs.
* **Cluster 3 – Les Mastodontes exportateurs autonomes** (*États-Unis, Brésil*) : Principaux concurrents mondiaux et grands producteurs.
* **Cluster 4 – Les Pays développés à haute stabilité** (*ex. Allemagne, Irlande, Japon*) : Fort pouvoir d'achat, excellente stabilité et dépendance aux importations.

---

## 🎯 Recommandations Stratégiques

1. **Cible Principale ("Premium Bio") 👉 Cluster 4** (*Allemagne, Irlande, Japon...*)
   * **Pourquoi ?** Pouvoir d'achat le plus élevé, stabilité maximale et forte dépendance aux importations (score F3 très élevé).
   * **Stratégie** : Positionnement haut de gamme axé sur la qualité, la certification bio française et la traçabilité.

2. **Cible Secondaire ("Marché de Masse") 👉 Cluster 0** (*Russie, Turquie, Afrique du Sud...*)
   * **Pourquoi ?** Assise macroéconomique en croissance et classe moyenne émergente.
   * **Stratégie** : Déploiement progressif avec des gammes ajustées.

---

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
