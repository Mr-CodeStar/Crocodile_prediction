# 🐊 Crocodile Species Classification

This project predicts the species of a crocodile based on ecological and biometric traits using a robust machine learning pipeline. It combines modular preprocessing, diagnostic evaluation to ensure transparency and accuracy.

---

## 🚀 Project Overview

The goal is to classify crocodile species from 18 known classes using observed traits such as length, weight, age class, sex, conservation status, country, and habitat. The model is deployed via a Streamlit app that allows users to input traits and receive real-time predictions.

---

## 📊 Model Performance

- **Model**: Random Forest Classifier
- **Accuracy**: **95%** on the test set
- **Evaluation Metrics**:
  - Precision, Recall, F1-score per class
  - Confusion matrix
  - ROC and PR curves

---

## 🧠 Features Used

| Feature               | Type         | Sample Values                                                                 |
|----------------------|--------------|--------------------------------------------------------------------------------|
| Observed Length (m)  | Numeric      | 0.1 – 10.0                                                                     |
| Observed Weight (kg) | Numeric      | 0.1 – 1000.0                                                                   |
| BMI                  | Numeric      | Computed as weight / length²                                                  |
| Age Class            | Categorical  | Adult, Subadult, Juvenile, Hatchling                                          |
| Sex                  | Categorical  | Male, Female, Unknown                                                         |
| Conservation Status  | Categorical  | Least Concern, Vulnerable, Endangered, Critically Endangered, Data Deficient |
| Country_grouped      | Categorical  | 35+ countries including India, Cuba, Australia, Cameroon, etc.               |
| Habitat_grouped      | Categorical  | 15+ habitats including Rivers, Swamps, Lakes, Forest Rivers, Mangroves       |

---

## 🧰 Libraries Used

- **Pandas** – data manipulation
- **NumPy** – numerical operations
- **Scikit-learn** – preprocessing, modeling, evaluation
- **Matplotlib / Seaborn** – visualization
- **Streamlit** – interactive frontend
- **Joblib** – model persistence

---

## 🖼️ Image Folder

**This folder contains images of all crocodile species used in the project.**

---

## 🔗 Dataset Source

[Kaggle Dataset: Crocodile Species Traits and Labels](https://www.kaggle.com/datasets/zadafiyabhrami/global-crocodile-species-dataset)
