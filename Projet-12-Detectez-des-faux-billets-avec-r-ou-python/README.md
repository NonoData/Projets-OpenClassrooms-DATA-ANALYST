# Détection de Faux Billets – Algorithme de Classification Binaire

## 📌 Présentation du Projet

Ce projet est réalisé dans le cadre des missions de l'**Organisation Nationale de Lutte Contre le Faux-Monnayage (ONCFM)**, une organisation publique chargée d'identifier les contrefaçons de billets de banque [cite: 3].

L'objectif principal est de concevoir un **algorithme d'apprentissage automatique (Machine Learning)** capable de différencier automatiquement un **vrai billet** d'un **faux billet** [cite: 3], à partir uniquement de ses **caractéristiques géométriques et dimensions physiques** (mesurées en millimètres) [cite: 3].

---

## 🎯 Enjeux Métier et Stratégiques

Dans le domaine de la lutte contre le faux-monnayage, toutes les erreurs de classification n'ont pas la même gravité [cite: 3] :
* **Détecter un faux billet est la priorité absolue** : Un faux billet classé comme vrai (faux négatif) s'infiltre dans le système financier et cause un préjudice économique direct [cite: 3].
* **L'enjeu clé** est donc de maximiser le **Rappel (Recall) sur la classe « Faux »** [cite: 3]. On cherche à atteindre un score de recall proche de **1,00 (100 % de faux billets interceptés)**, quitte à rejeter temporairement quelques vrais billets à des fins de vérification manuelle [cite: 3].

---

## 📊 Données Utilisées

Le jeu de données étudié comporte **1 500 billets de banque** [cite: 3] :
* **1 000 vrais billets** (`is_genuine = True`, soit 66,7 %) [cite: 3]
* **500 faux billets** (`is_genuine = False`, soit 33,3 %) [cite: 3]

### Variables Géométriques (en mm)
Pour chaque billet, 6 dimensions géométriques sont mesurées [cite: 3] :

| Variable | Description |
| :--- | :--- |
| `length` | Longueur du billet (mm) [cite: 3] |
| `height_left` | Hauteur mesurée sur le côté gauche du billet (mm) [cite: 3] |
| `height_right` | Hauteur mesurée sur le côté droit du billet (mm) [cite: 3] |
| `margin_up` | Marge entre le bord supérieur et l'image centrale (mm) [cite: 3] |
| `margin_low` | Marge entre le bord inférieur et l'image centrale (mm) [cite: 3] |
| `diagonal` | Longueur de la diagonale du billet (mm) [cite: 3] |

### Insights Exploratoires Clés
* **`length` (Longueur)** est l'indicateur le plus fort : les faux billets sont en moyenne plus courts (111,63 mm) que les vrais (113,20 mm) [cite: 3].
* **`margin_low` et `margin_up` (Marges)** : Les faux billets présentent des marges plus larges, notamment la marge inférieure (5,22 mm vs 4,12 mm pour les vrais) [cite: 3].
* **`diagonal`** présente très peu de correlation linéaire avec la véracité du billet et apporte très peu de pouvoir préditctif [cite: 3].

---

## 🛠️ Préparation des Données & Méthodologie

1. **Traitement des Valeurs Manquantes** : Imputation par la médiane sur la variable `margin_low` (37 valeurs manquantes) [cite: 3], calculée strictement sur le jeu d'entraînement pour éviter toute fuite de données (*data leakage*) [cite: 3].
2. **Séparation Train / Test** : Découpage stratifié 80 / 20 (1 200 billets pour l'entraînement, 300 billets pour le test) préservant la proportion 66,7% / 33,3% [cite: 3].
3. **Standardisation** : Mise à l'échelle (moyenne 0, écart-type 1) pour les algorithmes sensibles aux distances (Régression Logistique, KNN, K-means) [cite: 3].
4. **Modèles Évalués** :
   * **Régression Logistique** (supervisé) [cite: 3]
   * **KNN - K-Nearest Neighbors** (supervisé) [cite: 3]
   * **Random Forest / Forêt Aléatoire** (supervisé) [cite: 3]
   * **K-means** (non-supervisé pour analyse de clusters) [cite: 3]

---

## 🏆 Modèle Final et Performances

### Comparaison des Modèles (Sur Jeu de Test - 300 billets)

| Modèle | Accuracy | Précision (Faux) | Recall (Faux) | F1-Score (Faux) | Statut |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Random Forest** | **0,9900** | **0,9899** | **0,9800** | **0,9849** | **Retenu** [cite: 3] |
| **Régression Logistique** | 0,9900 | 0,9899 | 0,9800 | 0,9849 | Égalité [cite: 3] |
| **K-means** (non supervisé) | 0,9867 | 0,9800 | 0,9800 | 0,9800 | Évalué [cite: 3] |
| **KNN** | 0,9833 | 0,9798 | 0,9700 | 0,9749 | En retrait [cite: 3] |

> **Pourquoi le Random Forest a-t-il été retenu ?**
> Le Random Forest et la Régression Logistique obtiennent des résultats identiques [cite: 3]. Le **Random Forest** a été sélectionné car il ne nécessite pas de standardisation préalable des données [cite: 3], s'avère très robuste face à d'éventuelles dérives futures des données [cite: 3], et fournit une interprétabilité directe via l'importance des variables [cite: 3] (`length` compte pour ~50 % et `margin_low` pour ~31 % de la décision [cite: 3]).

### Optimisation Métier du Seuil de Décision
Afin d'atteindre l'objectif zéro faux billet manqué [cite: 3], le seuil de probabilité de classification a été optimisé [cite: 3] :
* **Seuil standard (0,50)** : Recall Faux = 0,970 [cite: 3]
* **Seuil optimisé (0,80)** : **Recall Faux = 1,000** | **Précision Faux = 0,952** [cite: 3]

👉 **Résultat** : Un billet n'est classé comme « Vrai » que si le modèle en est certain à **80 % au moins** [cite: 3]. **100 % des faux billets sont interceptés** sur le jeu de test [cite: 3].

---

## 🚀 Applications & Déploiement

Le projet comporte deux interfaces utilisateur pour exécuter les prédictions en production :

1. **Script en Ligne de Commande (CLI)** :
   * Permet d'analyser un fichier batch (`billets_production.csv`) ou un billet individuel [cite: 3].
   * Génère un compte-rendu console et enregistre les résultats détaillés dans `resultats.csv` [cite: 3].
   * Prérequis : `Python 3.8+`, `pandas`, `numpy`, `joblib` [cite: 3].

2. **Application Web Interactive (Streamlit)** :
   * Interface graphique intuitive permettant l'import de fichier CSV [cite: 3], le réglage des paramètres et la visualisation dynamique des prédictions [cite: 3].
   * Prérequis : `Python 3.10+`, `pandas`, `numpy`, `joblib`, `scikit-learn`, `streamlit` [cite: 3].

---

## 📂 Structure du Répertoire

```text
.
├── README.md                           <- Présentation générale du projet (ce fichier)
├── README_app.md                       <- Guide d'utilisation du script en ligne de commande (CLI)
├── README_app_streamlit.md             <- Guide d'utilisation de l'application Web Streamlit
├── billets_production.csv              <- Jeu de données de production pour test des scripts
├── models/
│   └── random_forest_model.joblib      <- Modèle Random Forest entraîné et optimisé
├── scripts/
│   ├── detecteur_cli.py                <- Script d'exécution en ligne de commande
│   └── app_streamlit.py                <- Application web interactive Streamlit
└── reports/
    └── support_de_presentation.pdf     <- Support de présentation synthétique du projet
```
