from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(pipeline, X_test, y_test):
    y_pred = pipeline.predict(X_test)
    
    st.subheader("Évaluation du modèle")
    st.write(f"Précision : {accuracy_score(y_test, y_pred):.2f}")
    
    st.write("Rapport de classification :")
    st.text(classification_report(y_test, y_pred))
    
    st.subheader("Matrice de confusion")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', ax=ax)
    plt.ylabel('Vraie classe')
    plt.xlabel('Classe prédite')
    st.pyplot(fig)
