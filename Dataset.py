# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:34:33 2024

@author: ELCOT
"""
import streamlit as st
import pandas as pd

def data_overview():
    # Dataset Information
    st.title("Dataset Overview:")
    st.write("The predictive model is trained on a dataset containing information about movies, including features such as Name, Year, Duration, Genre, Rating, Votes, Director, Actor 1, Actor 2, and Actor 3.")

    # Data Source
    st.header("Data Source:")
    st.write("For more details, you can explore the dataset on [here](https://www.kaggle.com/datasets/adrianmcmahon/imdb-india-movies)")

    # Sample Data
    st.header("Sample Data:")
    st.write("Here's a glimpse of the movie dataset:")
    data = pd.read_csv("movies_dataset.csv")  # Update with the actual file name
    st.dataframe(data.head())

    # Display your sample data here
    st.subheader("Download Dataset")
    st.write("You can download the full Movie dataset for further exploration:")

    def data_read(data):
        return data.to_csv().encode('utf-8')

    csv=data_read(data)

    st.download_button(
                             label='Download Sample Data',
                             data=csv,
                             file_name='movies_dataset.csv',
                             mime='text/csv'
                      )                   

    # Input Your Data
    st.header("Input Your Data:")
    st.write("Want predictions for your specific movie details? Enter your data in the input form and discover the forecasted rating.")

    # Guidance on Data Format
    st.header("Guidance on Data Format:")
    st.write("To ensure successful predictions, enter your data with the same features as the sample data. Include columns for Year, Duration, Rating, Votes, and Weighted Rating.")

    # GitHub Link
    st.header("GitHub Repository:")
    st.write("Explore the code and details of this project on my GitHub repository:")
    st.write("[Movie Rating Prediction GitHub Repository](https://github.com/Srikhanth14/CODSOFT/blob/main/Project_5_Movie_Rating_Prediction_With_Python.ipynb)")

    # Conclusion
    st.write("Ready to get predictions for your data? Input your movie details in the input form, and let the Movie Rating Prediction app work its magic!")
