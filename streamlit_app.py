import streamlit as st

"""
# Welcome to my TDEE calculator!

"""

def tdee(sex, weight, height, age, activity_level):
    if activity_level == "sedentary":
        activity = 1.2
    elif activity_level == "lightly active":
        activity = 1.375
    elif activity_level == "moderately active":
        activity = 1.55
    elif activity_level == "very active":
        activity = 1.725
    elif activity_level == "extremely active":
        activity = 1.9
    else:
        return "Invalid activity level"

    if sex == "male":
        bmr = (6.23762 * weight) + (12.7084 * height) - (6.755 * age) + 66.473
    elif sex == "female":
        bmr = (4.33789 * weight) + (4.69798 * height) - (4.6756 * age) + 655.0955
    else:
        return "Invalid sex"

    tdee_result = bmr * activity
    return round(tdee_result)

# Streamlit user inputs
st.sidebar.header('User Input Parameters')

sex = st.sidebar.selectbox('Sex', ('male', 'female'))
weight = st.sidebar.number_input('Weight (lbs)', min_value=0, value=150)
height = st.sidebar.number_input('Height (inches)', min_value=0, value=65)
age = st.sidebar.number_input('Age', min_value=0, value=25)
activity_level = st.sidebar.selectbox('Activity Level', 
                                      ('sedentary', 'lightly active', 'moderately active', 'very active', 'extremely active'))

# Calculate TDEE
tdee_result = tdee(sex, weight, height, age, activity_level)

# Display result
if isinstance(tdee_result, str):
    st.error(tdee_result)
else:
    st.success(f'You burn {tdee_result} calories per day.')
