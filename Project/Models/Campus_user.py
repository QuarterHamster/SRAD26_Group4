from User import User
from Enums import School_type

class Campus_user(User):
    def __init__(self, user_id, name, email, user_status, user_type: School_type):
        super().__init__(user_id, name, email, user_status)
        self.user_type = user_type

    def __str__(self): 
        return f"name: {self.name}\nuser type:{self.user_type.value}"
    

users = [
Campus_user(1,  "Anna Jónsdóttir",     "anna1@campus.is",  "active",   School_type.STUDENT),
Campus_user(2,  "Bjarni Sigurðsson",   "bjarni2@campus.is","active",   School_type.STUDENT),
Campus_user(3,  "Elín Guðmundsdóttir", "elin3@campus.is",  "active", School_type.STUDENT),
Campus_user(4,  "Kári Stefánsson",     "kari4@campus.is",  "active",   School_type.STUDENT),
Campus_user(5,  "Sara Magnúsdóttir",   "sara5@campus.is",  "active",   School_type.STUDENT),

Campus_user(6,  "Jón Þórsson",         "jon6@campus.is",   "active",   School_type.STAFF),
Campus_user(7,  "Helga Kristinsdóttir","helga7@campus.is", "active",   School_type.STAFF),
Campus_user(8,  "Arnar Pétursson",     "arnar8@campus.is", "active", School_type.STAFF),
Campus_user(9,  "Kristín Ólafsdóttir", "kristin9@campus.is","active",  School_type.STAFF),
Campus_user(10, "Davíð Einarsson",     "david10@campus.is","active",   School_type.STAFF),

Campus_user(11, "Ragnar Björnsson",    "ragnar11@campus.is","active",  School_type.STUDENT),
Campus_user(12, "Lilja Sigfúsdóttir",  "lilja12@campus.is","active",   School_type.STUDENT),
Campus_user(13, "Stefán Gíslason",     "stefan13@campus.is","active",School_type.STUDENT),
Campus_user(14, "María Björk",         "maria14@campus.is","active",   School_type.STUDENT),
Campus_user(15, "Óskar Þórðarson",     "oskar15@campus.is","active",   School_type.STUDENT),
]


print(users[1])