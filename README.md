# 🏥 Health Insurance Cost Predictor

This Streamlit-based web application predicts the cost of health insurance for individuals based on multiple factors like age, BMI, income, smoking habits, medical history, and more.

## 🔍 Features

- 📊 Predicts insurance cost using trained machine learning models
- 🧠 Considers demographics, medical risk, lifestyle, and plan type
- 👤 Separate models used for age groups (<=25 and >25)
- 🚀 Simple and interactive web interface built with Streamlit

## 🧩 Input Parameters

- Age
- Number of Dependants
- Income in Lakhs
- Genetical Risk (numeric)
- Insurance Plan (Bronze/Silver/Gold)
- Employment Status
- Gender
- Marital Status
- BMI Category
- Smoking Status
- Region
- Medical History

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/himanshunagi/health-insurance-cost-predictor.git
cd health-insurance-cost-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

## 📚 Libraries Used

- pandas
- numpy
- scikit-learn
- streamlit
- pickle

## 📁 Project Structure
.
├── main.py                    # Streamlit web interface
├── prediction_helper.py       # Preprocessing and prediction logic
├── artifacts/                 # Trained model files (not included)
│   ├── model_young.joblib
│   ├── model_rest.joblib
│   ├── scaler_young.joblib
│   └── scaler_rest.joblib
├── requirements.txt           # Python dependencies
└── README.md


## 🤝 Contributing

This project is part of the Codebasics ML Course — codebasics.io


## 📝 License
---

### 📦 `requirements.txt`

