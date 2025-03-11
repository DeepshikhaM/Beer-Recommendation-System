import streamlit as st
import pandas as pd
import numpy as np

# Load dataset
@st.cache
def load_data():
    df = pd.read_csv("beer_data.csv")
    return df

# Load the data
beer_df = load_data()

# Title
st.title("🍺 Beer Recommendation System")

# Introduction
st.write("A hybrid recommendation system using user-based, item-based filtering, and Bayesian optimization.")

# Show dataset preview
if st.checkbox("Show dataset"):
    st.write(beer_df.head())

# Select user input for recommendations
user_input = st.text_input("Enter a user name to get recommendations:", "")

if user_input:
    st.write(f"Generating recommendations for user: {user_input}")
    # Call your recommendation function (Placeholder)
    recommendations = ["Beer A", "Beer B", "Beer C", "Beer D", "Beer E"]
    st.write("**Top Beer Recommendations:**")
    for beer in recommendations:
        st.write(f"- {beer}")

# Footer
st.write("📌 Built with Streamlit | Deployed on Streamlit Cloud")
