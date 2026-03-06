from Models.Events import Event
from Models.Enums import Event_status


class AdminLogic():
    def admin_event_review(self, event: Event, decision: bool):
        """
        Takes in an event Object and the decision of the admin (True/False)
        """
        
        # If the decision is True
        if decision:
            event.status = Event_status.ACTIVE
        
        # If the decision is False
        else: del(event)

