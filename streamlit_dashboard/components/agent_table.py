import pandas as pd
import streamlit as st

def show_agents(agent_data, room_filter):
    df = pd.DataFrame(agent_data)
    if "current_room" not in df.columns:
        st.warning("Missing 'current_room' column in agent data.")
        st.dataframe(df)
        return

    filtered_df = df[df["current_room"] == room_filter]
    st.subheader(f"👩‍⚕️ Agents in Room: {room_filter}")
    st.dataframe(filtered_df, use_container_width=True)

