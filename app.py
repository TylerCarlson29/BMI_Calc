Conversation with Gemini
You said
Create an app to calculate the BMI using Git hub and stream lit.

The weight should be in Kg

The height should be in meters



BMI =  Weight/Height *Height

Gemini said
Building a BMI calculator with Streamlit is a fantastic way to deploy a data app quickly. Since we are using GitHub, I’ll walk you through the code and the steps to get it hosted.

One quick note on the formula: mathematically, it is Weight divided by (Height squared). In code, that looks like:

BMI= 
height 
2
 
weight
​
 
1. The Code (app.py)
Create a file named app.py and paste the following code. This uses Streamlit’s simple input widgets to capture user data.

Python
import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("⚖️ Body Mass Index Calculator")

with st.container():
    st.write("Enter your details below to calculate your BMI.")
    
    # Input fields
    weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
    height = st.number_input("Height (m)", min_value=0.1, step=0.01)

if st.button("Calculate BMI"):
    if height > 0:
        # Formula: weight / (height * height)
        bmi = weight / (height ** 2)
        bmi_result = round(bmi, 2)
        
        st.subheader(f"Your BMI is: {bmi_result}")
        
        # Interpretation logic
        if bmi_result < 18.5:
            st.warning("Category: Underweight")
        elif 18.5 <= bmi_result <= 24.9:
            st.success("Category: Healthy Weight")
        elif 25.0 <= bmi_result <= 29.9:
            st.info("Category: Overweight")
        else:
            st.error("Category: Obesity")
    else:
        st.error("Height must be greater than 0.")
