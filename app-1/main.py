import streamlit as st

#basic commands
st.title("This  is streamlit app 1")
st.subheader("Using streamlit library")

st.text("Using vs code as code editor")
st.write("Choose your programming language!")

lang = st.selectbox("Choose language", ['Python', 'Javascript', 'c++', 'Ruby', 'PHP'])

st.text(f"Great choice! , {lang} is good to begin with.")

st.success("You have chosen a language!")
