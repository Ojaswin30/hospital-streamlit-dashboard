import streamlit as st

def show_sidebar():
    """
    Renders a sidebar with filtering options and returns the selected filter values.
    
    This function creates a Streamlit sidebar containing filter controls that allow
    users to filter data by room location and status. It provides dropdown selectors
    for both filter types with predefined options.
    
    Parameters:
    ----------
    None
        This function doesn't take any parameters.
    
    Returns:
    -------
    tuple
        A tuple containing two elements:
        - room (str): The selected room filter value. Can be "All", "ICU", 
          "Ward A", or "Reception".
        - status (str): The selected status filter value. Can be "All", "Active", 
          "Idle", or "Error".
    
    Side Effects:
    ------------
    - Renders a sidebar title "Filters" to the Streamlit UI
    - Renders two selectbox widgets in the sidebar for room and status filtering
    
    Example:
    -------
    >>> selected_room, selected_status = show_sidebar()
    >>> print(f"User selected room: {selected_room}, status: {selected_status}")
    >>> if selected_room != "All":
    ...     # Apply room filtering to data
    ...     filtered_data = filter_by_room(data, selected_room)
    """
    # Create sidebar title
    st.sidebar.title("Filters")

    # Create room filter dropdown
    room = st.sidebar.selectbox("Filter by Room", ["All", "ICU", "Ward A", "Reception"])
    
    # Create status filter dropdown
    status = st.sidebar.selectbox("Filter by Status", ["All", "Active", "Idle", "Error"])

    # Return selected filter values
    return room, status