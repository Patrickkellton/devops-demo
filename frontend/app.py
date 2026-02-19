import streamlit as st
import requests

st.title("Frontend")

if st.button("Call backend"):
    response = requests.get("http://backend:8000/")
    st.write(response.json())