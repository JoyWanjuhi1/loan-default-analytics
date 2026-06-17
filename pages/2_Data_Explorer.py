import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Data Explorer", layout="wide")

st.title("📋 Portfolio Raw Data Explorer")
st.markdown("Search, filter, and drill down into specific tranches of customer profiles.")

# 👈 CHANGED: Swapped absolute path for the clean relative path
DATA_PATH = "Default_Fin.csv"

if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH).drop(columns=['Index'], errors='ignore')
    
    # Adding interactive sidebar widgets to filter the main interactive table
    st.sidebar.subheader("Filter Portfolio View")
    status_filter = st.sidebar.multiselect("Filter by Default Status", options=[0, 1], default=[0, 1], format_func=lambda x: "Defaulted" if x==1 else "Paid Off")
    balance_filter = st.sidebar.slider("Minimum Bank Balance", int(df['Bank Balance'].min()), int(df['Bank Balance'].max()), int(df['Bank Balance'].min()))
    
    # Apply filters dynamically
    filtered_df = df[(df['Defaulted?'].isin(status_filter)) & (df['Bank Balance'] >= balance_filter)]
    
    st.metric("Records Matching Filter Criteria", f"{len(filtered_df):,}")
    st.dataframe(filtered_df, use_container_width=True)
else:
    st.error("Data source missing.")