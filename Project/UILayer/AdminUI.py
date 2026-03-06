from UILayer.Place_holder_data import campus_users, events
from Models.Enums import School_type, Event_tags, Branch_type, Event_status
from Models.Events import Event
from LogicLayer import LogicLayerAPI



class AdminUI:
    def __init__(self):
        pass


    def accept_reject_event(self):
        pending_events: list = []

        for event in events:
            if event.status is Event_status.PENDING:
                pending_events.append(event.event_name)
        

        print(pending_events)
        print("------------------------------------")
        selected_event = input("Select an event to review>> ")

        for event in events:
            if selected_event == event.event_name:
                selected_event = event
                event_obj = event
                break

        print("--- Event Details ---")
        print(event,"\n")

        print("Accept or Decline the event")
        print("1. Accept")
        print("2. Decline")
        respond = (input(">> "))

        if respond == "1":
            result = True

        elif respond == "2":
            result = False

        print(LogicLayerAPI.admin_event_review(event_obj, result))