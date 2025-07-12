# 🏥 Health Insurance Cost Predictor

This Streamlit-based web application predicts the cost of health insurance for individuals based on multiple factors like age, BMI, income, smoking habits, medical history, and more.

## 🔍 Features

- 📊 Predicts insurance cost using trained machine learning models
- 🧠 Considers demographics, medical risk, lifestyle, and plan type
- 👤 Separate models used for age groups (<=25 and >25)
- 🚀 Simple and interactive web interface built with Streamlit

## 🧩 Input Parameters

- Age (18-100)
- Number of Dependants (0-20)
- Income in Lakhs (0-200)
- Genetical Risk (0-5)
- Insurance Plan (Bronze/Silver/Gold)
- Employment Status (Salaried/Self-Employed/Freelancer)
- Gender (Male/Female)
- Marital Status (Married/Unmarried)
- BMI Category (Normal/Obesity/Overweight/Underweight)
- Smoking Status (No Smoking/Regular/Occasional)
- Region (Northwest/Southeast/Northeast/Southwest)
- Medical History (Various combinations of health conditions)

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone <repository-url>
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
- joblib

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

See the LICENSE file for details.

Key improvements made:
1. Corrected the run command from `app.py` to `main.py`
2. Added joblib to the libraries list
3. Added value ranges for numeric inputs
4. Improved project structure documentation with descriptions
5. Reorganized the attribution section
6. Removed incomplete requirements.txt section
7. Added more detailed descriptions for model files