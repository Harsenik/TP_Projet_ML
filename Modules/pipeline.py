from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd


def update_selection():
    st.session_state.selected_option = st.session_state.selectbox

def create_ml_pipeline(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Ensure target is categorical
    if y.dtype in ['float64', 'int64'] and not all(y.astype(int) == y):
        st.warning("Converting continuous target to categorical for classification.")
        y = pd.qcut(y, q=2, labels=False)  # Binary classification

    
    options = ["Choisissez un algorithme","Régression Logistique", "Random Forest", "SVM", "KNN" ,]


    print(train_test_split(X, y, test_size=0.2, random_state=42))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    algorithm = st.selectbox("Choisissez un algorithme", options,key="selectbox", on_change=update_selection )

    # Display the selected option
    if algorithm:
        st.write(f"You selected: {algorithm}")
        
        if algorithm == "Régression Logistique":
            C = st.slider("C", 0.01, 10.0, 1.0)
            model = LogisticRegression(C=C)
        elif algorithm == "Random Forest":
            n_estimators = st.slider("Nombre d'arbres", 10, 200, 100)
            model = RandomForestClassifier(n_estimators=n_estimators)
        elif algorithm == "SVM":
            C = st.slider("C", 0.01, 10.0, 1.0)
            kernel = st.selectbox("Kernel", ["rbf", "linear", "poly"])
            model = SVC(C=C, kernel=kernel)
        else:
            n_neighbors = st.slider("Nombre de voisins", 1, 20, 5)
            model = KNeighborsClassifier(n_neighbors=n_neighbors)


    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', model)
    ])

    pipeline.fit(X_train, y_train)
    
    st.success("Modèle entraîné avec succès!")
    
    return pipeline, X_test, y_test
