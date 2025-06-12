from pydantic import BaseModel
from typing import Optional, List

class EventCreate(BaseModel):
    title: str
    location: str
    date: str
    is_open: Optional[bool] = True

class EventUpdate(BaseModel):
    title: Optional[str] = None
    location: Optional[str] = None
    date: Optional[str] = None
    is_open: Optional[bool] = True

class Event(BaseModel):
    id: int
    title: str
    location: str
    date: str
    is_open: bool = True
    speaker_ids: List[int]

last_event_id = 0 
events = []
