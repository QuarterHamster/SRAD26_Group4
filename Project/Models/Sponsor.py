from Models.User import User

class Sponsor(User):
    def __init__(self, user_id, name, email, user_status, organization):
        super().__init__(user_id, name, email, user_status)
        self.organization = organization