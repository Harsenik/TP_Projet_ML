from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np

def create_ml_pipeline(df, target_column):
    # Séparation features/target et suppression de la colonne Unnamed: 0
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Détection automatique du type de problème
    n_classes = len(np.unique(y))
    problem_type = "Classification" if n_classes <= 10 else "Régression"
    st.write(f"Type de problème détecté : {problem_type}")

    # Choix de l'algorithme selon le type de problème
    if problem_type == "Classification":
        options = {
            "Régression Logistique": LogisticRegression(),
            "Random Forest": RandomForestClassifier(),
            "SVM": SVC(),
            "KNN": KNeighborsClassifier()
        }
    else:
        st.error("Seule la classification est supportée pour le moment")
        return None, None, None

    # Split des données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Interface utilisateur pour le choix du modèle
    algorithm = st.selectbox("Choisissez un algorithme", list(options.keys()))
    
    # Configuration des hyperparamètres
    model = options[algorithm]
    if algorithm == "Régression Logistique":
        C = st.slider("Régularisation (C)", 0.01, 10.0, 1.0)
        model.set_params(C=C)
    elif algorithm == "Random Forest":
        n_estimators = st.slider("Nombre d'arbres", 10, 200, 100)
        max_depth = st.slider("Profondeur maximale", 1, 20, 5)
        model.set_params(n_estimators=n_estimators, max_depth=max_depth)
    elif algorithm == "SVM":
        C = st.slider("Régularisation (C)", 0.01, 10.0, 1.0)
        kernel = st.selectbox("Kernel", ["rbf", "linear", "poly"])
        model.set_params(C=C, kernel=kernel)
    elif algorithm == "KNN":
        n_neighbors = st.slider("Nombre de voisins", 1, 20, 5)
        model.set_params(n_neighbors=n_neighbors)

    # Création et entraînement du pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', model)
    ])
    
    with st.spinner("Entraînement du modèle en cours..."):
        pipeline.fit(X_train, y_train)
    
    st.success("Modèle entraîné avec succès!")

    # Prédiction sur de nouvelles données
    st.subheader("Prédiction sur de nouvelles données")
    if st.checkbox("Faire une prédiction"):
        new_data = {}
        for col in X.columns:
            new_data[col] = st.number_input(f"Entrez la valeur pour {col}", value=float(X[col].mean()))
        
        new_df = pd.DataFrame([new_data])
        
        # Définir le dictionnaire de conversion avant la prédiction
        wine_types = {
            1: "Vin amer",
            2: "Vin équilibré",
            3: "Vin sucré"
        }
        
        # Faire la prédiction et la convertir
        try:
            prediction = pipeline.predict(new_df)
            predicted_wine = wine_types[prediction[0]]
            st.success(f"Prédiction : {predicted_wine}")
        except Exception as e:
            st.error(f"Erreur lors de la prédiction : {str(e)}")

    return pipeline, X_test, y_test
