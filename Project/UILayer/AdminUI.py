from UILayer.Place_holder_data import campus_users, events
from Models.Enums import School_type, Event_tags, Branch_type, Event_status
from Models.Event import Event
from LogicLayer import LogicLayerAPI
from UILayer.ScreenOptions import ScreenOptions
from UILayer.UtilityUI import UtilityUI


class AdminUI:
    def __init__(self):
        self._utilityUI = UtilityUI()
        self.SCALE = self._utilityUI.SCALE

    def start_screen(self) -> ScreenOptions:
        print(self._utilityUI.border(self.SCALE))
        print(self._utilityUI.walls(self.SCALE))
        print(self._utilityUI.walls(self.SCALE, "1. See Events"))
        print(self._utilityUI.walls(self.SCALE, "2. Create Event"))
        print(self._utilityUI.walls(self.SCALE, "3. Accept/Reject Events As Admin"))
        print(self._utilityUI.walls(self.SCALE, "4. View Attendees For Event"))
        print(self._utilityUI.walls(self.SCALE, "5. Filter Events By Time Tag"))
        print(self._utilityUI.walls(self.SCALE, "q. Quit"))
        print(self._utilityUI.walls(self.SCALE))

        response: str = self._utilityUI.user_input(["1", "2", "3", "4", "5", "q"])
        print(self._utilityUI.border())

        if response == "q":
            return ScreenOptions.QUIT

    def login_screen(self) -> ScreenOptions:
        pass



    def accept_reject_event(self) -> ScreenOptions:
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
        print(event, "\n")

        print("Accept or Decline the event")
        print("1. Accept")
        print("2. Decline")
        respond = input(">> ")

        if respond == "1":
            result = True

        elif respond == "2":
            result = False

        print(LogicLayerAPI.admin_event_review(event_obj, result))

        return ScreenOptions.START_SCREEN
