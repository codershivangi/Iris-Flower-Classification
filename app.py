# app.py
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="Iris Flower Classifier", layout="centered")

st.title("🌸 Iris Flower Classification App")
st.write("Predict the Iris flower species based on sepal and petal measurements.")

# -----------------------------
# Load and Train Model
# -----------------------------
@st.cache_resource
def train_model():
    iris = load_iris()
    X = iris.data
    y = iris.target
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model, iris

model, iris = train_model()

# -----------------------------
# User Input
# -----------------------------
st.header("Enter Flower Measurements")

col1, col2 = st.columns(2)
with col1:
    sepal_length = st.number_input("Sepal Length (cm)", 4.0, 8.0, 5.1)
    sepal_width = st.number_input("Sepal Width (cm)", 2.0, 5.0, 3.5)
with col2:
    petal_length = st.number_input("Petal Length (cm)", 1.0, 7.0, 1.4)
    petal_width = st.number_input("Petal Width (cm)", 0.1, 3.0, 0.2)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("🔍 Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    predicted_class = iris.target_names[prediction][0]
    st.success(f"The predicted Iris species is: **{predicted_class.capitalize()}** 🌼")
