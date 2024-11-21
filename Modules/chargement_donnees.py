import pandas as pd
import streamlit as st

def load_data():
    uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("Données chargées avec succès!")
        st.write(df.head())
        return df
    else:
        st.warning("Veuillez charger un fichier CSV.")
        return None

def display_data_info(df):
    if df is not None:
        st.subheader("Informations sur le dataset")
        st.write(f"Nombre de lignes : {df.shape[0]}")
        st.write(f"Nombre de colonnes : {df.shape[1]}")
        st.write("Types de données :")
        st.write(df.dtypes)
