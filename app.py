import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Configuration
st.set_page_config(page_title="EcoGreenData", layout="wide")
DATA_FILE = "data_wastage.csv"

st.title("🌱 EcoGreenData : Collection & Analysis")

# --- 1. COLLECTION (The form) ---
st.header("Data entry")
with st.form("form"):
    col1, col2 = st.columns(2)
    with col1:
        meal = st.selectbox("Meal", ["Breakfast", "Launch", "Dinner"])
        category = st.selectbox("Type of food", ["Bread", "Vegetables", "Meat", "Starchy food"])
    with col2:
        mass = st.number_input("Mass thrown (kg)", min_value=0.0, step=0.1)
        submit = st.form_submit_button("Save")
        
if submit:
    if mass > 0:
        # Creating a data line (like a struct instance)
        new_entry = pd.DataFrame([[meal, category, mass]], columns=["Meal", "Category", "Mass"])
        
        # Saving in the CSV (mode 'a' for Append)
        new_entry.to_csv(DATA_FILE, mode='a', index=False, header=not os.path.exists(DATA_FILE))
        st.success(f"Saved : {mass}kg of {category}")
    else:
        st.error("The mass must be superior to 0 kg !")
        
st.divider()

# --- 2. DATA ANALYSIS ---
st.header("Descriptive analysis")

if os.path.exists(DATA_FILE):
    # Reading data
    df = pd.read_csv(DATA_FILE)
    
    # Display of quick stats
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Total thrown", f"{df['mass'].sum():.1f} kg")
    col_b.metric("Average per entry", f"{df['Mass'].mean():.2f} kg")
    col_c.metric("Number of entries", len(df))
    
    # Interactive graph with Plotly
    fig = px.pie(df, values='Mass', names='Category', title="Distribution of wastage by category")
    st.plotly_chart(fig, use_container_width=True)
    
    # Display of raw table
    with st.expander("See raw data"):
        st.dataframe(df)
        
else:
    st.info("No saved data for now. Fill in the form above.")