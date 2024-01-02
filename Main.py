# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:28:59 2024

@author: ELCOT
"""

import streamlit as st
from streamlit_option_menu import option_menu
import home, Dataset,Visualization,form

st.set_page_config(page_title="Movie Rating Prediction", page_icon="film", layout="wide")
selected = option_menu(
                        menu_title="Movie Rating Prediction App",
                        options=["Welcome", "Data Overview", "Visualization","Rating Prediction Form",],
                        icons=["🏠", "📊", "📈","🎬",],
                        default_index=0,
                        orientation="horizontal"
                      )

if selected == "Home":
    home.welcome()
if selected == "Data Overview":
    Dataset.data_overview()
if selected == "Rating Prediction Form":
    Visualization.rating_prediction()
if selected == "Visualization":
   form.exploratory_charts()
