# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 18:04:44 2024

@author: ELCOT
"""

import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

def rating_prediction():
    # Load your trained model 
    loaded_model = load('titanic_trained_model.joblib')

    # Creating function for prediction
    def movie_rating_prediction(input_data):
        input_data_np_array = np.asarray(input_data, dtype=float)
        input_data_reshaped = input_data_np_array.reshape(1, -1)
        column_names = ['Year', 'Duration', 'Votes', 'Weighted_Rating']

        input_data_reshaped_df = pd.DataFrame(input_data_reshaped, columns=column_names)
        prediction = loaded_model.predict(input_data_reshaped_df)
        st.success(f"The predicted movie rating is: {prediction}")

    st.title('Movie Rating Prediction Form')
    st.write("Enter the Movie Details: ")
    
    # Convert inputs to appropriate numerical types
    Year = st.text_input("Movie Release Year", type='number')
    Duration = st.text_input("Movie Duration (in minutes)", type='number')
    Votes = st.text_input("Number of Votes", type='number')
    Weighted_Rating = st.text_input("Weighted Rating", type='number')

    if st.button('Predict Movie Rating'):
        movie_rating_prediction([Year, Duration, Votes, Weighted_Rating])
