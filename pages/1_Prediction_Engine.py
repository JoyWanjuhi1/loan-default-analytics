import streamlit as st
import pandas as pd
import pickle
import os

st.set_page_config(page_title="Risk Prediction Engine", layout="wide")

st.title("🔮 Real-Time Loan Underwriting & Risk Prediction")
st.markdown("Input an applicant's financial attributes below to evaluate their statistical probability of defaulting on a loan installment.")

MODEL_PATH = "src/loan_model.pkl"

@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as f:
            return pickle.load(f)
    return None

model = load_model()

if model is not None:
    # Creating layout grids for inputs
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("👤 Applicant Profile")
        employed_input = st.selectbox("Current Employment Status", options=["Employed", "Unemployed"])
        annual_salary = st.slider("Verified Annual Salary ($)", min_value=10000, max_value=1000000, value=150000, step=5000)
        
    with col2:
        st.subheader("💳 Financial Leverage")
        bank_balance = st.slider("Current Liquid Bank Balance ($)", min_value=0, max_value=40000, value=5000, step=250)

    # Encoding
    employed_encoded = 1 if employed_input == "Employed" else 0
    
    st.markdown("---")
    
    # Large Action Button
    if st.button("⚡ Run Risk Assessment Model", use_container_width=True):
        input_data = pd.DataFrame([[employed_encoded, bank_balance, annual_salary]], 
                                  columns=['Employed', 'Bank Balance', 'Annual Salary'])
        
        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0][1]
        
        # Displaying results dynamically with beautiful alerts
        if prediction == 1:
            st.error(f"### ❌ Loan Application Rejected\n\n**Risk Level:** CRITICAL\n\nThis applicant exhibits a **{prediction_proba:.1%}** probability of default based on historical variance profiles.")
        else:
            st.success(f"### ✅ Loan Application Approved\n\n**Risk Level:** LOW\n\nThis applicant exhibits a **{prediction_proba:.1%}** probability of default. Safe to proceed with standard credit terms.")
else:
    st.error("Machine Learning pipeline file not found at `src/loan_model.pkl`.")