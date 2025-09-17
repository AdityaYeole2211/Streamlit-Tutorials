import streamlit as st

st.title("chai vote")

col1,col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/18419702/pexels-photo-18419702.jpeg", width=300)
    vote1 = st.button("Vote Masala Chai")
with col2 :
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/2262832/pexels-photo-2262832.jpeg", width=300)
    vote2 = st.button("Vote Adrak Chai")
    
if vote1:
    st.success("You voted Masala Chai")
elif vote2:
    st.success("You voted Adrak Chai")
    

#side bar
name = st.sidebar.text_input("Enter your name")
chai = st.sidebar.selectbox("Your chai choice: ", ['Masala', 'kesar', 'Adrak'])

st.write(f"Welcome, {name}, Your {chai} chai is getting ready!")

#expander
with st.expander("Expand to show recipe:"):
    st.write("""
             1. Boil water and pour tea leaves.
             2. Put milk and sugar 
             3. Serve hot.
             """)

# if want to write markdown style 

st.markdown("# Chai is life.")
st.markdown("### chai is eveyrones life")
st.markdown("> blockquote")