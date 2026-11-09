import streamlit as st
# import joblib
# import pandas as pd

# 1. Load your model once and cache it so the app stays fast!
# @st.cache_resource
# def load_model():
#     return joblib.load("model.pkl")
# model = load_model()

# 2. Build the User Interface
st.title("🚀 My Colab App")
st.write("Enter your details below to get a result:")

# Create input fields
user_text = st.text_input("Enter some text:", "Hello World")
user_number = st.number_input("Enter a number:", value=10)

# 3. Run your Colab code when the button is clicked
if st.button("Run Prediction"):
  # --- PUT YOUR COLAB LOGIC HERE ---
  # e.g., prediction = model.predict([[user_number]])
  result = f"You typed '{user_text}' and your number doubled is {user_number * 2}"

  # Display the output on the webpage
  st.success(f"Result: {result}")
