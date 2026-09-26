import mysql.connector
import pandas as pd
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="telecom_db"
)

df = pd.read_sql("SELECT tenure_months, monthly_bill, support_calls, churn FROM customers", conn)
conn.close()

print("=== 1. DATA LOADED FROM MYSQL ===")
print(df)

X = df[['tenure_months', 'monthly_bill', 'support_calls']]
y = df['churn']

model = LogisticRegression()
model.fit(X, y)

prediction = model.predict([[3, 80.0, 4]])
print("\n=== 2. MACHINE LEARNING PREDICTION ===")
print("New Customer (3 months, $80 bill, 4 calls) -> Will they leave? (1=Yes, 0=No):", prediction[0])
