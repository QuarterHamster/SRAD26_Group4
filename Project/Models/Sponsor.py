from Models.User import User

class Sponsor(User):
    def __init__(self, user_id, name, email, user_status, account_period):
        super().__init__(user_id, name, email, user_status)
        self.account_period = account_period