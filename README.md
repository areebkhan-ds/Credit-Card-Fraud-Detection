# Credit Card Fraud Detection

## Overview
Credit card fraud is a significant problem for financial institutions, resulting in financial loss and reputational damage. This project implements a **Machine Learning model to detect fraudulent credit card transactions in real-time**, using a highly imbalanced dataset.

The model identifies potentially fraudulent transactions automatically, helping companies reduce losses and protect their customers.

---

## Dataset
- Source: [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/code/youssefelbadry10/credit-card-fraud-detection/input)
- Size: 284,807 transactions
- Features: 23 columns including:
---

## Features & Preprocessing
- Converted time-related columns to datetime (for potential feature engineering)
- Scaled `Amount` column using StandardScaler
- Encoded categorical features (if any) using LabelEncoder
- Handled class imbalance using:
  - `class_weight='balanced'` in Random Forest
  - Optional: SMOTE for oversampling minority class

---

## Model
- Algorithm: **Random Forest Classifier**
- Parameters:
  - `n_estimators=100`
  - `class_weight='balanced'`
- Metrics:
  - **Precision (Fraud)**: 0.92
  - **Recall (Fraud)**: 0.59
  - **F1-score (Fraud)**: 0.72
  - **ROC-AUC**: 0.98

The model strikes a balance between **high precision** (few false alarms) and **good recall** (detecting most frauds).

---

## Benefits to the Company
- **Reduce financial losses**: Detects fraud before approval  
- **Protect customers**: Prevents fraudulent transactions  
- **Operational efficiency**: Reduces manual review workload  
- **Proactive risk management**: Improves over time as model retrains  

---

## Usage
1. Clone this repository:
```bash
git clone https://github.com/areebkhan-ds/credit-card-fraud-detection.git

---

## Author

Areeb Khan
