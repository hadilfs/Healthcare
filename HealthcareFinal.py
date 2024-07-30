import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Assessing the Risk Factors on Type 2 Diabetes in the North Africa and Middle East Region")
df = pd.read_csv("https://raw.githubusercontent.com/hadilfs/Healthcare/main/combined_data.csv") 
st.write(df.head())
