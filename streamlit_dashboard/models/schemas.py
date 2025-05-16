from typing import Literal
from pydantic import BaseModel

class Agent(BaseModel):
    agent_id: str
    name: str
    current_room: str
    role: str
    status: Literal["On Duty", "Off Duty"]

class Patient(BaseModel):
    patient_id: str
    event: str
    location: str
    timestamp: str
    status: Literal["Active", "Idle", "Completed"]
