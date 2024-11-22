from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import streamlit as st

def create_ml_pipeline(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    algorithm = st.selectbox("Choisissez un algorithme", ["Régression Logistique", "Random Forest", "SVM", "KNN"])

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
