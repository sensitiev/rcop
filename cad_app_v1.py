import streamlit as st
import time
import random

# Set the page configuration
st.set_page_config(
    page_title="CAD Position Sender",
    page_icon="📡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Title of the application
st.title("📡 CAD Position Sender Application")

# Initialize session state variables
if 'step' not in st.session_state:
    st.session_state.step = 1  # Step 1: Ask to send position

if 'position_sent' not in st.session_state:
    st.session_state.position_sent = False

if 'status' not in st.session_state:
    st.session_state.status = None

# Function to simulate sending positional data
def send_position_to_cad():
    # Simulate positional data (latitude and longitude)
    latitude = round(random.uniform(-90.0, 90.0), 6)
    longitude = round(random.uniform(-180.0, 180.0), 6)
    # Simulate sending data (here we just print it)
    st.write(f"📍 Sending Position to CAD:")
    st.write(f"**Latitude:** {latitude}")
    st.write(f"**Longitude:** {longitude}")
    # Simulate delay
    time.sleep(1)
    st.success("✅ Position successfully sent to CAD.")
    # Optionally, store the positional data in session state
    st.session_state.position = {'latitude': latitude, 'longitude': longitude}

# Step 1: Ask if the user wants to send their position
if st.session_state.step == 1:
    st.header("Step 1: Send Position to CAD")
    send_position = st.radio(
        "Do you want to send your position to CAD?",
        ("Yes", "No"),
        index=1  # Default to "No"
    )
    
    if st.button("Submit"):
        if send_position == "Yes":
            send_position_to_cad()
            st.session_state.position_sent = True
            st.session_state.step = 2  # Proceed to next step
        else:
            st.info("❌ Position not sent to CAD.")
            st.session_state.position_sent = False
            st.session_state.step = 2  # Proceed to next step regardless

## step 2
if st.session_state.step==2 and st.session_state.position_sent == True:
    st.header("Step 2: Identify Yourself")
    identity_options = ["Police Vehicle 227", "Fire Truck 123", "Security Van 663", "EMS UNIT 156", "Other"]
    selected_identity = st.selectbox("Who are you?", identity_options)
    
    if st.button("Submit Step 2"):
        st.session_state.identity = selected_identity
        st.success(f"✅ Identified as: **{selected_identity}**")
        st.session_state.step = 3  # Proceed to next step

# Step 3: Ask for the user's status
if st.session_state.step == 3:
    st.header("Step 3: Update Your Status")
    status_options = [
        "En Route to an Incident",
        "At an Incident",
        "CDO Watch Stander",
        "CO",
        "EMO"
    ]
    
    selected_status = st.selectbox("What is your Status?", status_options)
    
    if st.button("Submit Status"):
        st.session_state.status = selected_status
        st.success(f"✅ Status updated to: **{selected_status}**")
        # Optionally, simulate sending status to CAD
        if st.session_state.position_sent:
            st.write("📡 Sending status to CAD...")
            time.sleep(1)
            st.success("✅ Status successfully sent to CAD.")
        else:
            st.info("ℹ️ Position was not sent to CAD; only status was updated.")

# Optional: Display summary of actions
if st.session_state.step ==3:
    st.header("📄 Summary")
    if st.session_state.position_sent:
        pos = st.session_state.get('position', {})
        st.write(f"**Position Sent:** Yes")
        st.write(f"**Latitude:** {pos.get('latitude')}")
        st.write(f"**Longitude:** {pos.get('longitude')}")
    else:
        st.write("**Position Sent:** No")

    st.write(f"**Identification is:** {st.session_state.identity}")
    st.write(f"**Current Status:** {st.session_state.status}")

    st.balloons()  # Celebrate completion
