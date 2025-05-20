#Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
#..\venv\Scripts\Activate

import pandas as pd
import streamlit as st

def show_patients(patient_data, status_filter):
    """
    Displays a filtered table of patients based on their current status.
    
    This function takes patient data, filters it by the specified status, and 
    renders the filtered data as a Streamlit dataframe. If the required
    'status' column is missing from the data, it displays a warning
    and shows the unfiltered data instead.
    
    Parameters:
    ----------
    patient_data : list or dict
        A collection of patient records that can be converted to a pandas DataFrame.
        Each patient record should be a dictionary containing patient information.
        Expected to have a 'status' column for filtering (e.g., 'critical', 'stable').
        
    status_filter : str
        The status value to filter patients by. Only patients with their
        'status' value matching this parameter will be displayed.
    
    Returns:
    -------
    None
        This function does not return a value; it renders UI elements
        directly to the Streamlit app.
    
    Side Effects:
    ------------
    - Renders a subheader with the status description to the Streamlit UI
    - Renders a dataframe of filtered patients to the Streamlit UI
    - Displays a warning if the 'status' column is missing
    
    Example:
    -------
    >>> patients = [
    ...     {"name": "John Doe", "status": "critical", "room": "101"},
    ...     {"name": "Jane Smith", "status": "stable", "room": "102"},
    ...     {"name": "Robert Johnson", "status": "critical", "room": "103"}
    ... ]
    >>> show_patients(patients, "critical")
    # Will display a table with John Doe and Robert Johnson who have critical status
    """
    # Convert patient data to DataFrame
    df = pd.DataFrame(patient_data)
    
    # Check if required column exists
    if "status" not in df.columns:
        st.warning("Missing 'status' column in patient data.")
        st.dataframe(df)
        return
    
    # Filter the dataframe by status
    filtered_df = df[df["status"] == status_filter]
    
    # Display results
    st.subheader(f"🧑‍🦽 Patients with Status: {status_filter}")
    st.dataframe(filtered_df, use_container_width=True)