import streamlit as st
import pandas as pd

st.header('US Costco Locations')
source = pd.read_csv('Costco.csv')
st.write(source)