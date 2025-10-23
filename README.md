# 🌸 Iris Flower Classification using Machine Learning

## 📘 Overview
This project is an **interactive machine learning web app** that predicts the species of an Iris flower — *Setosa*, *Versicolor*, or *Virginica* — based on its sepal and petal measurements.  
It demonstrates the **end-to-end ML workflow**: data preprocessing → model training → evaluation → deployment with Streamlit.

---

## 🧠 Machine Learning Algorithm Used
The notebook uses the **K-Nearest Neighbors (KNN)** algorithm for classification.

### 🔹 Algorithm Details
- **Algorithm Name:** K-Nearest Neighbors (KNN)
- **Library:** `sklearn.neighbors.KNeighborsClassifier`
- **Working Principle:**  
  The model predicts the class of a new sample based on the *majority vote* of its *k nearest neighbors* in the training data.
- **Advantages:**
  - Simple and effective for small datasets
  - No training time (lazy learner)
  - Performs well on the Iris dataset
- **Performance:** ~97–99% accuracy on test data

---
