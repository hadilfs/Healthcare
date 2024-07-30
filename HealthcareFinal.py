import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv("https://github.com/hadilfs/Healthcare/blob/main/IHME-GBD_2021_DATA-7e856563-1.csv")
st.title("Visualization mortality rate in Lebanon")

