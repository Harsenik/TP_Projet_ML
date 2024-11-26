import pandas as pd
import streamlit as st

### Permet à l'utilisateur de choisir lui même le CSV à charger
# def load_data():
#     uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
#     if uploaded_file is not None:
#         df = pd.read_csv(uploaded_file)
#         st.success("Données chargées avec succès!")
#         st.write("Aperçu des données (5 premières lignes) :")
#         st.write(df.head())
#         return df
#     else:
#         st.warning("Veuillez charger un fichier CSV.")
#         return None

## Charge automatiquement les données de vin.csv  
def load_data():
    st.write("Chargement automatique de vin.csv")
    df = pd.read_csv("Modules/vin.csv")
    # print(df)
    if df is not None:
        st.success("Données chargées avec succès !")
        st.write("Aperçu des données (5 premières lignes) :")
        st.write(df.head())
        return df
    else:
        st.warning("Echec du chargement automatique des données.")
        return None

## Afficher informations sur le dataset
def display_data_info(df):
    if df is not None:
        st.subheader("Informations sur le dataset")
        st.write(f"Nombre de lignes : {df.shape[0]}")
        st.write(f"Nombre de colonnes : {df.shape[1]}")

        # Créer un DataFrame pour les types de données avec des titres personnalisés
        dtypes_df = pd.DataFrame({
            'Type': df.dtypes
        })
    if dtypes_df is not None:    
        st.write("Types de données :")
        st.table(dtypes_df)