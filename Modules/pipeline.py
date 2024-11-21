from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

def create_ml_pipeline(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    algorithm = st.selectbox("Choisissez un algorithme", ["Régression Logistique", "Random Forest"])

    if algorithm == "Régression Logistique":
        model = LogisticRegression()
    else:
        model = RandomForestClassifier()

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', model)
    ])

    pipeline.fit(X_train, y_train)
    
    st.success("Modèle entraîné avec succès!")
    
    return pipeline, X_test, y_test
