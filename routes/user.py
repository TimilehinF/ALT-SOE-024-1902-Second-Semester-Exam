from fastapi import APIRouter, HTTPException, status
from schemas.user import User, UserCreate, UserUpdate, users
from services.user import user_service 

user_router = APIRouter()

@user_router.get("/", status_code = status.HTTP_200_OK)
def get_user():
    return users 

@user_router.get("/{user_id}/", status_code = status.HTTP_200_OK )
def get_user_by_id(user_id:int):
    user = user_service.get_specific_user(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
    return user 

@user_router.post("/", status_code = status.HTTP_201_CREATED)
def add_user(user: UserCreate):
    user = user_service.create_user(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User email already exists")
    return { "message": "User Created Successfully",
            "data": user}

@user_router.put("/{user_id}/",status_code = status.HTTP_200_OK)
def update_user(user_id:int, user_in:UserUpdate):
    user = user_service.amend_user(user_id, user_in)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
    return { "message": "User Updated Successfully",
            "data": user}

@user_router.delete("/{user_id}", status_code = status.HTTP_200_OK)
def delete_user(user_id:int):
    user = user_service.remove_user(user_id)
    if not user: 
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
    return {"message": f"User with id: {user_id} deleted successfully"}
            
@user_router.patch("/{user_id}",status_code = status.HTTP_200_OK)
def deactivate_user(user_id:int):
    user = user_service.deactivate_user(user_id)
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
    return {"message": "User successfully deactivated", "data": user}



