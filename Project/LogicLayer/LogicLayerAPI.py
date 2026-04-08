from LogicLayer import EventLogic, CampusUserLogic
from LogicLayer.AdminLogic import AdminLogic
from Models.Event import Event
from Models.Campus_user import Campus_user

# Event Logic
event_logic = EventLogic.EventLogic()
def create_event(
    event_name,
    description,
    event_tags,
    branch_type,
    date_time,
    location,
    is_private,
    creator,
    status,
):
    return event_logic.create_event(
        event_name,
        description,
        event_tags,
        branch_type,
        date_time,
        location,
        is_private,
        status,
        creator,
    )

# Admin Logic
admin_logic = AdminLogic()

def admin_event_review(event: Event, decision: bool):
    return admin_logic.admin_event_review(event, decision)

# Campus user Logic
campus_user_logic = CampusUserLogic.CampusUserLogic()

def view_old_events(user: Campus_user):
    return campus_user_logic.view_old_events(user)

def view_favorite_events(user: Campus_user):
    return campus_user_logic.view_favorite_events(user)

def favorite_event(user: Campus_user, event: str):
    return campus_user_logic.favorite_event(user, event)

def unfavorite_event(user: Campus_user, event: str):
    return campus_user_logic.unfavorite_event(user, event)