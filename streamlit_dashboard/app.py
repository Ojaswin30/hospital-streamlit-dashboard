import streamlit as st
import time

from components.agent_table import show_agents
from components.patient_list import show_patients
from utils.data_handler import load_json, simulate_updates

# Configure the Streamlit app page
st.set_page_config(layout="wide", page_title="Hospital Dashboard")

# Display the main header and description of the dashboard
st.title("🏥 Winniio Hospital Dashboard")
st.markdown("Real-time patient and agent monitoring interface")

# Sidebar header for filter options
st.sidebar.header("Filters")

# Refresh interval in seconds for the dashboard updates
REFRESH_INTERVAL = 2  # seconds

# Placeholder container to dynamically update the dashboard content (rerun every 2 seconds)
placeholder = st.empty()

# Main application loop to refresh the dashboard continuously
while True:
    with placeholder.container():
        # Load agent and patient data from JSON files and simulate status updates
        agents = simulate_updates(load_json("shared_data/agents.json"), "status", ["On Duty", "Off Duty"])
        patients = simulate_updates(load_json("shared_data/patient.json"), "status", ["Active", "Idle", "Completed"])

        # Extract unique room names from agents for filtering dropdown
        rooms = sorted(set(agent["current_room"] for agent in agents))
        # Extract unique patient statuses for filtering dropdown
        statuses = sorted(set(patient["status"] for patient in patients))

        # Sidebar dropdown filters for room selection (agents) and patient status
        selected_room = st.sidebar.selectbox("Select Room for Agents", rooms, key="room")
        selected_status = st.sidebar.selectbox("Select Patient Status", statuses, key="status")

        # Two-column layout to display filtered agent and patient information side by side
        col1, col2 = st.columns(2)
        with col1:
            show_agents(agents, selected_room)
        with col2:
            show_patients(patients, selected_status)

    # Pause execution for the refresh interval before rerunning the app
    time.sleep(REFRESH_INTERVAL)
    # Trigger a rerun of the Streamlit app to refresh displayed data
    st.rerun()






