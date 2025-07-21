
import streamlit as st
import pandas as pd
import joblib
from fpdf import FPDF
import os

# Load trained models
model = joblib.load("models/salary_model.pkl")
clf_model = joblib.load("models/level_classifier.pkl")

# Page config
st.set_page_config(page_title="SmartPayPro", layout="wide")
st.title("🧠 SmartPayPro - Predict Your Salary & Job Level")

# User input
col1, col2 = st.columns(2)
with col1:
    experience = st.slider("Years of Experience", 0, 40, 5)
    gender = st.selectbox("Gender", ["Male", "Female"])
    edu = st.selectbox("Education", ["Bachelor's", "Master's", "PhD"])

with col2:
    job = st.selectbox("Job Title", ['Data Analyst', 'Software Engineer', 'Manager', 'Director', 'Clerk'])
    skill_score = st.slider("Skill Score (1-10)", 1, 10, 5)

# Input DataFrame
input_df = pd.DataFrame({
    "Gender": [gender],
    "Education": [edu],
    "Job Title": [job],
    "Experience": [experience],
    "Skill_Score": [skill_score]
})


# Predict and Generate Report
if st.button("Predict Now"):

    # Ensure correct column order
    input_df = input_df[["Gender", "Education", "Job Title", "Experience", "Skill_Score"]]

    # Debug: Show input shape
    st.write("🧪 Input DataFrame:")
    st.write(input_df)
    st.write("Shape:", input_df.shape)
    st.write("Columns:", input_df.columns.tolist())

    try:
        salary = model.predict(input_df)[0]
        level = clf_model.predict(input_df)[0]

        # Display Results
        st.success(f"💰 Estimated Salary: Rs. {int(salary):,}")
        st.info(f"📈 Predicted Job Level: {level}")

        if level == 'Junior' and salary < 600000:
            st.warning("⚠️ You might be underpaid compared to your peer average. Consider negotiation or upskilling.")

        # ✅ PDF Report Generation
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="SmartPayPro Salary Prediction Report", ln=True, align='C')
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Predicted Salary: Rs. {int(salary):,}", ln=True)
        pdf.cell(200, 10, txt=f"Predicted Job Level: {level}", ln=True)
        pdf.cell(200, 10, txt=f"Experience: {experience} years", ln=True)
        pdf.cell(200, 10, txt=f"Skill Score: {skill_score}/10", ln=True)

        os.makedirs("outputs", exist_ok=True)
        pdf_path = "outputs/prediction_report.pdf"
        pdf.output(pdf_path)
        # Download Button
        with open(pdf_path, "rb") as f:
            st.download_button("📄 Download PDF Report", f, file_name="SmartPayPro_Report.pdf")
    except Exception as e:
        st.error(f"❌ Prediction Error: {e}")

    

    
    





    
