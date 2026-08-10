# Détection automatique de faux billets — ONCFM (Application web avec Streamlit)

Application web interactive permettant d'analyser un lot de billets à partir d'un fichier CSV, et de détecter automatiquement les faux billets à partir de leurs caractéristiques géométriques grâce à un modèle **Random Forest** optimisé.

Tout comme la version en ligne de commande, le modèle a été entraîné et optimisé dans le notebook `Meloen_Arnaud_1_Notebook_analyse_072026.ipynb`. Cette application charge les artefacts exportés (modèle, imputer, configuration) et les applique à un billet unique ou à un lot de billets fourni sous forme de fichier CSV.

Contrairement à la version en ligne de commande (`Meloen_Arnaud_2_scrypt_app_072026.py`), cette application propose une interface graphique dans le navigateur : import du fichier par glisser-déposer (ou saisie manuelle), aperçu des données, lancement de l'analyse en un clic, affichage des résultats et export des résultats en CSV.

Deux modes d'analyse sont proposés :
- **📄 Fichier CSV** : import d'un lot de billets à analyser en une seule fois.
- **✍️ Saisie manuelle** : vérification d'un billet unique en renseignant ses mesures directement dans l'interface.

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Fichiers nécessaires](#fichiers-nécessaires)
- [Lancement de l'application](#lancement-de-lapplication)
- [Utilisation](#utilisation)
  - [Import CSV](#import-csv)
  - [Saisie manuelle](#saisie-manuelle)
- [Format du CSV attendu](#format-du-csv-attendu)
- [Structure du projet](#structure-du-projet)
- [Alternative en ligne de commande](#alternative-en-ligne-de-commande)

## Fonctionnalités

- Chargement du modèle, de l'imputer et de la configuration (mis en cache pour de meilleures performances).
- Détection automatique du séparateur CSV (`,` ou `;`).
- Vérification des colonnes requises avec message d'erreur explicite si des colonnes manquent.
- Imputation des valeurs manquantes avant prédiction.
- Calcul de la probabilité d'authenticité et classification (`Vrai` / `Faux`) selon un seuil de décision configurable.
- Export des résultats au format CSV.
- Saisie manuelle d'un billet avec formulaire dynamique généré à partir des variables du modèle.

## Prérequis

- Python 3.10 ou supérieur (pour être supporté par Streamlit)

Les librairie suivantes :
- `streamlit`
- `pandas`
- `joblib`
- `scikit-learn`

## Installation

Installez les dépendances nécessaires :

```bash
pip install streamlit pandas joblib scikit-learn
```

## Fichiers nécessaires

L'application a besoin des artefacts suivants, placés **dans le même dossier** que `Meloen_Arnaud_2_scrypt_app_streamlit_072026.py` :

| Fichier | Description |
|---|---|
| `random_forest_model.joblib` | Modèle Random Forest optimisé (entraîné via GridSearchCV) |
| `imputer.joblib` | `SimpleImputer` entraîné sur les données d'entraînement |
| `model_config.json` | Configuration du modèle : `{"threshold": 0.8, "features": [...]}` |

Ces fichiers sont générés une seule fois depuis le notebook d'entraînement (voir le bloc d'export en fin de notebook). Si l'un d'eux est absent, l'application affiche un message d'erreur s'affiche dans l'application et l'exécution s'arrête proprement.

## Lancement de l'application

Depuis le dossier contenant `Meloen_Arnaud_2_scrypt_app_streamlit_072026.py` :

```bash
streamlit run Meloen_Arnaud_2_scrypt_app_streamlit_072026.py
```

Streamlit ouvre automatiquement l'application dans le navigateur.

## Utilisation

### Import CSV

1. **Importer le fichier CSV** contenant les billets à analyser (le format du CSV sera donné plus bas)
2. **Vérifier l'aperçu** des données importées, affiché automatiquement sous forme de tableau.
3. **Cliquer sur "Lancer l'analyse des billets"** pour exécuter le modèle sur l'ensemble du fichier.
4. **Consulter les résultats** :
   - deux indicateurs synthétiques : nombre de billets authentiques et nombre de faux billets détectés ;
   - un tableau détaillé avec, pour chaque billet, sa probabilité d'authenticité (`proba_vrai`) et sa prédiction (`prediction` : "Vrai" ou "Faux").
5. **Télécharger les résultats** au format CSV via le bouton dédié (`resultats_predictions.csv`).

### Saisie manuelle

1. Ouvrez l'onglet **✍️ Saisie manuelle**.
2. Renseignez les 6 mesures géométriques du billet dans le formulaire.
3. Cliquez sur **Vérifier ce billet**.
4. Le résultat s'affiche immédiatement (billet authentique ✅ ou faux billet 🚫), avec la probabilité associée.

## Format du CSV attendu

Le fichier CSV doit contenir au minimum les colonnes suivantes (noms exacts définis dans `model_config.json`) :

- `length` — longueur du billet (mm)
- `height_left` — hauteur côté gauche (mm)
- `height_right` — hauteur côté droit (mm)
- `margin_up` — marge supérieure (mm)
- `margin_low` — marge inférieure (mm)
- `diagonal` — diagonale du billet (mm)

Le séparateur (`,` ou `;`) est détecté automatiquement. Toute colonne manquante entraîne l'arrêt de l'analyse avec un message précisant les colonnes absentes.

## Structure du projet

```
.
├── app_streamlit.py          # Application Streamlit (interface web)
├── app.py                    # Version en ligne de commande
├── random_forest_model.joblib
├── imputer.joblib
└── model_config.json
```

## Alternative en ligne de commande

Le fichier `Meloen_Arnaud_2_scrypt_app_072026` permet d'effectuer les mêmes analyses sans interface graphique, utile pour l'automatisation ou l'intégration dans un pipeline. Il nécessite les mêmes prérequis, sans Streamlit. Pour plus de détails sur le processus et les commandes ci-dessous, se reporter au fichier README_app.md 

```bash
# Un seul billet
python Meloen_Arnaud_2_scrypt_app_072026 --length 113.2 --height_left 104.0 --height_right 103.9 --margin_up 3.1 --margin_low 4.1 --diagonal 172.0

# Un fichier de plusieurs billets
python Meloen_Arnaud_2_scrypt_app_072026 --csv billets_production.csv

# Sauvegarder le résultat dans un fichier
python Meloen_Arnaud_2_scrypt_app_072026 --csv billets_production.csv --output resultats.csv
```
