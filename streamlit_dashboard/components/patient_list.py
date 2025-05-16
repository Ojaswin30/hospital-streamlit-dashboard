import pandas as pd
import streamlit as st

def show_patients(patient_data, status_filter):
    df = pd.DataFrame(patient_data)
    if "status" not in df.columns:
        st.warning("Missing 'status' column in patient data.")
        st.dataframe(df)
        return

    filtered_df = df[df["status"] == status_filter]
    st.subheader(f"🧑‍🦽 Patients with Status: {status_filter}")
    st.dataframe(filtered_df, use_container_width=True)
