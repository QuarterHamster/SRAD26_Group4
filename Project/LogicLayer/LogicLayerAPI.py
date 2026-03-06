from Models.Events import Event
from LogicLayer.AdminLogic import AdminLogic

def admin_event_review(event: Event, decision: bool):
    return AdminLogic().admin_event_review(event, decision)