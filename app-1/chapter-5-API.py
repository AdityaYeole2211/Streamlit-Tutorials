import streamlit as st
import requests

st.title("INR Currency Converter")

inr = st.number_input("Enter the currency in INR", min_value=1)

toConvert = st.selectbox("Enter currency to convert: ", ['USD', 'EUR', 'GBP', 'RUB'])

if st.button("Convert"):
    url = 'https://api.exchangerate-api.com/v4/latest/INR'
    response = requests.get(url)
    data = response.json()
    factor = data['rates'][toConvert]
    converted = inr * factor
    st.success(f"{inr} INR = {converted : .3f} {toConvert}")

