CREATE DATABASE IF NOT EXISTS telecom_db;
USE telecom_db;

CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tenure_months INT,
    monthly_bill FLOAT,
    support_calls INT,
    churn INT
);

INSERT INTO customers (tenure_months, monthly_bill, support_calls, churn) VALUES
(2, 85.5, 5, 1), (24, 45.0, 1, 0), (1, 90.0, 6, 1), (36, 50.0, 0, 0),
(3, 78.0, 4, 1), (18, 55.0, 1, 0), (5, 82.0, 5, 1), (48, 40.0, 0, 0);
