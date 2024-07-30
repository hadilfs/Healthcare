import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Assessing the Risk Factors on Type 2 Diabetes in the North Africa and Middle East Region")
df = pd.read_csv("https://github.com/hadilfs/Healthcare/blob/main/IHME-GBD_2021_DATA-7e856563-1.csv", delimiter=',')
