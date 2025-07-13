# codebasics ML course: codebasics.io, all rights reserverd

import streamlit as st
from prediction_helper import predict

# Initialize session state for reset functionality
if 'reset_key' not in st.session_state:
    st.session_state.reset_key = 0

# Define the page layout
st.title('🏥 Health Insurance Cost Predictor')
st.markdown("---")

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create four rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the grid with unique keys based on reset_key and proper default values
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=18,
                         help="Enter your current age (18-100 years)",
                         key=f'age_{st.session_state.reset_key}')
with row1[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20, value=0,
                                         key=f'dependants_{st.session_state.reset_key}')
with row1[2]:
    income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200, value=0,
                                 key=f'income_{st.session_state.reset_key}')

with row2[0]:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5, value=0,
                                   key=f'genetic_{st.session_state.reset_key}')
with row2[1]:
    # Bronze is index 0 in ['Bronze', 'Silver', 'Gold']
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'], index=0,
                                key=f'insurance_{st.session_state.reset_key}')
with row2[2]:
    # Salaried is index 0 in ['Salaried', 'Self-Employed', 'Freelancer', '']
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'], index=0,
                                   key=f'employment_{st.session_state.reset_key}')

with row3[0]:
    # Male is index 0 in ['Male', 'Female']
    gender = st.selectbox('Gender', categorical_options['Gender'], index=0,
                        key=f'gender_{st.session_state.reset_key}')
with row3[1]:
    # Unmarried is index 0 in ['Unmarried', 'Married']
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'], index=0,
                                key=f'marital_{st.session_state.reset_key}')
with row3[2]:
    # Normal is index 0 in ['Normal', 'Obesity', 'Overweight', 'Underweight']
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'], index=0,
                              key=f'bmi_{st.session_state.reset_key}')

with row4[0]:
    # No Smoking is index 0 in ['No Smoking', 'Regular', 'Occasional']
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'], index=0,
                                key=f'smoking_{st.session_state.reset_key}')
with row4[1]:
    # Northwest is index 0 in ['Northwest', 'Southeast', 'Northeast', 'Southwest']
    region = st.selectbox('Region', categorical_options['Region'], index=0,
                        key=f'region_{st.session_state.reset_key}')
with row4[2]:
    # No Disease is index 0 in the Medical History options
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'], index=0,
                                 key=f'medical_{st.session_state.reset_key}')

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Create columns for buttons with better spacing
button_cols = st.columns([1, 1, 2])

# Add predict button with a unique key
with button_cols[0]:
    if st.button('🔮 Predict', key='predict_button', use_container_width=True, type="primary"):
        # Basic validation
        if age < 18:
            st.error("Age must be at least 18 years.")
        elif income_lakhs < 0:
            st.error("Income cannot be negative.")
        else:
            with st.spinner('Calculating insurance cost...'):
                try:
                    prediction = predict(input_dict)
                    formatted_prediction = f"₹{prediction:,}"
                    st.success(f'Predicted Health Insurance Cost: {formatted_prediction}')
                except Exception as e:
                    st.error(f'Error during prediction: {str(e)}')

# Add reset button with a unique key - FIXED: using st.rerun() instead of st.experimental_rerun()
with button_cols[1]:
    if st.button('🔄 Reset All Fields', key='reset_button', use_container_width=True):
        st.session_state.reset_key += 1
        st.success("All fields have been reset to default values!")
        st.rerun()