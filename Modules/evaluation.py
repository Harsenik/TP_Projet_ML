from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def evaluate_model(pipeline, X_test, y_test):
    # Prédiction sur l'ensemble de test
    y_pred = pipeline.predict(X_test)

    # Affichage de la précision globale du modèle
    st.subheader("Évaluation du modèle")
    st.write(f"Précision : {accuracy_score(y_test, y_pred):.2f}")
    
    # Affichage du rapport de classification détaillé
    st.write("Rapport de classification :")
    st.text(classification_report(y_test, y_pred))

    # Création et affichage de la matrice de confusion
    st.subheader("Matrice de confusion")
    cm = confusion_matrix(y_test, y_pred)
    # Conversion de la matrice en pourcentages
    cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    
    # Création de la figure pour la matrice de confusion
    fig, ax = plt.subplots(figsize=(10, 8))

    # Définir les labels personnalisés
    labels = ['Vin amer', 'Vin équilibré', 'Vin sucré']
    
    # Créer la heatmap avec les labels personnalisés
    sns.heatmap(cm_percent, annot=True, fmt='.2%', cmap='Blues',xticklabels=labels, yticklabels=labels, ax=ax)
    plt.ylabel('Classe réelle')
    plt.xlabel('Classe prédite')
    plt.title('Matrice de Confusion')
    
    # Ajout d'une légende pour la barre de couleur
    cbar = ax.collections[0].colorbar
    cbar.set_label('Pourcentage de prédictions')
    
    # Affichage de la figure dans Streamlit
    st.pyplot(fig)

    # Calcul des métriques supplémentaires
    precision = cm[1,1] / (cm[1,1] + cm[0,1])
    recall = cm[1,1] / (cm[1,1] + cm[1,0])
    f1_score = 2 * (precision * recall) / (precision + recall)

    # Affichage des métriques supplémentaires
    st.write(f"Précision : {precision:.2f}")
    st.write(f"Rappel : {recall:.2f}")
    st.write(f"Score F1 : {f1_score:.2f}")

    # Explication de la matrice de confusion
    st.write("""
    La matrice de confusion montre :
    - En diagonale : les prédictions correctes
    - Hors diagonale : les erreurs de classification
    Une matrice idéale aurait des valeurs élevées uniquement sur la diagonale.
    """)
