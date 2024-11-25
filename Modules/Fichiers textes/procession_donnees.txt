import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_data(df):
    st.subheader("Analyse descriptive")
    st.write(df.describe())

    # Graphiques disponibles
    graph_type = st.selectbox("Choisissez le type de graphique", 
                             ["Distribution", "Corrélation", "Régression"])

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

    elif graph_type == "Régression":
        # Sélection des colonnes pour la régression
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        x_col = st.selectbox("Choisissez la variable X", numeric_cols)
        y_col = st.selectbox("Choisissez la variable Y", numeric_cols)
        
        fig = plt.figure(figsize=(10, 6))
        sns.lmplot(x=x_col, y=y_col, data=df, hue='target', 
                  markers=['o', 's', 'D'],
                  palette='colorblind', 
                  height=6, 
                  aspect=1.5, 
                  ci=None)
        plt.title(f"Régression linéaire : {x_col} vs {y_col}")
        st.pyplot(fig)

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