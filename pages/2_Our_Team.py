import streamlit as st
import pandas as pd

st.set_page_config(page_title="Our Team", page_icon="👥")
st.sidebar.image("./im/LeadingHR_logo.png", use_container_width=False)

st.title("Our Team")

# Load the team data from the updated CSV file
try:
    df = pd.read_csv("data/employees.csv")
except FileNotFoundError:
    st.error("Employee data not found. Please ensure 'data/employees.csv' exists.")
    st.stop()

# Check if the required columns exist
required_columns = {"Name", "Email", "Profile", "Country", "City", "Position", "Department"}
if not required_columns.issubset(df.columns):
    st.error("The employee data file is missing required columns. Please regenerate the file.")
    st.stop()

# Reorder columns as specified
df_display = df[["Profile", "Name", "Email", "Position", "Department", "City", "Country"]]

# Format the images in a circular style
df_display["Profile"] = df_display["Profile"].apply(
    lambda x: f'<img src="{x}" style="border-radius: 50%; width: 50px; height: 50px;">'
)

# Define a custom HTML style for left-aligning headers
custom_css = """
<style>
    th {
        text-align: left !important;
    }
</style>
"""

# Display the team data with formatted images
st.header("Team Members")
st.write(custom_css + df_display.to_html(escape=False, index=False), unsafe_allow_html=True)

# Allow the user to download the team data as a CSV file
st.download_button(
    label="Download Team as CSV",
    data=df_display.to_csv(index=False),
    file_name="team.csv",
    mime="text/csv"
)

# Display team locations on a map
st.header("Team Locations")
coordinates = {
    "lat": df["Latitude"],
    "lon": df["Longitude"]
}
st.map(pd.DataFrame(coordinates))
