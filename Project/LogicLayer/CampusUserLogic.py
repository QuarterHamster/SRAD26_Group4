from UILayer.Place_holder_data import campus_users, events
from Models.Campus_user import Campus_user
from Models.Enums import Event_status

class CampusUserLogic:
    def view_old_events(self, user: Campus_user)-> list[str]:
        """
        Looks through an list of events and returns a list of event names that the user has attended
        """
        past_events: list = []

        for i in events:
            if (i.status is Event_status.ENDED) and (user.email in i.attendees) :
                past_events.append(i.event_name)
        
        if not past_events: return "You have no past events"
        return past_events