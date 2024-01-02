# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:34:46 2024

@author: ELCOT
"""

import streamlit as st
from PIL import Image
def exploratory_charts():
    # Page Title
    st.title("Exploratory Charts")

    st.write("Explore visualizations highlighting patterns and insights from movie data.")
        # Chart 1: Year vs Rating (Barplot)
    st.header("1. Year vs Rating (Barplot)")
    image1 = Image.open("Year.png")  # Update with your actual image path
    st.image(image1, caption="Year vs Rating", use_column_width=True)
    
    # Chart 2: Correlation between Duration and Rating (Heatmap)
    st.header("2. Correlation between Duration and Rating (Heatmap)")
    image2 = Image.open("correlation.png")  # Update with your actual image path
    st.image(image2, caption="Correlation between Duration and Rating",   use_column_width=True)
    
    # Chart 3: Genre Counts (Barplot)
    st.header("3. Genre Counts (Barplot)")
    image3 = Image.open("Genre.png")  # Update with your actual image path
    st.image(image3, caption="Genre Counts", use_column_width=True)
    
    # Chart 4: Top 10 Actors by Movie Count (Barplot)
    st.header("4. Top 10 Actors by Movie Count (Barplot)")
    image4 = Image.open("top10.png")  # Update with your actual image path
    st.image(image4, caption="Top 10 Actors by Movie Count", use_column_width=True)
    
    # Chart 5: Top 10 Movies by Weighted Rating (Barplot)
    st.header("5. Top 10 Movies by Weighted Rating (Barplot)")
    image5 = Image.open("Family.png")  # Update with your actual image path
    st.image(image5, caption="Top 10 Movies by Weighted Rating", use_column_width=True)

    # Call to Action
    st.write("Ready to explore more or make predictions? Head to the **Dataset** and **Rating Prediction Form** pages for a deeper dive into the movie data.")
