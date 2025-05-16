import streamlit as st
import time

from components.agent_table import show_agents
from components.patient_list import show_patients
from utils.data_handler import load_json, simulate_updates

st.set_page_config(layout="wide", page_title="Hospital Dashboard")

# Header
st.title("🏥 Winniio Hospital Dashboard")
st.markdown("Real-time patient and agent monitoring interface")

# Sidebar Filters
st.sidebar.header("Filters")

# Auto-refresh interval
REFRESH_INTERVAL = 2  # seconds

# App refresh loop (rerun every 2 seconds)
placeholder = st.empty()

while True:
    with placeholder.container():
        # Load and simulate data updates
        agents = simulate_updates(load_json("shared_data/agents.json"), "status", ["On Duty", "Off Duty"])
        patients = simulate_updates(load_json("shared_data/patient.json"), "status", ["Active", "Idle", "Completed"])

        # Unique values for dropdowns
        rooms = sorted(set(agent["current_room"] for agent in agents))
        statuses = sorted(set(patient["status"] for patient in patients))

        selected_room = st.sidebar.selectbox("Select Room for Agents", rooms, key="room")
        selected_status = st.sidebar.selectbox("Select Patient Status", statuses, key="status")

        # Layout: 2-column panel
        col1, col2 = st.columns(2)
        with col1:
            show_agents(agents, selected_room)
        with col2:
            show_patients(patients, selected_status)

    time.sleep(REFRESH_INTERVAL)
    st.rerun()






