from turtle import st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

def run_model_pipeline(data):
    X = data.drop('quality', axis=1)
    y = data['quality']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    st.subheader("Choix du modèle")
    model_type = st.selectbox("Choisissez un modèle:", ["Regression", "Classification"])
    
    if model_type == "Regression":
        model_choice = st.selectbox("Choisissez un modèle de régression:", ["Linear Regression", "Random Forest Regressor"])
        if model_choice == "Linear Regression":
            model = LinearRegression().fit(X_train, y_train)
        else:
            model = RandomForestRegressor().fit(X_train, y_train)
    
    else:
        model_choice = st.selectbox("Choisissez un modèle de classification:", ["Logistic Regression", "Random Forest Classifier"])
        if model_choice == "Logistic Regression":
            model = LogisticRegression().fit(X_train, y_train)
        else:
            model = RandomForestClassifier().fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    
    return model, predictions, y_test
