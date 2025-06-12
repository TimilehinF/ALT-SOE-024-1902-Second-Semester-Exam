from schemas.user import User, UserCreate, UserUpdate, users 

class UserService:

    @staticmethod
    def create_user(user: UserCreate):
        if any(u.email == user.email for u in users):
            return None  
        new_id = max([u.id for u in users], default=0) + 1
        user_obj = User(
            id=new_id,
            name=user.name,
            email=user.email,
            is_active= user.is_active,
        )
        users.append(user_obj)
        return user_obj
    
    @staticmethod 
    def amend_user(user_id: int, user_in: UserUpdate):
        for user in users:
            if user.id == user_id:
                if user_in.name is not None:
                    user.name = user_in.name
                if user_in.email is not None:
                    user.email = user_in.email
                if user_in.is_active is not None:
                    user.is_active = user_in.is_active
                return user
        return None 
    
    @staticmethod
    def get_specific_user(user_id:int):
        for user in users: 
            if user.id == user_id:
                return user
        return None 
    
    @staticmethod
    def remove_user(user_id:int):
        for user in users: 
            if user.id == user_id:
                users.remove(user)
                return user
        return None 

    @staticmethod
    def deactivate_user(user_id:int):
        for user in users: 
            if user.id == user_id: 
                user.is_active = False
                return user 
        return None 

user_service = UserService()

