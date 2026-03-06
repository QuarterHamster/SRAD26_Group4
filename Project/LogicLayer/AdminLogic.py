from Models.Events import Event
from Models.Enums import Event_status


class AdminLogic():
    def admin_event_review(self, event: Event, decision: bool):
        """
        Takes in an event Object and the decision of the admin (True/False)

        Returns a message from the decision
        """        
        # If the decision is True
        if decision:
            event.status = Event_status.ACTIVE
            return "Event has been approved"
        
        # If the decision is False
        else: return "Event has been declined"

