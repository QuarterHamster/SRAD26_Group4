from Models.User import User
from Models.Enums import School_type


class Campus_user(User):
    def __init__(self, user_id, name, email, user_status, user_type: School_type):
        super().__init__(user_id, name, email, user_status)
        self.user_type = user_type
        self.favorites = []

    def add_favorite_event(self, event_name) -> bool:
        """
        Adds an event to the favorites list, if the event is not already in the favorites.
        :param event_name: Event name to add
        :return: True if the event was added, False otherwise
        """
        favorite_event_name = str(event_name).strip()
        if event_name == "":
            return False

        if favorite_event_name not in self.favorites:
            self.favorites.append(favorite_event_name)
            return True

        return False

    def remove_favorite_event(self, event_name) -> bool:
        """
        Remove an event in favorites list, if the event is in the favorites.
        :param event_name: Event name to remove
        :return: True if the event was removed, False otherwise
        """
        favorite_event_name = str(event_name).strip()
        if event_name == "":
            return False

        if favorite_event_name in self.favorites:
            self.favorites.remove(favorite_event_name)
            return True

        return False


    def __str__(self): 
        return f"name: {self.name}\nuser type:{self.user_type.value}"
    
