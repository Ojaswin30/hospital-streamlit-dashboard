from typing import Literal
from pydantic import BaseModel

class Agent(BaseModel):
    """
    Represents a healthcare agent.

    Attributes:
        agent_id: Unique identifier for the agent.
        name: Full name of the agent.
        current_room: Current location of the agent.
        role: Job role of the agent (e.g., Doctor, Nurse).
        status: Working status, either "On Duty" or "Off Duty".
    """
    agent_id: str
    name: str
    current_room: str
    role: str
    status: Literal["On Duty", "Off Duty"]


class Patient(BaseModel):
    """
    Represents a patient event in the healthcare system.

    Attributes:
        patient_id: Unique identifier for the patient.
        event: Description of the patient-related event.
        location: Location of the patient or event.
        timestamp: Event time as a string.
        status: Status of the event, one of "Active", "Idle", or "Completed".
    """
    patient_id: str
    event: str
    location: str
    timestamp: str
    status: Literal["Active", "Idle", "Completed"]
