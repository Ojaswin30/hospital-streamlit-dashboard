# hospital-streamlit-dashboard
 Streamlit dashboard for visualizing the Agent Hospital Simulacrum. Tracks patient journeys, mutations, diagnostics, and agent actions in real time. Built for Winniio/LifeAtlas. Modular, extensible, and designed for internal use with strict NDA/IP protection.


# Healthcare Dashboard System

## Project Overview
This Streamlit-based dashboard application provides real-time monitoring and management of healthcare providers and patients in a medical facility. The system delivers at-a-glance visibility of staff locations, patient statuses, and room allocations to support efficient healthcare operations.

## Project Structure

```
streamlit_dashboard/
├── components/
│   ├── __pycache__/
│   ├── agent_table.py
│   ├── patient_list.py
│   └── sidebar.py
├── models/
│   └── schemas.py
├── shared_data/
│   ├── agents.json
│   ├── event_log.json
│   └── patient.json
├── utils/
│   ├── __pycache__/
│   ├── data_handler.py
│   ├── data_loader.py
│   └── phaser_data_handler.py
├── app.py
└── status_bar.py
```

**Note:** The patient status dashboard component is currently under development and yet to be connected to the main codebase.
```

**Note:** The patient status dashboard component is currently under development and yet to be connected to the main codebase.
```

## Libraries and Dependencies
The application is built using:
* **Streamlit (`streamlit`)**: For creating the interactive web interface
* **Pandas (`pandas`)**: For data manipulation, filtering and analysis
* **Matplotlib (`matplotlib.pyplot`, `matplotlib.patches`)**: For data visualization and custom graphical elements
* **JSON (`json`)**: For parsing and handling JSON formatted data
* **Time (`time`)**: For timing operations and handling time-based functionality
* **Pydantic (`pydantic`)**: For data validation and schema definition

## Key Features
* **Real-time Staff Tracking**: Monitor healthcare providers' locations and availability
* **Patient Status Dashboard**: Track patient statuses, locations, and events
* **Customizable Filtering**: Filter views by room, status, and other parameters
* **Data Validation**: Enforce data integrity with Pydantic models
* **Responsive Layout**: Adapts to different screen sizes for desktop and tablet use

## Technical Implementation
The modular architecture separates concerns into components (UI elements), models (data structures), and utilities (data operations), making the codebase maintainable and extensible.

## Use Cases
* **Nurse Stations**: Monitor which providers are assigned to each area
* **Hospital Administration**: Track patient distribution and staff allocation
* **Shift Changes**: Quickly understand the current state of the facility
* **Emergency Response**: Identify available staff in critical situations

This dashboard enhances hospital operations by providing clear visibility into the current state of both healthcare providers and patients, supporting better decision-making and resource allocation in time-sensitive healthcare environments.