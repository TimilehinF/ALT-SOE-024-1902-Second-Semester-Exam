from fastapi import APIRouter, HTTPException, status
from schemas.event import Event, EventCreate, EventUpdate, events 
from services.event import event_service

event_router = APIRouter()

@event_router.get("/", status_code = status.HTTP_200_OK)
def get_event():
    return events

@event_router.get("/{event_id}",status_code = status.HTTP_200_OK)
def get_event_by_id(event_id:int):
    event = event_service.get_specific_event(event_id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event does not exist")
    return event 

@event_router.post("/",status_code = status.HTTP_201_CREATED)
def add_event(event:EventCreate):
    event = event_service.create_event(event)
    if not event:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Event already exists")
    return {"message": "Event successfully created", "data": event}

@event_router.put("/{event_id}", status_code = status.HTTP_200_OK)
def update_event(event_id: int, event_in: EventUpdate):
    event = event_service.amend_event(event_id, event_in)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event does not exist")
    return { "message": "Event Updated Successfully",
            "data": event}

@event_router.delete("/{event_id}", status_code = status.HTTP_200_OK)
def delete_event(event_id:int):
    event = event_service.remove_event(event_id)
    if not event: 
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event does not exist")
    return {"message": f"Event with id: {event_id} deleted successfully"}

@event_router.patch("/{event_id}",status_code = status.HTTP_200_OK)
def deactivate_event(event_id:int):
    event = event_service.close_event(event_id)
    if not event: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event does not exist")
    return {"message": "Event successfully deactivated", "data": event}