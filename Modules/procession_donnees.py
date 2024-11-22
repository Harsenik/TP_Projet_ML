import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_data(df):
    st.subheader("Analyse descriptive")
    st.write(df.describe())

    st.subheader("Distribution des variables")
    column = st.selectbox("Choisissez une colonne pour la distribution", df.columns)
    fig, ax = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Matrice de corrélation")
    newDf = df.drop(columns= df.columns[0])  
    newDf = newDf.drop(columns=['target'])
    corr = newDf.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
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
