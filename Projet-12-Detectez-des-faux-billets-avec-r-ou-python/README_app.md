# Détection automatique de faux billets — ONCFM (Ligne de commande)

Application en ligne de commande qui utilise un modèle **Random Forest** optimisé pour détecter automatiquement les faux billets à partir de leurs caractéristiques géométriques.

Le modèle a été entraîné et optimisé dans le notebook `Meloen_Arnaud_1_Notebook_analyse_072026.ipynb`. Cette application charge les artefacts exportés (modèle, imputer, configuration) et les applique à un billet unique ou à un lot de billets fourni sous forme de fichier CSV.

## Prérequis

- Python 3.8+
- Les librairies suivantes :
  - `pandas`
  - `numpy`
  - `joblib`

Installation rapide :

```bash
pip install pandas numpy joblib scikit-learn
```

## Fichiers requis

Avant de pouvoir exécuter l'application, **trois fichiers doivent être présents dans le même dossier que `Meloen_Arnaud_2_scrypt_app_072026.py`** (générés une seule fois depuis le notebook, via le bloc d'export prévu à cet effet) :

| Fichier | Description |
|---|---|
| `random_forest_model.joblib` | Modèle Random Forest optimisé (issu du `GridSearchCV`) |
| `imputer.joblib` | `SimpleImputer(strategy="median")` entraîné sur les données d'entraînement, pour gérer les valeurs manquantes |
| `model_config.json` | Fichier de configuration contenant le seuil de décision et la liste des variables attendues, au format :<br>`{"threshold": 0.8, "features": [...]}` |

Si l'un de ces fichiers est manquant, l'application affiche un message d'erreur explicite et s'arrête proprement (au lieu d'un traceback sklearn/joblib difficile à interpréter).

## Utilisation

### 1. Analyser un seul billet

Fournissez les 6 caractéristiques géométriques du billet en argument (en millimètres) :

```bash
python Meloen_Arnaud_2_scrypt_app_072026.py --length 113.2 --height_left 104.0 --height_right 103.9 --margin_up 3.1 --margin_low 4.1 --diagonal 172.0
```

Arguments disponibles :

| Argument | Description |
|---|---|
| `--length` | Longueur du billet (mm) |
| `--height_left` | Hauteur côté gauche (mm) |
| `--height_right` | Hauteur côté droit (mm) |
| `--margin_up` | Marge supérieure (mm) |
| `--margin_low` | Marge inférieure (mm) |
| `--diagonal` | Diagonale du billet (mm) |

Les 6 valeurs sont obligatoires si `--csv` n'est pas utilisé.

### 2. Analyser plusieurs billets à partir d'un fichier CSV

```bash
python Meloen_Arnaud_2_scrypt_app_072026.py --csv billets_production.csv
```
(noter après '--csv' le nom du fichier contenant les billets à analyser)

Le fichier CSV doit contenir au minimum les colonnes suivantes : `length`, `height_left`, `height_right`, `margin_up`, `margin_low`, `diagonal`.

Le séparateur (`,` ou `;`) est détecté automatiquement, ce qui permet de traiter aussi bien un CSV standard que les fichiers fournis par l'ONCFM (séparés par `;`).

### 3. Sauvegarder les résultats dans un fichier

Ajoutez l'option `--output` (fonctionne avec un billet unique ou un CSV) :

```bash
python Meloen_Arnaud_2_scrypt_app_072026.py --csv billets_production.csv --output resultats.csv
```
(noter après '--output' le nom voulu pour le fichier qui contiendra l'analyse des billets)

## Résultat produit

L'application ajoute deux colonnes au tableau d'origine :

- **`proba_vrai`** : probabilité (entre 0 et 1) que le billet soit authentique, arrondie à 4 décimales
- **`prediction`** : `"Vrai"` ou `"Faux"`, déterminée en comparant `proba_vrai` au seuil de décision défini dans `model_config.json` (0.8 par défaut)

Un résumé est affiché à la fin de l'exécution, indiquant le nombre total de billets analysés, le nombre de vrais et le nombre de faux, ainsi que le seuil de décision utilisé.

### Exemple de sortie terminal

```
 length  height_left  height_right  margin_up  margin_low  diagonal  proba_vrai prediction
  113.2        104.0         103.9        3.1         4.1     172.0      0.9421       Vrai

Résumé : 1 billet(s) analysé(s) — 1 vrai(s), 0 faux.
Seuil de décision utilisé : 0.8
```

## Gestion des erreurs

L'application vérifie et signale clairement plusieurs cas d'erreur courants, avec un message explicite plutôt qu'un traceback Python :

- fichiers de modèle manquants (`random_forest_model.joblib`, `imputer.joblib`, `model_config.json`)
- `model_config.json` incomplet (clés `threshold` ou `features` manquantes)
- fichier CSV introuvable, vide, ou illisible
- colonnes manquantes ou non numériques dans les données d'entrée
- valeurs géométriques manquantes lorsque `--csv` n'est pas utilisé

## Structure attendue du dossier

```
.
├── app.py
├── random_forest_model.joblib
├── imputer.joblib
├── model_config.json
└── billets_production.csv      (optionnel, le fichier d'entrée contenant les billets à analyser)
```
