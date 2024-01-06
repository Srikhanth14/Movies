# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:34:46 2024

@author: ELCOT
"""

import streamlit as st
from PIL import Image

def welcome():
    
    st.image(Image.open('Movies1.jpg'),use_column_width=True)
    # Introduction
    st.title("Movie Rating Prediction App")
    st.write("Embark on a cinematic adventure as we predict movie ratings using machine learning. This web app leverages data insights to estimate a movie's rating based on various features.")

    # Key Features
    st.subheader("Key Features:")
    st.write('''1. **Predictive Analytics:**
    Explore the predictions of movie ratings using advanced analytics. The model considers features like release year, duration, director, and more.''')

    st.write('''2. **User-Friendly Interface:**
    Navigate through the app effortlessly. No expertise required – simply input movie details and discover the predicted rating.''')

    st.write('''3. **Data Visualization:**
    Visualize patterns and trends in the dataset with interactive charts. Gain insights into the factors influencing movie ratings.''')

    # About the Project
    st.subheader("About the Project:")
    st.write("The Movie Rating Prediction project blends the magic of movies with data science techniques. Join us in exploring the features that contribute to predicting a movie's rating.")

    # About You
    st.subheader("About Me:")
    st.write("Curious about the mind behind the predictions? I'm SRIKHANTH R, a passionate data analyst dedicated to unraveling insights from data.")
    st.write("Feel free to connect with me on [LinkedIn](inkedin.com/in/srikhanth-r) or explore more projects on my [portfolio](datascienceportfol.io/srikhanth_r). Let's dive deep into the world of movie ratings together!")

    # Call to Action
    st.write("Ready to explore the world of movie ratings? Head over to the **Data Overview** page to dive into the dataset and make your own rating predictions!")
