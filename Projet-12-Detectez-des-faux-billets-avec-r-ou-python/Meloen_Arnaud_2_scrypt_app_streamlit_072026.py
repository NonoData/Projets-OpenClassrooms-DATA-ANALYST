import streamlit as st
import pandas as pd
import joblib
import json
from pathlib import Path

# Configuration de la page
st.set_page_config(page_title="Détecteur de Faux Billets - ONCFM", layout="centered")

st.title("🔍 Détecteur de Faux Billets ")
#st.write("Importez un fichier CSV contenant les dimensions des billets pour lancer l'analyse.")

# --- Chargement des fichiers ---
BASE_DIR = Path(__file__).resolve().parent

@st.cache_resource # Évite de recharger le modèle à chaque interaction
def load_assets():
    model = joblib.load(BASE_DIR / "random_forest_model.joblib")
    imputer = joblib.load(BASE_DIR / "imputer.joblib")
    with open(BASE_DIR / "model_config.json", encoding="utf-8") as f:
        config = json.load(f)
    return model, imputer, config

try:
    model, imputer, config = load_assets()
except Exception as e:
    st.error(f"Erreur lors du chargement du modèle : {e}")
    st.stop()

FEATURES = config["features"]
THRESHOLD = config["threshold"]

# Libellés lisibles pour les champs de saisie manuelle (fallback : nom brut)
LABELS = {
    "length": "Longueur (length, mm)",
    "height_left": "Hauteur côté gauche (height_left, mm)",
    "height_right": "Hauteur côté droit (height_right, mm)",
    "margin_up": "Marge supérieure (margin_up, mm)",
    "margin_low": "Marge inférieure (margin_low, mm)",
    "diagonal": "Diagonale (diagonal, mm)",
}


def predict_df(df: pd.DataFrame) -> pd.DataFrame:
    """Applique l'imputer + le modèle à un DataFrame contenant les colonnes FEATURES.

    Retourne le DataFrame d'origine enrichi des colonnes proba_vrai / prediction.
    """
    X = df[FEATURES].copy()
    X_imputed = imputer.transform(X)
    probas = model.predict_proba(X_imputed)[:, 1]
    predictions = ["Vrai" if p >= THRESHOLD else "Faux" for p in probas]

    result = df.copy()
    result["proba_vrai"] = probas
    result["prediction"] = predictions
    return result


tab_csv, tab_manuel = st.tabs(["📄 Fichier CSV", "✍️ Saisie manuelle"])

# ---------------------------------------------------------------------------
# ONGLET 1 : Import CSV (comportement inchangé)
# ---------------------------------------------------------------------------
with tab_csv:
    st.subheader("Importez votre fichier CSV")
    uploaded_file = st.file_uploader(
        "Glissez-déposez le fichier CSV comportant les dimensions des billets à analyser ici ⬇️",
        type=["csv"]
    )

    if uploaded_file is not None:
        # Lecture automatique du séparateur (virgule ou point-virgule)
        df = pd.read_csv(uploaded_file, sep=None, engine="python")

        st.write("### Aperçu des données importées :")
        st.dataframe(df.head())

        if st.button("Lancer l'analyse des billets", type="primary"):
            # Vérification de la présence des colonnes requises
            missing_cols = [c for c in FEATURES if c not in df.columns]
            if missing_cols:
                st.error(f"Erreur : Le fichier CSV ne contient pas toutes les colonnes nécessaires. Colonnes manquantes : {missing_cols}")
                st.stop()

            df_result = predict_df(df)
            predictions = df_result["prediction"].tolist()

            # Statistiques rapides
            n_vrai = predictions.count("Vrai")
            n_faux = predictions.count("Faux")

            st.write("---")
            st.subheader("📊 Résultats de l'analyse")

            col1, col2 = st.columns(2)
            col1.metric("Billets Authentiques (Vrai)", n_vrai)
            col2.metric("Faux Billets détectés (Faux)", n_faux)

            # Affichage du tableau complet avec mise en valeur
            st.write("### Tableau détaillé des prédictions :")
            st.dataframe(df_result.style.highlight_max(axis=0, subset=["proba_vrai"]))

            # Bouton de téléchargement pour le résultat obtenu
            csv_result = df_result.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Télécharger les résultats (CSV)",
                data=csv_result,
                file_name="resultats_predictions.csv",
                mime="text/csv"
            )

# ---------------------------------------------------------------------------
# ONGLET 2 : Saisie manuelle d'un seul billet
# ---------------------------------------------------------------------------
with tab_manuel:
    st.subheader("Analysez un billet en saisissant ses dimensions")
    st.write("Renseignez les 6 mesures géométriques du billet, puis cliquez sur *Vérifier ce billet*.")

    with st.form("form_saisie_manuelle"):
        # Génère automatiquement un champ numérique pour chaque feature attendue par le modèle
        cols = st.columns(2)
        valeurs = {}
        for i, feat in enumerate(FEATURES):
            with cols[i % 2]:
                valeurs[feat] = st.number_input(
                    LABELS.get(feat, feat),
                    min_value=0.0,
                    value=100.0,
                    step=0.1,
                    format="%.2f",
                )
        submitted = st.form_submit_button("Vérifier ce billet", type="primary")

    if submitted:
        df_manuel = pd.DataFrame([valeurs])
        df_result = predict_df(df_manuel)

        proba = df_result.loc[0, "proba_vrai"]
        prediction = df_result.loc[0, "prediction"]

        st.write("---")
        st.subheader("📊 Résultat de l'analyse")

        if prediction == "Vrai":
            st.success(f"✅ Billet **authentique** (probabilité : {proba:.2%})")
        else:
            st.error(f"🚫 **Faux billet** détecté (probabilité d'authenticité : {proba:.2%})")

        st.write("### Détail des valeurs saisies :")
        st.dataframe(df_result)
