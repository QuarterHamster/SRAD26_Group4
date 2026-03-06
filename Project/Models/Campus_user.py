from Models.User import User
from Models.Enums import School_type


class Campus_user(User):
    def __init__(self, user_id, name, email, user_status, user_type: School_type):
        super().__init__(user_id, name, email, user_status)
        self.user_type = user_type

    def __str__(self): 
        return f"name: {self.name}\nuser type:{self.user_type.value}"
    
