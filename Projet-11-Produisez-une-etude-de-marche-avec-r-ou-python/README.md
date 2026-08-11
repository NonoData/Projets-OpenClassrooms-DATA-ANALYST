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
