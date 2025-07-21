# SmartPayPro
# SmartPayPro – AI-Powered Salary & Job Level Prediction System

## End-to-End Machine Learning Project  
Project by: Suryansh Chawla  
Tech Stack:Python, Scikit-Learn, XGBoost, Streamlit, FPDF, Git

---

## Live Application  
Access the deployed project here:  
[SmartPayPro – Live on Streamlit](https://smartpaypro-pukfvbdfd9y3buw5k2pbtj.streamlit.app/)


---

##  Project Overview

SmartPayPro is a real-time web-based ML application that predicts:
- Expected Salary based on job title, education, experience, and skills
- Job Level Classification (Junior / Mid / Senior)
- Provides a personalized salary insight report as downloadable PDF

Developed to solve the problem of compensation estimation for job applicants and HR teams, this project demonstrates a full ML pipeline: **data preparation → model building → deployment → reporting.

---

##  Problem Statement

In today's fast-evolving job market, employees and hiring teams struggle to assess:
- Whether a candidate is underpaid or overpaid
- What job level matches their profile
- How to transparently present compensation decisions

This leads to:
- Pay inequality
- Mismatched expectations
- Inefficient hiring and internal promotions

SmartPayPro addresses this by using historical salary data and AI models to provide accurate, unbiased compensation benchmarks and job level predictions.

---

## Solution Overview

| Component           | Description                                                                          |
|---------------------|--------------------------------------------------------------------------------------|
| Input Parameters    | Gender, Education Level, Job Title, Years of Experience, Skill Score                 |
| Salary Prediction   | ML regression model (XGBoost) estimates fair market salary                           |
| Job Level Prediction| ML classification model (Random Forest) assigns job level (Junior, Mid, Senior)      |
| Reports             | Instant downloadable PDF report with predictions and guidance                        |
| UI/UX               | Clean Streamlit interface with dropdowns, sliders, and smart alerts                  |

---

## Tools & Technologies

| Layer            | Stack Used                                              |
|------------------|---------------------------------------------------------
| Frontend         | Streamlit                                                  |
| ML Models        | XGBoost Regressor, RandomForestClassifier                  |
| Preprocessing    | Scikit-Learn Pipelines, OneHotEncoder, StandardScaler      |
| Deployment       | Streamlit Cloud                                            |
| Reports          | FPDF (for generating dynamic PDF reports)                  |
| Versioning       | Git & GitHub                                               |

---

## Project Structure
smartpaypro/
│
├── models/
│ ├── salary_model.pkl # Trained salary prediction pipeline
│ └── level_classifier.pkl # Trained job level classifier pipeline
│
├── outputs/
│ └── prediction_report.pdf # Auto-generated PDF report
│
├── smartpaypro_app.py # Main Streamlit application script
├── requirements.txt # Project dependencies
├── README.md # This documentation



---

##  How to Run This Project Locally

### Clone the Repository
```bash
git clone https://github.com/Sury690/smartpaypro.git
cd smartpaypro

### Install Dependencies
pip install -r requirements.txt

##Launch the Application:

streamlit run smartpaypro_app.py

###Model Details
Salary Prediction:

Algorithm: XGBoostRegressor

Pipeline includes: OneHotEncoding (categorical) + StandardScaler (numeric)

Trained on 5 core features with handle_unknown='ignore' for deployment stability

Job Level Classifier:

Algorithm: RandomForestClassifier

Uses same preprocessor pipeline for consistency

Training Features:

Categorical: Gender, Education, Job Title

Numerical: Experience, Skill Score

Model Details
Salary Prediction:

Algorithm: XGBoostRegressor

Pipeline includes: OneHotEncoding (categorical) + StandardScaler (numeric)

Trained on 5 core features with handle_unknown='ignore' for deployment stability

Job Level Classifier:

Algorithm: RandomForestClassifier

Uses same preprocessor pipeline for consistency

Training Features:

Categorical: Gender, Education, Job Title

Numerical: Experience, Skill Score.


###Output Example
Input:
Gender: Female

Education: Master’s Degree

Job Title: Data Analyst

Experience: 4 years

Skill Score: 8/10

Output:
Estimated Salary: ₹7,25,000

Job Level: Mid-Level

 Downloadable Report: prediction_report.pdf.

###Future Scope
📄 Resume parser to auto-fill input

🌐 LinkedIn/Glassdoor API integration

🧠 SHAP/LIME-based explainability dashboard

🛡️ Bias detection and mitigation in salary models

📊 Admin dashboard for HR analytics.


###References
XGBoost Documentation

Scikit-learn Pipeline Guide

Streamlit Docs

FPDF for Python

Dataset: Cleaned internal dataset used during academic training.


Author
Suryansh Chawla









