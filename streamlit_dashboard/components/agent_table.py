import pandas as pd
import streamlit as st

def show_agents(agent_data, room_filter):
    """
    Displays a filtered table of agents based on their current room location.
    
    This function takes agent data, filters it by the specified room, and 
    renders the filtered data as a Streamlit dataframe. If the required
    'current_room' column is missing from the data, it displays a warning
    and shows the unfiltered data instead.
    
    Parameters:
    ----------
    agent_data : list or dict
        A collection of agent records that can be converted to a pandas DataFrame.
        Each agent record should be a dictionary containing agent information.
        Expected to have a 'current_room' column for filtering.
        
    room_filter : str
        The room identifier to filter agents by. Only agents with their
        'current_room' value matching this parameter will be displayed.
    
    Returns:
    -------
    None
        This function does not return a value; it renders UI elements
        directly to the Streamlit app.
    
    Side Effects:
    ------------
    - Renders a subheader with the room name to the Streamlit UI
    - Renders a dataframe of filtered agents to the Streamlit UI
    - Displays a warning if the 'current_room' column is missing
    
    Example:
    -------
    >>> agents = [
    ...     {"name": "Dr. Smith", "current_room": "101", "specialty": "Cardiology"},
    ...     {"name": "Dr. Jones", "current_room": "102", "specialty": "Neurology"},
    ...     {"name": "Dr. Lee", "current_room": "101", "specialty": "Oncology"}
    ... ]
    >>> show_agents(agents, "101")
    # Will display a table with Dr. Smith and Dr. Lee who are in room 101
    """
    # Convert agent data to DataFrame
    df = pd.DataFrame(agent_data)
    
    # Check if required column exists
    if "current_room" not in df.columns:
        st.warning("Missing 'current_room' column in agent data.")
        st.dataframe(df)
        return
    
    # Filter the dataframe by room
    filtered_df = df[df["current_room"] == room_filter]
    
    # Display results
    st.subheader(f"👩‍⚕️ Agents in Room: {room_filter}")
    st.dataframe(filtered_df, use_container_width=True)