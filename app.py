import streamlit as st
import mysql.connector
import pandas as pd
from sklearn.linear_model import LogisticRegression

st.title("📊 Customer Churn Prediction (SQL + ML)")

# 1. Load Data from MySQL (with fallback table for live demo)
try:
    conn = mysql.connector.connect(
        host="localhost", user="root", password="YOUR_MYSQL_PASSWORD", database="telecom_db"
    )
    df = pd.read_sql("SELECT tenure_months, monthly_bill, support_calls, churn FROM customers", conn)
    conn.close()
except Exception:
    df = pd.DataFrame({
        'tenure_months': [2, 24, 1, 36, 3, 18, 5, 48],
        'monthly_bill': [85.5, 45.0, 90.0, 50.0, 78.0, 55.0, 82.0, 40.0],
        'support_calls': [5, 1, 6, 0, 4, 1, 5, 0],
        'churn': [1, 0, 1, 0, 1, 0, 1, 0]
    })

st.subheader("1. Live Database Records (MySQL)")
st.dataframe(df)

# 2. Train Machine Learning Model
X = df[['tenure_months', 'monthly_bill', 'support_calls']]
y = df['churn']
model = LogisticRegression().fit(X, y)

# 3. Interactive Prediction Sliders
st.subheader("2. Test a New Customer")
tenure = st.slider("Tenure (Months)", 1, 60, 3)
bill = st.number_input("Monthly Bill ($)", 10.0, 150.0, 80.0)
calls = st.slider("Support Calls", 0, 10, 4)

if st.button("Predict Churn"):
    pred = model.predict([[tenure, bill, calls]])[0]
    if pred == 1:
        st.error("⚠️ Prediction: Customer WILL Leave (Churn = 1)")
    else:
        st.success("✅ Prediction: Customer Will Stay (Churn = 0)")
