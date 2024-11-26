from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
from sklearn.preprocessing import label_binarize
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def evaluate_model(pipeline, X_test, y_test):
    # Prédiction sur l'ensemble de test
    y_pred = pipeline.predict(X_test)
    y_proba = pipeline.predict_proba(X_test)

    # Affichage de la précision globale du modèle
    st.subheader("Évaluation du modèle")
    st.write(f"Précision : {accuracy_score(y_test, y_pred):.2f}")
    
    # Affichage du rapport de classification détaillé
    st.write("Rapport de classification :")
    st.text(classification_report(y_test, y_pred))

    # Création et affichage de la matrice de confusion
    st.subheader("Matrice de confusion")
    cm = confusion_matrix(y_test, y_pred)
    cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    
    # Création de la figure pour la matrice de confusion
    fig, ax = plt.subplots(figsize=(10, 8))

    # Définir les labels personnalisés
    labels = ['Vin amer', 'Vin équilibré', 'Vin sucré']
    
    # Créer la heatmap avec les labels personnalisés
    sns.heatmap(cm_percent, annot=True, fmt='.2%', cmap='Blues',
                xticklabels=labels, yticklabels=labels, ax=ax)
    plt.ylabel('Classe réelle')
    plt.xlabel('Classe prédite')
    plt.title('Matrice de Confusion')
    
    # Ajout d'une légende pour la barre de couleur
    cbar = ax.collections[0].colorbar
    cbar.set_label('Pourcentage de prédictions')
    
    # Affichage de la figure dans Streamlit
    st.pyplot(fig)

    # Courbe ROC
    st.subheader("Courbe ROC")
    
    # Binariser les labels pour la courbe ROC
    y_test_bin = label_binarize(y_test, classes=[1, 2, 3])
    n_classes = 3

    # Calculer ROC curve et ROC area pour chaque classe
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test_bin[:, i], y_proba[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Tracer la courbe ROC
    fig_roc, ax_roc = plt.subplots(figsize=(10, 6))
    
    for i in range(n_classes):
        plt.plot(fpr[i], tpr[i], 
                label=f'ROC curve for {labels[i]} (area = {roc_auc[i]:0.2f})')
    
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Taux de faux positifs')
    plt.ylabel('Taux de vrais positifs')
    plt.title('Courbe ROC multi-classes')
    plt.legend(loc="lower right")
    
    # Affichage de la courbe ROC dans Streamlit
    st.pyplot(fig_roc)

    # Explication de la matrice de confusion
    st.write("""
    La matrice de confusion montre :
    - En diagonale : les prédictions correctes
    - Hors diagonale : les erreurs de classification
    Une matrice idéale aurait des valeurs élevées uniquement sur la diagonale.
    """)

    # Explication de la courbe ROC
    st.write("""
    La courbe ROC (Receiver Operating Characteristic) :
    - Montre la performance du modèle pour chaque classe
    - Une courbe proche du coin supérieur gauche indique une meilleure performance
    - L'aire sous la courbe (AUC) proche de 1.0 indique une excellente classification
    """)
