from fastapi import APIRouter, HTTPException, status
from schemas.registration import Registration, RegistrationCreate, registrations 
from services.registration import registration_service

registration_router = APIRouter()

@registration_router.get("/", status_code = status.HTTP_200_OK)
def get_all_registrations():
    return registrations

@registration_router.get("/{user_id}", status_code = status.HTTP_200_OK)
def get_user_registrations(user_id:int):
    regs = registration_service.get_user_registrations(user_id)
    if not regs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User has not registered for any events")
    return {"message": "User registrations", "data": regs}

@registration_router.post("/", status_code = status.HTTP_201_CREATED)
def add_registration(reg:RegistrationCreate):
    reg = registration_service.create_registration(reg)
    return { "message": "User has registered successfully",
            "data": reg}

@registration_router.patch("/{reg_id}", status_code = status.HTTP_200_OK)
def mark_attendance(reg_id:int):
    reg = registration_service.set_attendance(reg_id)
    if not reg: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registration not found")
    return {"message": f"User has attended event {reg.event_id}", "data": reg}

