# Détection de Faux Billets – Algorithme de Classification Binaire

## 📌 Présentation du Projet

Ce projet est réalisé dans le cadre des missions de l'**Organisation Nationale de Lutte Contre le Faux-Monnayage (ONCFM)**, une organisation publique chargée d'identifier les contrefaçons de billets de banque .

L'objectif principal est de concevoir un **algorithme d'apprentissage automatique (Machine Learning)** capable de différencier automatiquement un **vrai billet** d'un **faux billet** , à partir uniquement de ses **caractéristiques géométriques et dimensions physiques** (mesurées en millimètres) .

---

## 🎯 Enjeux Métier et Stratégiques

Dans le domaine de la lutte contre le faux-monnayage, toutes les erreurs de classification n'ont pas la même gravité  :
* **Détecter un faux billet est la priorité absolue** : Un faux billet classé comme vrai (faux négatif) s'infiltre dans le système financier et cause un préjudice économique direct .
* **L'enjeu clé** est donc de maximiser le **Rappel (Recall) sur la classe « Faux »** . On cherche à atteindre un score de recall proche de **1,00 (100 % de faux billets interceptés)**, quitte à rejeter temporairement quelques vrais billets à des fins de vérification manuelle .

---

## 📊 Données Utilisées

Le jeu de données étudié comporte **1 500 billets de banque**  :
* **1 000 vrais billets** (`is_genuine = True`, soit 66,7 %) 
* **500 faux billets** (`is_genuine = False`, soit 33,3 %) 

### Variables Géométriques (en mm)
Pour chaque billet, 6 dimensions géométriques sont mesurées  :

| Variable | Description |
| :--- | :--- |
| `length` | Longueur du billet (mm)  |
| `height_left` | Hauteur mesurée sur le côté gauche du billet (mm)  |
| `height_right` | Hauteur mesurée sur le côté droit du billet (mm)  |
| `margin_up` | Marge entre le bord supérieur et l'image centrale (mm)  |
| `margin_low` | Marge entre le bord inférieur et l'image centrale (mm)  |
| `diagonal` | Longueur de la diagonale du billet (mm)  |

### Insights Exploratoires Clés
* **`length` (Longueur)** est l'indicateur le plus fort : les faux billets sont en moyenne plus courts (111,63 mm) que les vrais (113,20 mm) .
* **`margin_low` et `margin_up` (Marges)** : Les faux billets présentent des marges plus larges, notamment la marge inférieure (5,22 mm vs 4,12 mm pour les vrais) .
* **`diagonal`** présente très peu de correlation linéaire avec la véracité du billet et apporte très peu de pouvoir préditctif .

---

## 🛠️ Préparation des Données & Méthodologie

1. **Traitement des Valeurs Manquantes** : Imputation par la médiane sur la variable `margin_low` (37 valeurs manquantes) , calculée strictement sur le jeu d'entraînement pour éviter toute fuite de données (*data leakage*) .
2. **Séparation Train / Test** : Découpage stratifié 80 / 20 (1 200 billets pour l'entraînement, 300 billets pour le test) préservant la proportion 66,7% / 33,3% .
3. **Standardisation** : Mise à l'échelle (moyenne 0, écart-type 1) pour les algorithmes sensibles aux distances (Régression Logistique, KNN, K-means) .
4. **Modèles Évalués** :
   * **Régression Logistique** (supervisé) 
   * **KNN - K-Nearest Neighbors** (supervisé) 
   * **Random Forest / Forêt Aléatoire** (supervisé) 
   * **K-means** (non-supervisé pour analyse de clusters) 

---

## 🏆 Modèle Final et Performances

### Comparaison des Modèles (Sur Jeu de Test - 300 billets)

| Modèle | Accuracy | Précision (Faux) | Recall (Faux) | F1-Score (Faux) | Statut |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Random Forest** | **0,9900** | **0,9899** | **0,9800** | **0,9849** | **Retenu**  |
| **Régression Logistique** | 0,9900 | 0,9899 | 0,9800 | 0,9849 | Égalité  |
| **K-means** (non supervisé) | 0,9867 | 0,9800 | 0,9800 | 0,9800 | Évalué  |
| **KNN** | 0,9833 | 0,9798 | 0,9700 | 0,9749 | En retrait  |

> **Pourquoi le Random Forest a-t-il été retenu ?**
> Le Random Forest et la Régression Logistique obtiennent des résultats identiques . Le **Random Forest** a été sélectionné car il ne nécessite pas de standardisation préalable des données , s'avère très robuste face à d'éventuelles dérives futures des données , et fournit une interprétabilité directe via l'importance des variables  (`length` compte pour ~50 % et `margin_low` pour ~31 % de la décision ).

### Optimisation Métier du Seuil de Décision
Afin d'atteindre l'objectif zéro faux billet manqué , le seuil de probabilité de classification a été optimisé  :
* **Seuil standard (0,50)** : Recall Faux = 0,970 
* **Seuil optimisé (0,80)** : **Recall Faux = 1,000** | **Précision Faux = 0,952** 

👉 **Résultat** : Un billet n'est classé comme « Vrai » que si le modèle en est certain à **80 % au moins** . **100 % des faux billets sont interceptés** sur le jeu de test .

---

## 🚀 Applications & Déploiement

Le projet comporte deux interfaces utilisateur pour exécuter les prédictions en production :

1. **Script en Ligne de Commande (CLI)** :
   * Permet d'analyser un fichier batch (`billets_production.csv`) ou un billet individuel .
   * Génère un compte-rendu console et enregistre les résultats détaillés dans `resultats.csv` .
   * Prérequis : `Python 3.8+`, `pandas`, `numpy`, `joblib` .

2. **Application Web Interactive (Streamlit)** :
   * Interface graphique intuitive permettant l'import de fichier CSV , le réglage des paramètres et la visualisation dynamique des prédictions .
   * Prérequis : `Python 3.10+`, `pandas`, `numpy`, `joblib`, `scikit-learn`, `streamlit` .

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
