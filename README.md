# 🏦 Credit Risk & Loan Default Analytics Dashboard

A full-stack, cloud-deployed credit risk data platform designed to assist banking institutions in predicting consumer loan defaults. This multi-page web platform combines an interactive executive control center with a real-time predictive underwriting engine driven by an optimized Random Forest machine learning pipeline.

🚀 **Live Interactive Application:** [https://loan-default-analytics-kbzh9gnaxgyswdhfjnsrda.streamlit.app/]
---

## 🎯 Business Problem & Project Goal

Commercial banking entities lose billions annually to non-performing loans (NPLs) and default rates. Mitigating this risk requires defensive analytics to identify systemic risk trends and early-stage algorithmic filters at the underwriting tier. 

This project delivers an end-to-end operational tool to solve two fundamental problems:
1. **Descriptive Analytics:** What underlying micro-segments and financial attributes (e.g., account leverage vs. salary) correlate highest with default occurrence?
2. **Predictive Analytics:** Can we programmatically flag high-risk applicants at the point of ingestion using applicant-submitted profiles?

---

## 📊 Core Insights & Key Findings

During the Exploratory Data Analysis (EDA) phase, several critical risk indicators were surfaced:
* **The Class Imbalance Challenge:** The operational dataset presents a heavy class imbalance, containing a **3.33% historical default rate** against a **96.67% clear repayment rate**. Models evaluated strictly on accuracy fail to detect risk, requiring optimized calibration.
* **Liquid Capital Over Leverage:** Analysis revealed that an applicant's **Bank Balance** is the single highest predictor of financial distress. The median balance of defaulting accounts sits significantly higher than that of healthy accounts.
* **The Income Paradox:** **Annual Salary** showed surprisingly minimal statistical divergence between defaulting and non-defaulting populations, indicating that behavioral cash spending management (liquid balance) outweighs raw income scale in assessing creditworthiness.

---

## 🛠️ Technical Stack & Frameworks

* **Environment Infrastructure:** Python (Virtual Environments)
* **Data Engineering & Analysis:** Pandas, NumPy
* **Statistical Visualization:** Plotly Express, Seaborn, Matplotlib
* **Machine Learning Pipeline:** Scikit-Learn (Random Forest Architecture)
* **Application Framework:** Streamlit Core (Multi-Page Component Engine)
* **Deployment & Version Control:** Git, GitHub, Streamlit Cloud Core

---

## 🏗️ Repository Architecture

The codebase is organized following standardized modular architecture principles:

```text
loan-default-analytics/
│
├── pages/                     # Sub-pages compiled by Streamlit's multi-page engine
│   ├── 1_Prediction_Engine.py # Dynamic machine learning underwriting form
│   └── 2_Data_Explorer.py     # Live multi-criteria data table search filter
│
├── src/
│   └── loan_model.pkl         # Saved serialized Random Forest classification pipeline
│
├── app.py                     # Main executive landing page and interactive Plotly dashboard
├── Default_Fin.csv            # Unified historical credit dataset
├── train_model.py             # Feature engineering, split balancing, and model generation script
├── requirements.txt           # Verified production library dependencies
└── .gitignore                 # Active version control structural filter
