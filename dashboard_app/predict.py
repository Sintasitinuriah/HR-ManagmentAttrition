import streamlit as st
import pandas as pd
import joblib

# Load model dan scaler
model = joblib.load('model_best.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Prediksi Karyawan Keluar")

# Input dari user
job_involvement = st.slider("Job Involvement (1-4)", 1, 4, 2)
travel_freq = st.selectbox("Frekuensi Perjalanan Bisnis", ["Tidak Pernah", "Sering"])
job_role = st.selectbox("Job Role", [
    "Lainnya", "Laboratory Technician", "Manager", 
    "Manufacturing Director", "Research Director", 
    "Sales Representative"
])
marital_status = st.selectbox("Status Pernikahan", ["Single", "Married", "Divorced"])
overtime = st.selectbox("Lembur", ["Yes", "No"])

# Proses input ke format model
data = {
    'JobInvolvement': job_involvement,
    'BusinessTravel_Travel_Frequently': 1 if travel_freq == "Sering" else 0,
    'JobRole_Laboratory Technician': 1 if job_role == "Laboratory Technician" else 0,
    'JobRole_Manager': 1 if job_role == "Manager" else 0,
    'JobRole_Manufacturing Director': 1 if job_role == "Manufacturing Director" else 0,
    'JobRole_Research Director': 1 if job_role == "Research Director" else 0,
    'JobRole_Sales Representative': 1 if job_role == "Sales Representative" else 0,
    'MaritalStatus_Single': 1 if marital_status == "Single" else 0,
    'OverTime_Yes': 1 if overtime == "Yes" else 0
}

input_df = pd.DataFrame([data])

# Standarisasi input
input_scaled = scaler.transform(input_df)

# Prediksi
if st.button("Prediksi"):
    prediction = model.predict(input_scaled)[0]
    st.success(f"Hasil Prediksi: {'Keluar' if prediction == 1 else 'Tidak Keluar'}")
