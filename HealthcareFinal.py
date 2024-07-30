import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Assessing the Risk Factors on Type 2 Diabetes in the North Africa and Middle East Region")
try:
    df = pd.read_csv("https://github.com/hadilfs/Healthcare/blob/main/IHME-GBD_2021_DATA-7e856563-1.csv", on_bad_lines='skip')  # Handles problematic lines
    print(df.head())
except pd.errors.ParserError as e:
    print(f"ParserError: {e}")
st.title(df)
