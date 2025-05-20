# --- Imports ---
import streamlit as st               # Streamlit for building the web-based UI
import json                         # JSON module for reading and writing data
import os                           # OS module to check file existence
from datetime import datetime       # Used for timestamping events

# --- File Paths ---
AGENT_FILE = "shared_data/agents.json"     # File to store agent records
PATIENT_FILE = "shared_data/patient.json"  # File to store patient records
EVENT_FILE = "shared_data/event_log.json"  # File to store event logs

# --- Utility Functions ---

def load_json(path, default={}):
    """
    Loads JSON data from a file.
    Returns the content if successful, otherwise returns the provided default.
    Handles file not found or malformed JSON gracefully.
    """
    if os.path.exists(path):
        with open(path, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return default
    return default

def save_json(path, data):
    """
    Saves Python data as JSON to the specified file path.
    Displays an error using Streamlit if the write operation fails.
    """
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        st.error(f"Error saving JSON: {e}")

def append_json(path, entry):
    """
    Appends a dictionary entry to a JSON file.
    Converts file content into a list if it isn't one already.
    Handles errors and displays them via Streamlit.
    """
    try:
        existing = load_json(path, default=[])
        if not isinstance(existing, list):
            existing = [existing]
        existing.append(entry)
        save_json(path, existing)
    except Exception as e:
        st.error(f"Error appending JSON: {e}")

# --- Streamlit UI Setup ---

st.title("🧠 Agent-Patient-Event Manager")  # App title

# Create four interactive tabs
tab1, tab2, tab3, tab4 = st.tabs(["🧑 Agents", "🏥 Patients", "📝 Add Event", "📂 View/Edit Files"])

# --- AGENT TAB ---
with tab1:
    st.header("Manage Agents")
    agents = load_json(AGENT_FILE, default={})  # Load current agents

    # Select action type
    action = st.radio("Action", ["Add", "Update", "Delete"])
    agent_id = st.text_input("Agent ID")  # Input for unique agent ID

    # Additional inputs for Add/Update
    if action in ["Add", "Update"]:
        name = st.text_input("Name")
        role = st.text_input("Role")

    # Action button
    if st.button(f"{action} Agent"):
        if action == "Add" and agent_id:
            agents[agent_id] = {"name": name, "role": role}
        elif action == "Update" and agent_id in agents:
            agents[agent_id].update({"name": name, "role": role})
        elif action == "Delete" and agent_id in agents:
            del agents[agent_id]
        else:
            st.warning("Invalid Agent ID or Action.")
        save_json(AGENT_FILE, agents)  # Save updated data
        st.success(f"Agent {action}d successfully.")

    st.subheader("Current Agents")
    st.json(agents)  # Display agent data as JSON

# --- PATIENT TAB ---
with tab2:
    st.header("Manage Patients")
    patients = load_json(PATIENT_FILE, default={})  # Load current patients

    # Select action type
    action = st.radio("Action", ["Add", "Update", "Delete"], key="patient_action")
    patient_id = st.text_input("Patient ID")  # Input for patient ID

    # Additional inputs for Add/Update
    if action in ["Add", "Update"]:
        name = st.text_input("Patient Name")
        condition = st.text_input("Condition")

    # Action button
    if st.button(f"{action} Patient"):
        if action == "Add" and patient_id:
            patients[patient_id] = {"name": name, "condition": condition}
        elif action == "Update" and patient_id in patients:
            patients[patient_id].update({"name": name, "condition": condition})
        elif action == "Delete" and patient_id in patients:
            del patients[patient_id]
        else:
            st.warning("Invalid Patient ID or Action.")
        save_json(PATIENT_FILE, patients)  # Save updated data
        st.success(f"Patient {action}d successfully.")

    st.subheader("Current Patients")
    st.json(patients)  # Display patient data as JSON

# --- EVENT TAB ---
with tab3:
    st.header("Add Event")

    # Input fields for event creation
    agent_id = st.text_input("Agent ID (Event)")
    patient_id = st.text_input("Patient ID (Event)")
    description = st.text_area("Event Description")

    # Add event to log
    if st.button("➕ Add Event"):
        if agent_id and patient_id and description:
            event = {
                "agent_id": agent_id,
                "patient_id": patient_id,
                "description": description,
                "timestamp": datetime.utcnow().isoformat()  # Timestamp in ISO format
            }
            append_json(EVENT_FILE, event)  # Add event to log
            st.success("✅ Event added successfully.")
        else:
            st.warning("Please fill in all fields.")

# --- JSON VIEW / EDIT TAB ---
with tab4:
    st.header("View/Edit Raw Files")

    # Map display names to file paths
    file_map = {
        "Agents": AGENT_FILE,
        "Patients": PATIENT_FILE,
        "Event Log": EVENT_FILE
    }

    selected_file = st.selectbox("Select a file to edit", list(file_map.keys()))
    file_path = file_map[selected_file]
    content = load_json(file_path, default={})  # Load content of selected file

    # Display and edit JSON manually
    st.subheader(f"Raw content of {selected_file}")
    edited_text = st.text_area("Edit JSON manually", json.dumps(content, indent=2), height=400)

    # Save edited JSON
    if st.button("💾 Save Edited JSON"):
        try:
            new_content = json.loads(edited_text)
            save_json(file_path, new_content)
            st.success("✅ File saved.")
        except json.JSONDecodeError as e:
            st.error(f"Invalid JSON: {e}")
