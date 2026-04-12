# 💳 Credit Card Fraud Detection using Machine Learning

## 📌 Overview

This project focuses on detecting fraudulent credit card transactions using Machine Learning techniques. Due to the highly imbalanced nature of the dataset, special attention is given to handling class imbalance and evaluating models using appropriate metrics.

The project explores multiple models and data balancing techniques to identify the most effective approach for fraud detection.

---

## 🎯 Objectives

* Detect fraudulent transactions accurately
* Handle imbalanced dataset effectively
* Compare multiple machine learning models
* Optimize performance using proper evaluation metrics

---

## 📊 Dataset

* Transactions made by European cardholders (September 2013)
* Total transactions: **284,807**
* Fraud cases: **492 (~0.17%)**
* Features:

  * `V1–V28` (PCA transformed features)
  * `Time` (seconds from first transaction)
  * `Amount` (transaction value)
  * `Class` (0 = Genuine, 1 = Fraud)

---

## ⚙️ Technologies Used

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Imbalanced-learn (SMOTE)
* Streamlit (for deployment)

---

## 🧠 Machine Learning Approach

### 🔹 Data Preprocessing

* Train-Test Split (Stratified)
* Feature Scaling (Time & Amount)
* Handling Imbalance:

  * Undersampling
  * Oversampling
  * SMOTE

---

### 🔹 Models Used

* Logistic Regression
* Decision Tree
* Random Forest

---

### 🔹 Evaluation Metrics

* Precision
* Recall
* F1-score
* Confusion Matrix

> Accuracy is not used due to class imbalance.

---

## 📈 Results Summary

| Model               | Technique    | Precision | Recall   | F1 Score |
| ------------------- | ------------ | --------- | -------- | -------- |
| Logistic Regression | Oversampling | 0.06      | 0.92     | 0.12     |
| Decision Tree       | Oversampling | 0.71      | 0.71     | 0.71     |
| Random Forest       | Oversampling | 0.96      | 0.77     | 0.85     |
| **Random Forest**   | **SMOTE**    | **0.85**  | **0.83** | **0.84** |

---

## 🏆 Best Model

**Random Forest with SMOTE** provided the best balance between precision and recall.

---

## 🚀 Deployment

A simple web application was built using **Streamlit** to demonstrate real-time fraud detection.

### Features:

* User input for transaction details
* Real-time prediction
* Fraud probability display

---

## ⚠️ Note

Due to anonymized PCA features (V1–V28), real user input is simulated during deployment.

---

## 📂 Project Structure

```
├── app.py
├── model.pkl
├── scaler.pkl
├── notebook.ipynb
├── README.md
```

---

## 🎥 Demo

[👉 Add your demo video link here]

---

## 🌍 SDG Contribution

Aligned with **SDG 8: Decent Work and Economic Growth**
This project helps reduce financial fraud, improving trust and stability in digital financial systems.

---

## 📚 Key Learnings

* Handling imbalanced datasets
* Importance of Precision vs Recall
* Model comparison and evaluation
* Real-world ML deployment

---

## 👨‍💻 Author

**Rahul Kumar**
B.Tech IT | Data Science Enthusiast

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
