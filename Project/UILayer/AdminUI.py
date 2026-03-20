from LogicLayer import LogicLayerAPI
from Models.Enums import Event_status
from UILayer.Place_holder_data import events, sponsors
from UILayer.ScreenOptions import ScreenOptions
from UILayer.UserUI import UserUI


class AdminUI(UserUI):
    """Admin-only screens and actions."""

    ROLE_TITLE = "Admin"
    HOME_SCREEN = ScreenOptions.ADMIN_HOME
    SEE_EVENTS_SCREEN = ScreenOptions.ADMIN_SEE_EVENTS
    CREATE_EVENT_SCREEN = ScreenOptions.ADMIN_CREATE_EVENT
    VIEW_ATTENDEES_SCREEN = ScreenOptions.ADMIN_VIEW_ATTENDEES
    FILTER_EVENTS_SCREEN = ScreenOptions.ADMIN_FILTER_EVENTS
    MANAGE_SPONSORS_SCREEN = ScreenOptions.ADMIN_MANAGE_SPONSORS
    CAN_JOIN_EVENTS = False
    CAN_VIEW_PRIVATE_ATTENDEES = True

    def home_screen(self) -> ScreenOptions:
        self._utilityUI.show_box(
            "",
            "Admin Menu",
            "1. See Events",
            "2. Create Event",
            "3. Accept Or Reject Events",
            "4. View Attendees For Event",
            "5. Filter Events",
            "6. Grant Sponsor Permissions",
            "b. Log Out",
            "q. Quit",
            "",
        )

        response = self._utilityUI.user_input(["1", "2", "3", "4", "5", "6", "b", "q"])
        screen_map = {
            "1": self.SEE_EVENTS_SCREEN,
            "2": self.CREATE_EVENT_SCREEN,
            "3": ScreenOptions.ADMIN_ACCEPT_REJECT_EVENT,
            "4": self.VIEW_ATTENDEES_SCREEN,
            "5": self.FILTER_EVENTS_SCREEN,
            "6": self.MANAGE_SPONSORS_SCREEN,
            "b": ScreenOptions.LOGIN_SCREEN,
            "q": ScreenOptions.QUIT,
        }
        return screen_map[response]

    def _get_visible_events(self, user_id: str | None = None) -> list:
        return list(events)

    def _get_sorted_visible_events(self, user_id: str | None, sort_key: str) -> list:
        sort_functions = {
            "date": lambda event: getattr(event, "date_time"),
            "name": lambda event: str(getattr(event, "event_name", "")).lower(),
            "branch": lambda event: str(getattr(event, "branch_type", "")).lower(),
        }
        return sorted(list(events), key=sort_functions[sort_key])

    def _event_needs_review(self, event) -> bool:
        status = self._normalize_status(getattr(event, "status", ""))
        return status in {"pending", "proposed"}

    def create_event_screen(self) -> ScreenOptions:
        return self._run_create_event_screen(status=Event_status.ACTIVE)

    def accept_reject_event(self) -> ScreenOptions:
        pending_events = [event for event in events if self._event_needs_review(event)]

        if len(pending_events) == 0:
            self._utilityUI.show_box(
                "",
                "No pending events to review.",
                "",
            )
            self._utilityUI.pause()
            return self.HOME_SCREEN

        self._utilityUI.show_box(
            "",
            "Pending Events",
            "",
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

    def manage_sponsors_screen(self) -> ScreenOptions:
        self._utilityUI.show_box(
            "",
            "Sponsors",
            "",
        )

        if len(sponsors) == 0:
            print("No sponsors available.")
            self._utilityUI.pause()
            return self.HOME_SCREEN

        for index, sponsor in enumerate(sponsors, start=1):
            sponsor_name = getattr(sponsor, "organization", getattr(sponsor, "name", ""))
            sponsor_status = getattr(sponsor, "user_status", "unknown")
            print(f"{index}. {sponsor_name} [{sponsor_status}]")
        print("b. Back")

        valid_options = [str(i) for i in range(1, len(sponsors) + 1)] + ["b"]
        selection = self._utilityUI.user_input(valid_options)

        if selection == "b":
            return self.HOME_SCREEN

        sponsor = sponsors[int(selection) - 1]
        sponsor_name = getattr(sponsor, "organization", getattr(sponsor, "name", "Sponsor"))
        current_status = str(getattr(sponsor, "user_status", "inactive")).strip().lower()
        next_status = "inactive" if current_status == "active" else "active"
        sponsor.user_status = next_status

        print(f"{sponsor_name} is now {next_status}.")
        self._utilityUI.pause()
        return self.HOME_SCREEN
