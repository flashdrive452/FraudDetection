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
st.title('Random Forest Classifier')
st.markdown('## Predict Fraud or Not')

# Input form with improved styling
sepal_length = st.number_input('Enter Sepal Length', min_value=0.0, max_value=10.0, format='%f', key='sepal_length')
sepal_width = st.number_input('Enter Sepal Width', min_value=0.0, max_value=10.0, format='%f', key='sepal_width')
petal_length = st.number_input('Enter Petal Length', min_value=0.0, max_value=10.0, format='%f', key='petal_length')
petal_width = st.number_input('Enter Petal Width', min_value=0.0, max_value=10.0, format='%f', key='petal_width')

if st.button('Predict'):
    input_data = pd.DataFrame({
        'sepal_length': [sepal_length],
        'sepal_width': [sepal_width],
        'petal_length': [petal_length],
        'petal_width': [petal_width]
    })

    #prediction = model.predict(input_data)
    #prediction_prob = model.predict_proba(input_data)

    st.markdown('### Prediction Results:')
    fraud_map = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
    st.markdown(f'**Predicted Fraud:**')
    st.markdown(f'**Class Probabilities:**')
    #st.write(pd.DataFrame({'Fraud or Not': ))

