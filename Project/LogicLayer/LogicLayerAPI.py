from LogicLayer import EventLogic

event_logic = EventLogic.EventLogic()
def create_event(event_name, description, event_tags, branch_type, date_time, location, is_private, creator):
    return event_logic.create_event(event_name, description, event_tags, branch_type, date_time, location, is_private, creator)