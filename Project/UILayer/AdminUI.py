from UILayer.Place_holder_data import campus_users, events
from Models.Enums import School_type, Event_tags, Branch_type, Event_status
from Models.Event import Event
from LogicLayer import LogicLayerAPI
from UILayer.ScreenOptions import ScreenOptions
from UILayer.UtilityUI import UtilityUI
from UILayer.UserUI import UserUI


class AdminUI(UserUI):
    """Handles admin screens and admin-only actions."""

    ROLE_TITLE = "Admin"
    HOME_SCREEN = ScreenOptions.ADMIN_HOME
    SEE_EVENTS_SCREEN = ScreenOptions.ADMIN_SEE_EVENTS
    CREATE_EVENT_SCREEN = ScreenOptions.ADMIN_CREATE_EVENT
    VIEW_ATTENDEES_SCREEN = ScreenOptions.ADMIN_VIEW_ATTENDEES
    FILTER_EVENTS_SCREEN = ScreenOptions.ADMIN_FILTER_EVENTS
    ACCEPT_REJECT_EVENT_SCREEN = ScreenOptions.ADMIN_ACCEPT_REJECT_EVENT

    def home_screen(self) -> ScreenOptions:
        """
        Renders the admin home screen and returns the next screen.

        :return: Next screen to navigate to.
        :rtype: ScreenOptions
        """
        self._utilityUI.show_box(
            "",
            "Admin Menu",
            "1. See Events",
            "2. Create Event",
            "3. Accept/Reject Events",
            "4. View Attendees For Event",
            "5. Filter Events By Time Tag",
            "b. Log Out",
            "q. Quit",
            "",
        )

        response = self._utilityUI.user_input(["1", "2", "3", "4", "5", "b", "q"])
        screen_map = {
            "1": self.SEE_EVENTS_SCREEN,
            "2": self.CREATE_EVENT_SCREEN,
            "3": self.ACCEPT_REJECT_EVENT_SCREEN,
            "4": self.VIEW_ATTENDEES_SCREEN,
            "5": self.FILTER_EVENTS_SCREEN,
            "b": ScreenOptions.LOGIN_SCREEN,
            "q": ScreenOptions.QUIT,
        }
        return screen_map[response]

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
            return self.HOME_SCREEN

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
            return self.HOME_SCREEN

        event_obj = pending_events[int(selection) - 1]

        print("\n--- Event Details ---")
        print(event_obj)
        print("\nAccept or decline the event")
        print("1. Accept")
        print("2. Decline")
        print("b. Back")

        response = self._utilityUI.user_input(["1", "2", "b"])
        if response == "b":
            return self.HOME_SCREEN

        result = response == "1"
        print(LogicLayerAPI.admin_event_review(event_obj, result))
        self._utilityUI.pause()
        return self.HOME_SCREEN
