# 🤰 Fetal Health Classification using Machine Learning

This project aims to predict the health status of a fetus (Normal, Suspect, or Pathological) using various fetal cardiotocographic (CTG) features. By leveraging machine learning models, this application provides an intelligent, data-driven approach to assist obstetricians in monitoring fetal well-being.

---

## 🚀 Demo

You can launch the interactive Streamlit app here *(update with your deployed link if hosted on Streamlit Cloud or Hugging Face)*.

---

## 📊 Problem Statement

Accurate and early prediction of fetal health status is critical for reducing infant mortality and ensuring timely medical interventions. Traditional analysis of CTG data can be subjective and error-prone. This project automates the analysis using supervised machine learning models to classify fetal health into:

- `Class 1`: Normal  
- `Class 2`: Suspect  
- `Class 3`: Pathological  

---

## 📁 Dataset

The dataset is publicly available from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/fetal+health).  
It contains **21 features** extracted from fetal cardiotocograms, and a `fetal_health` target column with three classes.

---

## 🔧 Features Used

Some of the features used for prediction include:

- `baseline value`, `accelerations`, `fetal_movement`, `uterine_contractions`
- `prolongued_decelerations`, `severe_decelerations`, `abnormal_short_term_variability`
- `histogram_min`, `histogram_max`, `histogram_number_of_zeroes`
- `histogram_tendency`, and others

---

## 🛠️ Tech Stack

- **Language**: Python  
- **Frontend**: Streamlit  
- **Models**: XGBoost, Random Forest (final selected models)  
- **Libraries**: `scikit-learn`, `xgboost`, `pandas`, `numpy`, `matplotlib`, `pickle`  
- **Data Preprocessing**: StandardScaler, Label Encoding

---

## 🧠 Model Training Summary

Two models were selected based on their high performance on test data:

| Model            | Accuracy | F1 Score | Recall | Precision |
|------------------|----------|----------|--------|-----------|
| **XGBoost**      | 94.67%   | 0.9463   | 0.9467 | 0.9463    |
| **Random Forest**| 93.10%   | 0.9290   | 0.9310 | 0.9292    |

Both models were trained using class-balanced weights to handle imbalanced data.

---

## 🖥️ Running the App Locally

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/fetal-health-classifier.git
cd fetal-health-classifier
```

2. **Install the Dependencies**

```bash
pip install -r requirements.txt
```

3. **Launch the Streamlit app**

```bash
streamlit run app.py
```

---

## 🔍 App Preview

Below is a screenshot of the Fetal Health Prediction Streamlit web app:

![Streamlit App Screenshot](https://github.com/sudharshanpaul/Fetal-Health-Predictor/blob/main/images/Screenshot%202025-06-18%20095838.png)

![Streamlit App Screenshot](https://github.com/sudharshanpaul/Fetal-Health-Predictor/blob/main/images/Screenshot%202025-06-18%20095854.png)

---

## 🤝 Contributions
Feel free to fork this repository and contribute. Open a pull request for suggestions, bug fixes, or improvements!

---

## 🙏 Acknowledgments
- UCI Machine Learning Repository for the Fetal Health Dataset

- Streamlit for the rapid prototyping tool

- Scikit-learn and XGBoost for powerful modeling frameworks

---

## ✉️ Contact
For any queries or collaborations, reach out via [LinkedIn](https://www.linkedin.com/in/sudharshan-paul/) or email: gantasudarshanpaul@gmail.com
