from UILayer.Place_holder_data import campus_users, events
from Models.Campus_user import Campus_user
from Models.Enums import Event_status


class CampusUserLogic:
    def view_old_events(self, user: Campus_user) -> list[str]:
        """
        Looks through an list of events and returns a list of event names that the user has attended
        """
        past_events: list = []

        for i in events:
            if (i.status is Event_status.ENDED) and (user.email in i.attendees):
                past_events.append(i.event_name)

        if not past_events:
            return []
        return past_events

    def view_favorite_events(self, user: Campus_user) -> list[str]:
        """
        Looks through a list of events and returns a list of event names that the user has favorite
        :param user: Campus_user object
        :return: List of event names that the user has favorited
        """
        favorite_events: list = []
        for i in events:
            if i.event_name in user.favorites:
                favorite_events.append(i.event_name)

        if not favorite_events:
            return []
        return favorite_events

    def favorite_event(self, user: Campus_user, event: str):
        return user.add_favorite_event(event)

    def unfavorite_event(self, user: Campus_user, event: str):
        return user.remove_favorite_event(event)