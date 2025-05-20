# Patient Health Monitoring Dashboard
# This Streamlit application visualizes patient health data from a JSON file, 
# allowing healthcare providers to monitor patient status and health progression over time.

import streamlit as st   # Streamlit library for web application
import pandas as pd      # Pandas for data manipulation
import matplotlib.pyplot as plt    # Matplotlib for creating visualizations
import matplotlib.patches as mpatches  # For custom legend elements
import json              # For reading the JSON data file
import time              # For refresh functionality

# Load patient data from JSON file
with open('patients.json') as f:
    data = json.load(f)

# Convert JSON data to DataFrame and prepare for analysis
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])  # Convert timestamp strings to datetime objects
df = df.sort_values(by=['id', 'timestamp'])  # Sort by patient ID and timestamp

# Extract list of unique patient IDs for the selector
patient_ids = df['id'].unique()

# Sidebar patient selector
selected_id = st.sidebar.selectbox("Select Patient ID", patient_ids)
patient_data = df[df['id'] == selected_id]  # Filter data for selected patient

#--------sidebar--------

# Get the most recent data entry for the selected patient
latest_entry = patient_data.iloc[-1]
latest_value = latest_entry['value']  # Current health score
room_location = latest_entry['room']  # Current room location

# Determine health status based on the latest health score value
if latest_value >= 7:
    status_color = "🟢 Stable"
elif latest_value >= 4:
    status_color = "🟡 Moderate"
else:
    status_color = "🔴 Critical"

# --- Auto Refresh Settings ---
AUTO_REFRESH_INTERVAL = 10  # seconds

# Initialize session state for tracking refresh time
if "last_refresh" not in st.session_state:
    st.session_state.last_refresh = time.time()

# Display main patient status panel
st.markdown(f"## 🧑‍⚕️ Patient Status Panel: `{selected_id}`")
col1, col2 = st.columns([3,2])  # Create two columns for layout
with col1:
    st.markdown(f"**Room Location:** {room_location}")
    st.markdown(f"**Current Health Score:** {latest_value}/10")

with col2:
    st.markdown(f"**Status:** {status_color}")
    # --- Manual Refresh Button ---
    if st.button("🔄 Manual Refresh"):
        st.session_state.last_refresh = time.time()  # update time
        st.rerun()  # Refresh the app

# Get the full time range for the selected patient
min_time = patient_data['timestamp'].min().to_pydatetime()
max_time = patient_data['timestamp'].max().to_pydatetime()

# Sidebar time range selector
selected_time_range = st.slider(
    "⏱️ Select Time Interval",
    min_value=min_time,
    max_value=max_time,
    value=(min_time, max_time),
    format="YYYY-MM-DD HH:mm"
)

# Filter data based on selected time range
filtered_data = patient_data[
    (patient_data['timestamp'] >= selected_time_range[0]) &
    (patient_data['timestamp'] <= selected_time_range[1])
]
    
# --- Health Progression Graph with Color-Coded Points ---
st.markdown("### 📈 Health State Progression")

# Define color mapping function for health scores
def get_color(value):
    if value >= 7:
        return 'green'   # Stable
    elif value >= 4:
        return 'orange'  # Moderate
    else:
        return 'red'     # Critical

# Generate colors for each data point based on health score
colors = filtered_data['value'].apply(get_color)

# Create visualization
fig, ax = plt.subplots(figsize=(10, 4))
ax.scatter(filtered_data['timestamp'], filtered_data['value'], color=colors, s=100)  # s=point size
ax.plot(filtered_data['timestamp'], filtered_data['value'], color='lightgray', linestyle='--', alpha=0.5)

ax.set_ylim(0, 10)  # Set y-axis limits for health score
ax.set_title(f"Health Progression for {selected_id}")
ax.set_xlabel("Time")
ax.set_ylabel("Health Score (0–10)")

# --- Custom legend creation ---
legend_patches = [
    mpatches.Patch(color='green', label='Low'),
    mpatches.Patch(color='orange', label='Moderate'),
    mpatches.Patch(color='red', label='High')
]
ax.legend(handles=legend_patches, title="Status")

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Display the graph
st.pyplot(fig)