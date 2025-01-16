import streamlit as st
import pandas as pd
from geopy.distance import geodesic

st.set_page_config(page_title="Travel Itinerary", page_icon="✈️")
st.sidebar.image("./im/LeadingHR_logo.png", use_container_width=False)

st.title("Travel Itinerary")

# Load the team data from the CSV file
try:
    df = pd.read_csv("data/employees.csv")
except FileNotFoundError:
    st.error("Employee data not found. Please ensure 'data/employees.csv' exists.")
    st.stop()

# Dropdown to select an employee
employee_name = st.selectbox(
    "Select an employee to view their invitation",
    options=df["Name"]
)

# Retrieve selected employee's details
selected_employee = df[df["Name"] == employee_name].iloc[0]

# Event details
event_city = "Rome"
event_airport = "Leonardo da Vinci–Fiumicino Airport (FCO)"
event_date_start = "July 15, 2025"
event_date_end = "July 17, 2025"
employee_city = selected_employee["City"]
employee_country = selected_employee["Country"]
employee_lat_lon = (selected_employee["Latitude"], selected_employee["Longitude"])
event_lat_lon = (41.9028, 12.4964)  # Coordinates of Rome

# Calculate distance and estimate flight price
distance_km = geodesic(employee_lat_lon, event_lat_lon).km
estimated_price = round(50 + (distance_km * 0.25), 2)  # Example pricing logic

flight_details = (
    f"Round-trip flight from {employee_city} Airport to {event_airport}. "
    f"Estimated price: ${estimated_price}."
)

# Display the invitation in a styled box
st.markdown(
    f"""
    <div style="border: 2px solid #ddd; border-radius: 10px; padding: 15px;">
        <h3 style="text-align: center;">Invitation for {selected_employee['Name']} 🎉</h3>
        <p>Dear {selected_employee['Name'].split()[0]},</p>
        <p>We are thrilled to invite you to our corporate summer event taking place in <strong>{event_city} 🇮🇹</strong>.</p>
        <p><strong>Event Dates:</strong> {event_date_start} - {event_date_end}</p>
        <p>Please find your travel itinerary below:</p>
        <ul>
            <li>✈️ {flight_details}</li>
            <li>🧾 Upon arrival, keep your flight receipt and send it to the HR team for reimbursement.</li>
        </ul>
        <p>🌟 <strong>Event Agenda:</strong></p>
        <ul>
            <li>📅 <strong>Day 1:</strong> Arrival in {event_city} and Welcome Dinner 🍝.</li>
            <li>🤝 <strong>Day 2:</strong> Team Building Activities to foster collaboration and innovation 💡.</li>
            <li>📈 <strong>Day 3:</strong> Conference and Networking sessions focused on cutting-edge technology trends 🌐.</li>
        </ul>
        <p>We look forward to seeing you there! Feel free to reach out for any additional details or support.</p>
        <p>Best regards,<br>🌍 The HR Team</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Button to send the invitation email
if st.button("Send Invitation Email"):
    # Placeholder for sending email logic
    st.success(f"The invitation email has been sent to {selected_employee['Email']}!")
