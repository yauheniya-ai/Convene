# Introduction.py
import streamlit as st
import requests
import pandas as pd
from PIL import Image
import itertools
import time

# Sidebar
st.set_page_config(page_title="Corporate Event Organizer", page_icon="./im/LeadingHR_tn.png")
st.sidebar.image("./im/LeadingHR_logo.png", use_container_width=False)

# Main
st.title("Welcome to the Corporate Event Organizer! 🎉")

# Add image slider functionality
def image_slider(image_paths, width=800):
    placeholder = st.empty()
    while True:
        for img_path in itertools.cycle(image_paths):
            img = Image.open(img_path)
            placeholder.image(img, width=width)
            time.sleep(2)

image_files = [
    "./im/corporate_event_00.jpeg",
    "./im/corporate_event_01.jpeg",
    "./im/corporate_event_02.jpeg",
    "./im/corporate_event_03.jpeg",
    "./im/corporate_event_04.jpeg"
]

st.write("Enjoy browsing some of our past corporate events!")
st.write("Below is a dynamic image slider showcasing our events:")
image_slider(image_files, width=800)


st.markdown(
    """
    This app helps organize corporate events effortlessly by managing your team and event details.

    - **Page 1:** Your Profile - View a random user from the team.
    - **Page 2:** Our Team - View all team members and their locations.
    - **Page 3:** Closest City - Find the central meeting point for the team.
    - **Page 4:** Travel Itinerary - Generate travel plans for the event.

    Let's get started!
    """
)


