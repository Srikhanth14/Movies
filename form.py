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

    def movie_rating_prediction(Year, Duration, Votes, Weighted_Rating):
        
        # Create a dictionary from inputs
        user_input = {
            'Year': [Year], 
            'Duration': [Duration], 
            'Votes': [Votes], 
            'Weighted_Rating': [Weighted_Rating]
        }

        # Convert dictionary to DataFrame
        input_df = pd.DataFrame(user_input)
        
        # Make prediction
        prediction = loaded_model.predict(input_df)
        st.success(f"The predicted movie rating is: {prediction[0]:.2f}")

    def main():
        st.title('Movie Rating Prediction Form')
        st.write("Enter the Movie Details: ")
        
        # Convert inputs to appropriate numerical types
        Year = st.number_input("Movie Release Year", min_value=1900, max_value=2100, step=1, format='%d')
        Duration = st.number_input("Movie Duration (in minutes)", min_value=1, step=1, format='%d')
        Votes = st.number_input("Number of Votes", min_value=1, step=1, format='%d')
        Weighted_Rating = st.number_input("Weighted Rating", min_value=0.0, step=0.1, format='%f')
    
        if st.button('Predict Movie Rating'):
            movie_rating_prediction(int(Year), int(Duration), int(Votes), float(Weighted_Rating))
    main()
    

