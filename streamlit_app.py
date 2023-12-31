import streamlit as st
import pandas as pd
#import joblib

# Load the pre-trained Random Forest model
#model = joblib.load('your_random_forest_model.pkl')

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        font-size: 24px;
        text-align: center;
    }
    .input {
        width: 300px;
        padding: 10px;
        margin: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a Streamlit UI
st.title('Credit Card Fraud Detection')
st.markdown('### This model predicts whether a credit card transaction is fraudulent or not')

# Input form with improved styling
cc_num = st.number_input('Enter Credit card Number', min_value=0.0, max_value=9999999999999999990.0, format='%f', key='cc_num')
amt = st.number_input('Enter Enter transaction amount', min_value=0.0, max_value=100000000.0, format='%f', key='amt')
street = st.number_input('Enter Enter Street', min_value=0.0, max_value=10.0, format='%f', key='street')
city = st.number_input('Enter Enter City', min_value=0.0, max_value=10.0, format='%f', key='city')

if st.button('Predict'):
    input_data = pd.DataFrame({
        'Enter Credit card Number': [cc_num],
        'Enter Enter transaction amount': [amt],
        'Enter Enter Street': [street],
        'Enter Enter City': [city]
    })

    #prediction = model.predict(input_data)
    #prediction_prob = model.predict_proba(input_data)

    st.markdown('### Prediction Results:')
    fraud_map = {0: 'Not Fraud', 1: 'Fraud'}
    st.markdown(f'**Predicted Fraud:**')
    st.markdown(f'**Class Probabilities:**')
    #st.write(pd.DataFrame({'Fraud or Not': ))

# Input for batch prediction using CSV file
st.markdown('## Batch Prediction (CSV Upload)')
uploaded_file = st.file_uploader("Upload a CSV file for batch prediction", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    batch_data = pd.read_csv(uploaded_file)

    if st.button('Perform Batch Prediction'):
        # Perform batch prediction on the uploaded data
        #batch_predictions = model.predict(batch_data)
        #batch_data['Predicted Species'] = batch_predictions

        st.markdown('### Batch Prediction Results:')
        st.write(batch_data)



