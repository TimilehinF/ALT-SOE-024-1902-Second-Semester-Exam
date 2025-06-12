from pydantic import BaseModel
from datetime import datetime

class RegistrationCreate(BaseModel):
    user_id: int
    event_id: int

class Registration(BaseModel):
    id: int
    user_id: int
    event_id: int
    registration_date: datetime
    attended: bool = False

registrations = []