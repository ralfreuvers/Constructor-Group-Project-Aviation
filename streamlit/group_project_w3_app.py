import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import io
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

# Load data file


# Title + headers
st.title("In-Flight Emergencies")
st.text("")


# Navigation bar
selected = option_menu(None, ["Home", "Model", "Visualization", 'Sources'], 
    icons=['house', 'graph-up', 'bar-chart', 'globe2'], 
    menu_icon="cast", default_index=0, orientation="horizontal")


# HOME
if selected == "Home":
    st.header("Home")
    st.text("Welcome text about our project")


# MODEL
if selected == "Model":
    st.header("Our models")


# VISUALIZATION
if selected == "Visualization":
    st.header("Fancy graphs")


# SOURCES
if selected == "Sources":
    st.header("Sources:")