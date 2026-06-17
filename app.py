import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Credit Risk Analytics", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for a premium dark/modern feel
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .metric-box { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

# 👈 CHANGED: This path is now relative so it works perfectly locally AND on Streamlit Cloud!
DATA_PATH = "Default_Fin.csv"

@st.cache_data
def load_data():
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        df['Employment_Status'] = df['Employed'].map({1: 'Employed', 0: 'Unemployed'})
        df['Default_Label'] = df['Defaulted?'].map({1: 'Defaulted', 0: 'Paid Off'})
        return df
    return None

df = load_data()

st.title("🏦 Credit Risk & Loan Default Analytics")
st.markdown("Welcome to the executive credit risk control center. Use the sidebar to navigate between analytics and the predictive engine.")

if df is not None:
    # --- KPI METRICS ---
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Portfolio Customers", value=f"{len(df):,}")
    with col2:
        st.metric(label="Portfolio Default Rate", value=f"{df['Defaulted?'].mean():.2%}")
    with col3:
        st.metric(label="Avg Outstanding Balance", value=f"${df['Bank Balance'].mean():,.2f}")
    with col4:
        st.metric(label="Avg Annual Salary", value=f"${df['Annual Salary'].mean():,.2f}")

    st.markdown("---")
    
    # --- INTERACTIVE CHARTS ---
    st.subheader("📊 Risk Factor Deep-Dive")
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Interactive Boxplot using Plotly
        fig_box = px.box(df, x="Default_Label", y="Bank Balance", color="Default_Label",
                         title="Impact of Bank Balance on Default Risk",
                         labels={"Default_Label": "Status", "Bank Balance": "Account Balance ($)"},
                         color_discrete_map={"Paid Off": "#2ecc71", "Defaulted": "#e74c3c"})
        st.plotly_chart(fig_box, use_container_width=True)
        
    with chart_col2:
        # Interactive Histogram for Income Distribution
        fig_hist = px.histogram(df, x="Annual Salary", color="Default_Label", marginal="box",
                                title="Annual Income Distribution & Default Spread",
                                barmode="overlay",
                                color_discrete_map={"Paid Off": "#2ecc71", "Defaulted": "#e74c3c"})
        st.plotly_chart(fig_hist, use_container_width=True)
else:
    st.error("Dataset not found. Please verify the file path.")