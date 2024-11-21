import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def process_data(data):
    st.subheader("Analyse Descriptive")
    st.write(data.describe())
    
    st.subheader("Graphique de distribution")
    st.hist(data["alcohol"])
    
    st.subheader("Pairplot")
    st.pyplot(sns.pairplot(data, hue="quality"))
    
    st.subheader("Matrice de corrélation")
    st.heatmap(data.corr(), annot=True)
    
    st.subheader("Gestion des valeurs manquantes")
    missing_data = data.isnull().sum()
    st.write(missing_data[missing_data > 0])
    method = st.radio("Choisissez une méthode pour traiter les valeurs manquantes:", ("Supprimer", "Imputer"))
    if method == "Imputer":
        imputation_method = st.selectbox("Choisissez la méthode d'imputation:", ["Mean", "Median", "Mode"])
        if imputation_method == "Mean":
            data = data.fillna(data.mean())
        elif imputation_method == "Median":
            data = data.fillna(data.median())
        else:
            data = data.fillna(data.mode().iloc[0])
        st.write("Valeurs manquantes imputées")
    else:
        data = data.dropna()
        st.write("Lignes avec valeurs manquantes supprimées")
    
    return data
