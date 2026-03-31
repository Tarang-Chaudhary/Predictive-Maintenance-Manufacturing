# 🔧 Predictive Maintenance in Manufacturing

A Machine Learning project focused on predicting equipment failures and Remaining Useful Life (RUL) using the NASA CMAPSS FD001 dataset.

---

## 📌 Overview

Predictive Maintenance is a data-driven approach used to predict machine failures before they occur. This project uses machine learning techniques to analyze sensor data and estimate the health of industrial equipment.

The goal is to:
- Reduce downtime
- Improve efficiency
- Enable proactive maintenance

---

## 🎯 Problem Statement

Industrial machines generate large amounts of sensor data. The challenge is to use this data to:

- Predict when a machine will fail
- Estimate Remaining Useful Life (RUL)
- Help industries schedule maintenance efficiently

---

## 📊 Dataset

- **Source:** NASA CMAPSS FD001 Dataset  
- **Type:** Time-series sensor data  
- **Features include:**
  - Engine ID
  - Cycle number
  - Operational settings
  - Sensor measurements

- **Target:**
  - Remaining Useful Life (RUL)

---

## ⚙️ Project Workflow

1. **Data Preprocessing**
   - Handling missing values
   - Normalization/Scaling
   - Feature selection

2. **Exploratory Data Analysis (EDA)**
   - Trend analysis of sensors
   - Correlation analysis

3. **Feature Engineering**
   - Window-based features
   - Degradation patterns

4. **Model Building**
   - Regression / Deep Learning models (e.g., CNN/LSTM if used)
   - Training on historical data

5. **Evaluation**
   - RMSE
   - MAE
   - R² Score

6. **Prediction**
   - Estimation of Remaining Useful Life

---

## 🧠 Models Used

- Linear Regression
- Random Forest
- XGBoost (if used)
- Deep Learning Models (CNN / LSTM) *(optional based on your implementation)*

---

## 📈 Results

- Achieved accurate prediction of machine degradation
- Improved early failure detection capability
- Model performance evaluated using standard regression metrics

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:**
  - NumPy
  - Pandas
  - Matplotlib / Seaborn
  - Scikit-learn
  - TensorFlow / PyTorch (if used)

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/Tarang-Chaudhary/Predictive-Maintenance-Manufacturing.git
cd Predictive-Maintenance-Manufacturing
