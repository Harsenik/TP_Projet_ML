import streamlit as st
from .chargement_donnees import load_data
from .procession_donnees import process_data
from .pipeline import run_model_pipeline
from .evaluation import evaluate_model

st.set_page_config(
    page_title="Projet ML",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    tabs_1, tabs_2, tabs_3, tabs_4 = st.tabs(["Traitement des données", "Visualisations", "Modélisation", "Évaluation"])
    
    with tabs_1:
        data = load_data()
        processed_data = process_data(data)
    
    with tabs_2:
        st.write("Visualisations à implémenter ici.")
    
    with tabs_3:
        model, predictions, y_test = run_model_pipeline(processed_data)
    
    with tabs_4:
        evaluate_model(model, y_test, predictions)

if __name__ == "__main__":
    main()
