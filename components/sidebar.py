import streamlit as st

def show_sidebar():
    st.sidebar.title("Filters")

    room = st.sidebar.selectbox("Filter by Room", ["All", "ICU", "Ward A", "Reception"])
    status = st.sidebar.selectbox("Filter by Status", ["All", "Active", "Idle", "Error"])

    return room, status
