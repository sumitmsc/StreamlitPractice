import streamlit as st

st.title("User Input Form")

with st.form("user_form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=1, max_value=100)
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success(f"Hello {name}, age {age}")
