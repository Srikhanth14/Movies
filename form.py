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
    loaded_model = load('movies_trained_model.joblib')

    # Creating function for prediction
    def movie_rating_prediction(input_data):
        try:
            input_data_np_array = np.asarray(input_data, dtype=float)
            input_data_reshaped = input_data_np_array.reshape(1, -1)
            column_names = ['Year', 'Duration', 'Votes', 'Weighted_Rating']

            input_data_reshaped_df = pd.DataFrame(input_data_reshaped, columns=column_names)
            prediction = loaded_model.predict(input_data_reshaped_df)
            st.success(f"The predicted movie rating is: {prediction[0]:.2f}")
        except Exception as e:
            st.error(f"Error in prediction: {e}")

    def main():
        st.title('Movie Rating Prediction Form')
        st.write("Enter the Movie Details: ")
        
        # Convert inputs to appropriate numerical types
        Year = st.number_input("Movie Release Year", min_value=1900, max_value=2100, step=1, format='%d')
        Duration = st.number_input("Movie Duration (in minutes)", min_value=1, step=1, format='%d')
        Votes = st.number_input("Number of Votes", min_value=1, step=1, format='%d')
        Weighted_Rating = st.number_input("Weighted Rating", min_value=0.0, step=0.1, format='%f')
    
        if st.button('Predict Movie Rating') and all([Year, Duration, Votes, Weighted_Rating]):
            movie_rating_prediction([Year, Duration, Votes, Weighted_Rating])
    main()

