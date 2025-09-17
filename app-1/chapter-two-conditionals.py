import streamlit as  st
import datetime

# st.title("Chai making !!")

# st.text("Select base for your chai")

# base = st.radio("Chai base :", ['Milk', 'Almond Milk', 'Water'])

# ingredient = st.selectbox("Select Additional Ingredient",  ['Ginger',  'Tulsi', 'Honey', 'Turmeric'])

# sugar_level = st.number_input("Select Sugar level", 0,5,2)

# name = st.text_input("Enter your name: ")

# dob = st.date_input("Enter your date of birth")

# if st.button("Make chai"):
#     st.success(f"Welcome,  {name} . Brewing your chai with {base} base added with {ingredient} with {sugar_level} teaspoons sugar. Your birthday is on {dob}")



### BIRTHDAY AGE CALCULATOR

st.title("Calculate your age: ")

dob = st.date_input("Enter your date of birth", min_value="1950-01-01")
# st.write(f"selected date:  {dob}"

today = datetime.date.today()
# calculate difference in years
age_years = today.year - dob.year
age_months = today.month - dob.month
age_days = today.day - dob.day

# adjust if birthday not yet reached this year
if age_days < 0:
    age_months -= 1
    # borrow days from previous month
    last_month = (today.month - 1) if today.month > 1 else 12
    last_month_year = today.year if today.month > 1 else today.year - 1
    days_in_last_month = (datetime.date(last_month_year, last_month % 12 + 1, 1) - datetime.timedelta(days=1)).day
    age_days += days_in_last_month

if age_months < 0:
    age_years -= 1
    age_months += 12

st.write(f"Your Age: {age_years} years, {age_months} months, {age_days} days")