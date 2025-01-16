import streamlit as st
import requests
from geopy.distance import geodesic
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="Closest City", page_icon="🌍")
st.sidebar.image("./im/LeadingHR_logo.png", use_container_width=False)

st.title("Find the Closest City")

# Load the team data from the CSV file
try:
    df = pd.read_csv("data/employees.csv")
except FileNotFoundError:
    st.error("Team data is not available. Please ensure 'data/employees.csv' exists.")
    st.stop()

# Check if the required columns exist
required_columns = {"Latitude", "Longitude", "City", "Country"}
if not required_columns.issubset(df.columns):
    st.error("The team data file is missing required columns. Please regenerate the file.")
    st.stop()

# Extract locations
locations = list(zip(df["Latitude"], df["Longitude"]))

# Find central point
if locations:
    latitudes, longitudes = zip(*locations)
    center_point = (sum(latitudes) / len(latitudes), sum(longitudes) / len(longitudes))
    st.write(f"Central location of the team (latitude, longitude): ({center_point[0]:.2f}, {center_point[1]:.2f})")


    # Match center point to the closest capital city with a population of at least 1 million
    capital_cities = [
        {"name": "Berlin", "coordinates": (52.5200, 13.4050), "population": 3769000},
        {"name": "London", "coordinates": (51.5074, -0.1278), "population": 8982000},
        {"name": "Paris", "coordinates": (48.8566, 2.3522), "population": 2148000},
        {"name": "Madrid", "coordinates": (40.4168, -3.7038), "population": 3223000},
        {"name": "Rome", "coordinates": (41.9028, 12.4964), "population": 2873000},
        {"name": "Moscow", "coordinates": (55.7558, 37.6173), "population": 10381222},
        {"name": "Kyiv", "coordinates": (50.4501, 30.5234), "population": 2797553},
        {"name": "Bucharest", "coordinates": (44.4268, 26.1025), "population": 1877155},
        {"name": "Minsk", "coordinates": (53.9006, 27.5590), "population": 1742124},
        {"name": "Budapest", "coordinates": (47.4979, 19.0402), "population": 1741041},
        {"name": "Warsaw", "coordinates": (52.2297, 21.0122), "population": 1702139},
        {"name": "Vienna", "coordinates": (48.2082, 16.3738), "population": 1691468}
    ]


    closest_city = min(
        capital_cities,
        key=lambda city: geodesic(center_point, city["coordinates"]).kilometers
    )

    st.write(f"Closest capital city: {closest_city['name']} (Population: {closest_city['population']:,})")

    # Display the city on the map
    city_location = pd.DataFrame({
        'lat': [closest_city['coordinates'][0]],
        'lon': [closest_city['coordinates'][1]]
    })
    st.map(city_location)



    # Fetch weather data for the city
    weather_response = requests.get(f"http://wttr.in/{closest_city['name']}?format=4")
    if weather_response.status_code == 200:
        weather_data = weather_response.text
    else:
        weather_data = "Weather information is not available at the moment."

    # Get the current time for the city
    city_timezone = pytz.timezone("Europe/Rome")  # Adjust this dynamically based on city
    current_time = datetime.now(city_timezone).strftime("%Y-%m-%d %H:%M:%S")

    # Display information
    st.write(weather_data)
    st.write(f"Current Time: {current_time}")
