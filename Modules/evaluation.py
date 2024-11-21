from turtle import st
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, classification_report, confusion_matrix

def evaluate_model(model, y_test, predictions):
    st.subheader("Évaluation du modèle")
    
    if isinstance(model, (LinearRegression, RandomForestRegressor)):
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        st.write(f"Mean Squared Error: {mse}")
        st.write(f"R² Score: {r2}")
        
    else:
        st.write("Classification Report:")
        st.text(classification_report(y_test, predictions))
        
        st.write("Confusion Matrix:")
        cm = confusion_matrix(y_test, predictions)
        sns.heatmap(cm, annot=True)
