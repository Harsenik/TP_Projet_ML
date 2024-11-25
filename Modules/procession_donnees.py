import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_data(df):
    st.subheader("Analyse descriptive")
    st.write(df.describe())

    # Graphiques disponibles
    graph_type = st.selectbox("Choisissez le type de graphique", ["Distribution", "Corrélation", "Pairplot"])

    if graph_type == "Distribution":
        column = st.selectbox("Choisissez une colonne pour la distribution", df.columns)
        fig, ax = plt.subplots()
        sns.histplot(df[column], kde=True, ax=ax)
        st.pyplot(fig)

    elif graph_type == "Corrélation":
        newDf = df.drop(columns=df.columns[0])
        newDf = newDf.drop(columns=['target'])
        corr = newDf.corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    elif graph_type == "Pairplot":
        sns.pairplot(df, hue='target')
        st.pyplot()

    if st.checkbox("Afficher les fréquences des valeurs"):
        column = st.selectbox("Choisissez une colonne pour voir les fréquences", df.columns)
        st.write(df[column].value_counts())

def handle_missing_values(df):
    st.subheader("Gestion des valeurs manquantes")
    missing_values = df.isnull().sum()
    st.write("Valeurs manquantes par colonne :")
    st.write(missing_values)

    method = st.selectbox("Choisissez une méthode pour gérer les valeurs manquantes", 
                          ["Supprimer", "Remplacer par la moyenne", "Remplacer par la médiane"])
    
    if method == "Supprimer":
        df = df.dropna()
    elif method == "Remplacer par la moyenne":
        df = df.fillna(df.mean())
    elif method == "Remplacer par la médiane":
        df = df.fillna(df.median())
    
    st.success("Valeurs manquantes traitées!")
    return df


def handle_target_parsing(df):
    # Mapping dictionary
    mapping = {'Vin amer': 1, 'Vin éuilibré': 2, 'Vin sucré': 3}
    # Map the string values to integers
    df['target'] = df['target'].map(mapping)
    # Ensure the column is of integer type
    # df['target'] = df['target'].astype(int)
    return df