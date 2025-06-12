from fastapi import HTTPException, status
from schemas.event import Event, EventCreate, EventUpdate, events, last_event_id
from schemas.speaker import speakers 

class EventService:

    @staticmethod
    def create_event(event:EventCreate):
        global last_event_id
        for e in events: 
            if e.title == event.title and e.location == event.location and e.date == event.date:
                return None 
        all_speaker_ids = [s.id for s in speakers]
        last_event_id += 1
        event_obj = Event(
            id = last_event_id,
            title = event.title, 
            location = event.location,
            date = event.date,
            is_open = event.is_open,
            speaker_ids=all_speaker_ids,
        )
        events.append(event_obj)
        return event_obj
    
    @staticmethod
    def amend_event(event_id:int, event_in:EventUpdate):
        for event in events: 
            if event.id == event_id:
                if event_in.title is not None:
                    event.title = event_in.title
                if event_in.location is not None:
                    event.location = event_in.location
                if event_in.date is not None:
                    event.date = event_in.date
                if event_in.is_open is not None:
                    event.is_open = event_in.is_open
                return event
        return None 
    
    @staticmethod
    def get_specific_event(event_id:int):
        for event in events: 
            if event.id == event_id:
                return event
        return None 
    
    @staticmethod
    def remove_event(event_id:int):
        for event in events:
            if event.id == event_id:
                events.remove(event)
                return event 
        return None 

    @staticmethod
    def close_event(event_id:int):
        for event in events: 
            if event.id == event_id: 
                event.is_open = False
                return event 
        return None 
    
event_service = EventService()
