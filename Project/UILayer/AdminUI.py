from UILayer.Place_holder_data import campus_users, events
from Models.Enums import School_type, Event_tags, Branch_type, Event_status
from Models.Event import Event
from LogicLayer import LogicLayerAPI
from UILayer.ScreenOptions import ScreenOptions
from UILayer.UtilityUI import UtilityUI
from UILayer.UserUI import UserUI


class AdminUI:
    """Admin-only screens and actions."""

    def __init__(self) -> None:
        self._utilityUI = UtilityUI()
        self.SCALE = self._utilityUI.SCALE

    def home_screen(self) -> ScreenOptions:
        input("You are at admin home screen")

        return ScreenOptions.LOGIN_SCREEN

    def accept_reject_event(self) -> ScreenOptions:
        """
        Lets an admin review pending events.

        :return: The next screen to navigate to.
        :rtype: ScreenOptions
        """
        pending_events = [
            event for event in events if event.status is Event_status.PENDING
        ]

        if len(pending_events) == 0:
            self._utilityUI.show_box(
                "",
                "No pending events to review.",
                "",
                scale=self.SCALE,
            )
            self._utilityUI.pause()
            return ScreenOptions.LOGIN_SCREEN

        self._utilityUI.show_box(
            "",
            "Pending Events",
            "",
            scale=self.SCALE,
        )
        for index, event in enumerate(pending_events, start=1):
            print(f"{index}. {event.event_name}")
        print("b. Back")

        valid_options = [str(i) for i in range(1, len(pending_events) + 1)] + ["b"]
        selection = self._utilityUI.user_input(valid_options)

        if selection == "b":
            return ScreenOptions.LOGIN_SCREEN

        event_obj = pending_events[int(selection) - 1]

        print("\n--- Event Details ---")
        print(event_obj)
        print("\nAccept or decline the event")
        print("1. Accept")
        print("2. Decline")
        print("b. Back")

        response = self._utilityUI.user_input(["1", "2", "b"])
        if response == "b":
            return ScreenOptions.LOGIN_SCREEN

        result = response == "1"
        print(LogicLayerAPI.admin_event_review(event_obj, result))
        self._utilityUI.pause()
        return ScreenOptions.LOGIN_SCREEN
