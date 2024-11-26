# Importation des modules nécessaires
import streamlit as st
import pandas as pd
import joblib
from Modules import chargement_donnees
from Modules.procession_donnees import analyze_data, handle_missing_values, handle_target_parsing
from Modules.pipeline import create_ml_pipeline
from Modules.evaluation import evaluate_model

# Configuration de l'affichage pandas
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def main():
    # Configuration de la page Streamlit
    st.set_page_config(page_title="Analyse de Vin", layout="wide")
    st.title("Analyse de Vin")

    # Initialiser la session state
    if 'df' not in st.session_state:
        st.session_state.df = None
    if 'model' not in st.session_state:
        st.session_state.model = None

    # Menu avec onglets
    tabs = st.tabs(["Chargement des données", "Visualisation & Traitement des données", "Machine Learning", "Évaluation"])

    # Contenu des onglets
    with tabs[0]:
        load_data_tab()
    with tabs[1]:
        process_data_tab()
    with tabs[2]:
        ml_pipeline_tab()
    with tabs[3]:
        evaluate_model_tab()

def load_data_tab():
    # Onglet de chargement des données
    st.title("Chargement des données")
    st.session_state.df = chargement_donnees.load_data()
    if st.session_state.df is not None:
        chargement_donnees.display_data_info(st.session_state.df)

def process_data_tab():
    # Onglet de traitement et visualisation des données
    if st.session_state.df is not None:
        subTabs = st.tabs(["Visualisation des données", "Traitement des données"])
        with subTabs[0]:
            st.header("Visualisation des données")
            analyze_data(st.session_state.df)
        with subTabs[1]:
            st.header("Traitement des données")
            st.session_state.df = handle_missing_values(st.session_state.df)
            st.session_state.df = handle_target_parsing(st.session_state.df)
            # Sélection de colonnes
            selected_columns = st.multiselect("Sélectionnez les colonnes à conserver", st.session_state.df.columns)
            if selected_columns:
                st.session_state.df = st.session_state.df[selected_columns]
                st.success(f"Colonnes sélectionnées : {', '.join(selected_columns)}")
    else:
        st.warning("Veuillez d'abord charger des données dans l'onglet 'Chargement des données'.")

def ml_pipeline_tab():
    # Onglet de machine learning
    if st.session_state.df is not None:
        st.header("Pipeline de Machine Learning")
        target_column = st.selectbox("Choisissez la colonne cible", st.session_state.df.columns)
        if target_column != "Unnamed: 0":
            st.session_state.model, X_test, y_test = create_ml_pipeline(st.session_state.df, target_column)
            st.session_state.X_test = X_test
            st.session_state.y_test = y_test
            st.success("Modèle entraîné avec succès!")

            # Boutons pour sauvegarder et charger le modèle
            if st.button("Sauvegarder le modèle"):
                joblib.dump(st.session_state.model, 'wine_model.joblib')
                st.success("Modèle sauvegardé avec succès!")
            if st.button("Charger un modèle"):
                try:
                    st.session_state.model = joblib.load('wine_model.joblib')
                    st.success("Modèle chargé avec succès!")
                except:
                    st.error("Aucun modèle sauvegardé trouvé.")
    else:
        st.warning("Veuillez d'abord charger et traiter les données.")

def evaluate_model_tab():
    # Onglet d'évaluation du modèle
    if st.session_state.model is not None:
        st.header("Évaluation du modèle")
        evaluate_model(st.session_state.model, st.session_state.X_test, st.session_state.y_test)
    else:
        st.warning("Veuillez d'abord entraîner un modèle dans l'onglet 'Machine Learning'.")

if __name__ == "__main__":
    main()
