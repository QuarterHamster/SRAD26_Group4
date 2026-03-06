class User:
    """
    A generalized class to represent a user

    Stores name, email and user status

    :param uuid: Unique identifier for the player
    :type uuid: str
    :param name: Full name of the user
    :type name: str
    :param email: Email of the user
    :type email: str
    :param user_status: Status of the user
    :type user_status: boolean
    """
    def __init__(self, uuid, name, email, user_status):
        self.uuid = uuid
        self.name = name
        self.email = email
        self.user_status = user_status
