import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration (Title of the tab)
st.set_page_config(page_title="EcoGreenData", layout="wide")

st.title("🌱 EcoGreenData : Collecte de Gaspillage")

# --- SECTION 1 : COLLECTE DES DONNEES ---
st.header("1. Information Writing")

# We use a form to gather the entries (efficiency)
with st.form("Writing_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        date_input = st.date_input("Date", datetime.now())
        meal = st.selectbox("Type of meal", ["Breakfast", "Diner"])
        
    with col2:
        category = st.selectbox("Food category", ["Bread", "Starchy foods", "Proteins", "Vegetables"])
        mass = st.number_input("Mass thrown (kg)", min_value=0.0, step=0.1)
        
    submit = st.form_submit_button("Save data")