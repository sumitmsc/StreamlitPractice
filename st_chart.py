import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "x": [1,2,3,4,5],
    "y": [10,20,30,25,15]
})

st.title("Simple Line Chart")
st.line_chart(df)
