from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(pipeline, X_test, y_test):
    # Predict using the trained pipeline
    y_pred = pipeline.predict(X_test)
    
    # Display accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f"Précision : {accuracy:.2f}")
    
    # Display classification report
    st.write("Rapport de classification :")
    st.code(classification_report(y_test, y_pred), language='plaintext')
    
    # Display confusion matrix
    st.subheader("Matrice de confusion")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", ax=ax)
    ax.set_ylabel("Vraie classe")
    ax.set_xlabel("Classe prédite")
    st.pyplot(fig)


def predict_target(pipeline, feature_names):
    st.subheader("Prédisez une nouvelle valeur")
    
    # Create input fields for each feature
    user_inputs = {}
    for feature in feature_names:
        user_inputs[feature] = st.number_input(f"Entrez une valeur pour {feature}:", value=0.0)
    
    # Convert inputs to DataFrame for prediction
    input_df = pd.DataFrame([user_inputs])  # Create a single-row DataFrame
    
    if st.button("Prédire"):
        # Use the pipeline to predict the target
        prediction = pipeline.predict(input_df)
        st.success(f"Prédiction : {prediction[0]}")
