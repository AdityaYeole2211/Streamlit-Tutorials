import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSV ANALYZER")

file = st.file_uploader("Upload your CSV file", type=['csv'])

if file:
    st.success("File uploaded successfully")
    df = pd.read_csv(file)
    st.subheader("DATASET PREVIEW: ")
    st.dataframe(df.head())
    
    st.subheader("Summary: ")
    st.dataframe(df.describe())
    
    st.subheader("Country wise GDP:")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df['Country Name'], df['GDP (in USD)'], marker='o', linestyle='-')
    ax.set_title("Countrywise GDP")
    ax.set_xlabel("Country")
    ax.set_ylabel("GDP (in USD)")
    ax.grid(True)
    plt.xticks(rotation=45)  # rotate x labels if countries overlap
    
    st.pyplot(fig)  # <-- show the figure in Streamlit


