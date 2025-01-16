import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Your Profile", page_icon="👤")
st.sidebar.image("./im/LeadingHR_logo.png", use_container_width=False)

st.title("Your Profile")

# Load the employee data from the CSV file
try:
    df = pd.read_csv("data/employees.csv")
except FileNotFoundError:
    st.error("Employee data not found. Please ensure 'data/employees.csv' exists.")
    st.stop()

# Check if the required columns exist
required_columns = {"Name", "Gender", "Email", "Profile", "Country", "City", "Latitude", "Longitude", "Position", "Department"}
if not required_columns.issubset(df.columns):
    st.error("The employee data file is missing required columns. Please regenerate the file.")
    st.stop()

# Select a random employee
random_employee = df.sample(1).iloc[0]

# Display the employee's profile
image_path = random_employee.get("Profile")
if pd.notna(image_path):
    try:
        st.image(image_path, width=200)
    except Exception as e:
        st.warning(f"Could not load image for {random_employee['Name']}.")
else:
    st.warning("No image available for this employee.")

st.header("Personal Information")
st.write(f"**Name:** {random_employee['Name']}")
st.write(f"**Gender:** {random_employee['Gender']}")
st.write(f"**Email:** {random_employee['Email']}")
st.write(f"**City:** {random_employee['City']}")
st.write(f"**Country:** {random_employee['Country']}")

coordinates = {
    "lat": [random_employee["Latitude"]],
    "lon": [random_employee["Longitude"]]
}
st.map(pd.DataFrame(coordinates))

st.header("Position Details")
st.write(f"**Position:** {random_employee['Position']}")
st.write(f"**Department:** {random_employee['Department']}")
