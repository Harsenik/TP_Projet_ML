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
        # Affichage de la distribution d'une colonne
        column = st.selectbox("Choisissez une colonne pour la distribution", df.columns)
        fig, ax = plt.subplots()
        sns.histplot(df[column], kde=True, ax=ax)
        st.pyplot(fig)
    elif graph_type == "Corrélation":
        # Affichage de la matrice de corrélation
        newDf = df.drop(columns=df.columns[0])
        newDf = newDf.drop(columns=['target'])
        corr = newDf.corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    elif graph_type == "Pairplot":
        # Affichage du pairplot
        selected_columns = st.multiselect(
            "Sélectionnez les colonnes pour le pairplot",
            df.columns.tolist(),
            default=df.columns.tolist()
        )
        
        #Enlève warning
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.markdown("*Sélection 'target' obligatoire*")
        if 'target' not in selected_columns:
            selected_columns.append('target')
        if len(selected_columns) > 1:
            sns.pairplot(df[selected_columns], hue='target')
            st.pyplot()
        else:
            st.warning("Veuillez sélectionner au moins deux colonnes.")

    # Affichage des fréquences des valeurs
    if st.checkbox("Afficher les fréquences des valeurs"):
        column = st.selectbox("Choisissez une colonne pour voir les fréquences", df.columns)
        st.write(df[column].value_counts())

def handle_missing_values(df):
    st.subheader("Gestion des valeurs manquantes")
    missing_values = df.isnull().sum()
    st.write("Valeurs manquantes par colonne :")
    st.table(missing_values)

    # Choix de la méthode de gestion des valeurs manquantes
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
    # Conversion des valeurs de la colonne target en entiers
    mapping = {'Vin amer': 1, 'Vin éuilibré': 2, 'Vin sucré': 3}
    df['target'] = df['target'].map(mapping)
    return df
