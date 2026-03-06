from LogicLayer import EventLogic
from LogicLayer.AdminLogic import AdminLogic
from Models.Event import Event

event_logic = EventLogic.EventLogic()
def create_event(event_name, description, event_tags, branch_type, date_time, location, is_private, creator):
    return event_logic.create_event(event_name, description, event_tags, branch_type, date_time, location, is_private, creator)


def admin_event_review(event: Event, decision: bool):
    return AdminLogic().admin_event_review(event, decision)