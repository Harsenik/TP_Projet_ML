import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path="C:\\Users\\henri\\OneDrive\\Documents\\Cours Diginamic\\30. Projet - Conception et développement d'IA 3J\\vin.csv"):
    data = pd.read_csv(path)
    return data