#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "random_forest_model.joblib"
IMPUTER_PATH = BASE_DIR / "imputer.joblib"
CONFIG_PATH = BASE_DIR / "model_config.json"


# ---------------------------------------------------------------------------
# Chargement des artefacts du modèle
# ---------------------------------------------------------------------------

def load_artifacts():
    """Charge le modèle, l'imputer et la configuration (seuil, variables).

    Lève une erreur explicite si l'un des fichiers est manquant, plutôt
    qu'une trace d'erreur sklearn/joblib peu compréhensible.
    """
    missing = [p.name for p in (MODEL_PATH, IMPUTER_PATH, CONFIG_PATH) if not p.exists()]
    if missing:
        print(
            "Erreur : fichier(s) manquant(s) dans le dossier de l'application : "
            + ", ".join(missing)
            + "\nCes fichiers doivent être générés depuis le notebook "
            "(export du modèle, de l'imputer et de la configuration).",
            file=sys.stderr,
        )
        sys.exit(1)

    model = joblib.load(MODEL_PATH)
    imputer = joblib.load(IMPUTER_PATH)
    with open(CONFIG_PATH, encoding="utf-8") as f:
        config = json.load(f)

    if "threshold" not in config or "features" not in config:
        print(
            "Erreur : model_config.json doit contenir les clés 'threshold' et 'features'.",
            file=sys.stderr,
        )
        sys.exit(1)

    return model, imputer, config


# ---------------------------------------------------------------------------
# Prédiction
# ---------------------------------------------------------------------------

def predict(df: pd.DataFrame, model, imputer, config: dict) -> pd.DataFrame:
    """Applique le modèle à un DataFrame de billets et retourne le résultat.

    Ajoute deux colonnes au DataFrame d'origine :
        - proba_vrai : probabilité que le billet soit authentique
        - prediction : "Vrai" ou "Faux", selon le seuil retenu (0.8 par défaut)
    """
    features = config["features"]
    threshold = config["threshold"]

    missing_cols = [c for c in features if c not in df.columns]
    if missing_cols:
        raise ValueError(
            f"Colonnes manquantes dans les données d'entrée : {missing_cols}. "
            f"Colonnes attendues : {features}"
        )

    X = df[features].copy()

    # Les colonnes doivent être numériques (garde-fou contre un CSV mal formé)
    non_numeric = [c for c in features if not pd.api.types.is_numeric_dtype(X[c])]
    if non_numeric:
        raise ValueError(f"Colonnes non numériques détectées : {non_numeric}")

    X_imputed = pd.DataFrame(imputer.transform(X), columns=features, index=X.index)

    probas = model.predict_proba(X_imputed)[:, 1]  # probabilité de la classe "Vrai"
    predictions = np.where(probas >= threshold, "Vrai", "Faux")

    result = df.copy()
    result["proba_vrai"] = probas.round(4)
    result["prediction"] = predictions
    return result


# ---------------------------------------------------------------------------
# Construction du DataFrame d'entrée
# ---------------------------------------------------------------------------

GEOMETRIC_ARGS = ["length", "height_left", "height_right", "margin_up", "margin_low", "diagonal"]


def build_single_billet_df(args) -> pd.DataFrame:
    """Construit un DataFrame à une ligne à partir des arguments en ligne de commande."""
    values = {name: getattr(args, name) for name in GEOMETRIC_ARGS}
    missing = [name for name, v in values.items() if v is None]
    if missing:
        print(
            "Erreur : il manque les valeurs géométriques suivantes : "
            + ", ".join(missing)
            + "\nFournissez soit --csv <fichier>, soit les 6 valeurs géométriques "
            "(--length, --height_left, --height_right, --margin_up, --margin_low, --diagonal).",
            file=sys.stderr,
        )
        sys.exit(1)
    return pd.DataFrame([values])


def load_csv_df(csv_path: str) -> pd.DataFrame:
    """Charge un fichier CSV de billets, avec un message d'erreur clair si échec."""
    path = Path(csv_path)
    if not path.exists():
        print(f"Erreur : le fichier '{csv_path}' n'existe pas.", file=sys.stderr)
        sys.exit(1)
    try:
        # Les fichiers billets fournis par l'ONCFM utilisent ';' comme séparateur ;
        # on détecte automatiquement entre ',' et ';'.
        df = pd.read_csv(path, sep=None, engine="python")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV : {e}", file=sys.stderr)
        sys.exit(1)
    if df.empty:
        print("Erreur : le fichier CSV est vide.", file=sys.stderr)
        sys.exit(1)
    return df


# ---------------------------------------------------------------------------
# Point d'entrée
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="Détection automatique de faux billets — ONCFM (modèle Random Forest).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--csv", type=str, default=None,
        help="Chemin vers un fichier CSV contenant plusieurs billets "
             "(colonnes : length, height_left, height_right, margin_up, margin_low, diagonal).",
    )
    parser.add_argument("--length", type=float, default=None, help="Longueur du billet (mm)")
    parser.add_argument("--height_left", type=float, default=None, help="Hauteur côté gauche (mm)")
    parser.add_argument("--height_right", type=float, default=None, help="Hauteur côté droit (mm)")
    parser.add_argument("--margin_up", type=float, default=None, help="Marge supérieure (mm)")
    parser.add_argument("--margin_low", type=float, default=None, help="Marge inférieure (mm)")
    parser.add_argument("--diagonal", type=float, default=None, help="Diagonale du billet (mm)")
    parser.add_argument(
        "--output", type=str, default=None,
        help="Chemin d'un fichier CSV où sauvegarder les résultats (optionnel).",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    model, imputer, config = load_artifacts()

    if args.csv:
        df = load_csv_df(args.csv)
    else:
        df = build_single_billet_df(args)

    try:
        result = predict(df, model, imputer, config)
    except ValueError as e:
        print(f"Erreur : {e}", file=sys.stderr)
        sys.exit(1)

    # Affichage lisible dans le terminal
    pd.set_option("display.width", 120)
    print(result.to_string(index=False))

    n_faux = (result["prediction"] == "Faux").sum()
    n_vrai = (result["prediction"] == "Vrai").sum()
    print(f"\nRésumé : {len(result)} billet(s) analysé(s) — {n_vrai} vrai(s), {n_faux} faux.")
    print(f"Seuil de décision utilisé : {config['threshold']}")

    if args.output:
        result.to_csv(args.output, index=False)
        print(f"\nRésultats sauvegardés dans : {args.output}")


if __name__ == "__main__":
    main()