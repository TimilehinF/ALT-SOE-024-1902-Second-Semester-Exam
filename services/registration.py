from fastapi import HTTPException, status
from datetime import datetime
from schemas.registration import Registration, RegistrationCreate, registrations 
from schemas.user import users
from schemas.event import events
from services.user import user_service
from services.event import event_service

class RegistrationService:

    @staticmethod
    def create_registration(reg:RegistrationCreate):
        user = user_service.get_specific_user(reg.user_id)
        if not user: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        event = event_service.get_specific_event(reg.event_id)
        if not event: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
        if not user.is_active:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is inactive")
        if not event.is_open:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Event is closed")
        if any(r.user_id == reg.user_id and r.event_id == reg.event_id for r in registrations):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already registered for this event")
        
        registration = Registration(
            id=len(registrations) + 1,
            user_id = reg.user_id,
            event_id = reg.event_id,
            registration_date = datetime.now(),
        )
        registrations.append(registration)
        return registration
    
    @staticmethod
    def set_attendance(reg_id:int):
        for reg in registrations: 
            if reg.id == reg_id:
                reg.attended = True 
                return reg
        return None 

    @staticmethod
    def get_user_registrations(user_id:int):
        user = user_service.get_specific_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user_regs = [reg for reg in registrations if reg.user_id == user_id]
        return user_regs if user_regs else None


registration_service = RegistrationService()