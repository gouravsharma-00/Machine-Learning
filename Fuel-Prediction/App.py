import streamlit as st
import joblib
import pandas as pd
import numpy as np 

# Load the model 
model = joblib.load('./public/linear_regression_model.pkl')

# App Title 
st.title('Aircraft Fuel Consumption Predictor')

# Input Field
flight_Distance = st.number_input('distance (km)')
number_of_passanger = st.number_input('Number of Passanger')
flight_Duration = st.number_input('Flight_Duration (hours)')
aircraft_type = st.selectbox('Aircraft_Type', ['Type1','Type2','Type3'])

#DataFrame 
input_data = pd.DataFrame({
    'Flight_Distance': [flight_Distance],
    'Number_of_Passengers': [number_of_passanger],
    'Flight_Duration': [flight_Duration],
    'Aircraft_Type_Type1': [1 if aircraft_type == 'Type1' else 0],
    'Aircraft_Type_Type2': [1 if aircraft_type == 'Type2' else 0],
    'Aircraft_Type_Type3': [1 if aircraft_type == 'Type3' else 0]
})

# Prediction
if st.button('predict'):
   Fuel_Consumption = model.predict(input_data)
   st.write(Fuel_Consumption)
