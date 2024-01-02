# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:28:59 2024

@author: ELCOT
"""

import streamlit as st
from streamlit_option_menu import option_menu
import home,Dataset,Visualization,form

st.set_page_config(page_title="Movie Rating", page_icon="🎬", layout="wide")
selected = option_menu(
                        menu_title="Movie Rating",
                        options=["Welcome","Data Overview","Visualization","Form"],
                        icons=["house-heart", "database-down", "vignette","ui-radios",],
                        default_index=0,
menu_icon="film",                        orientation="horizontal"
                      )

if selected == "Welcome":
    home.welcome()
if selected == "Data Overview":
    Dataset.data_overview()
if selected == "Form":
    form.rating_prediction()
if selected == "Visualization":
   Visualization.exploratory_charts()
