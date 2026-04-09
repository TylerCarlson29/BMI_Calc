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
        # Formula: weight / (height^2)
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
