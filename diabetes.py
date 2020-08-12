import pandas as pd
import numpy as np
import streamlit as st


st.header('# Diabetes Prediction')

st.write(""" 
         
     #    DIABETES PREDICTOR
         
   """)

st.markdown("### Diabetes APP ")

data_df = pd.read_csv('diabetes.csv')
st.sidebar.header('Please Provide Below Information')

#função info
data_df.info()

#função describe
data_df.describe()