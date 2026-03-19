import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Snack Expiry & Profit Analysis")

# Load data
df_snacks = pd.read_csv(r"C:\Users\dshak\Downloads\Snacks_data.csv")

# Dropdown for snack selection
snack_name = st.selectbox("Select Snack", df_snacks['Snack Name'].unique())
snack_name = st.selectbox("Select Company", df_snacks['Company Name'].unique())

# Filter data
filtered_data = df_snacks[df_snacks['Snack Name'] == snack_name]
filtered_data = df_snacks[df_snacks['Company Name'] == snack_name]

# Show result
st.subheader(f"Details of {snack_name}")
st.write(filtered_data)


