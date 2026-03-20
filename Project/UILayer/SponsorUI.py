from Models.Enums import Event_status
from UILayer.ScreenOptions import ScreenOptions
from UILayer.UserUI import UserUI


class SponsorUI(UserUI):
    """Handles sponsor-facing screens."""

    ROLE_TITLE = "Sponsor"
    HOME_SCREEN = ScreenOptions.SPONSOR_HOME
    SEE_EVENTS_SCREEN = ScreenOptions.SPONSOR_SEE_EVENTS
    CREATE_EVENT_SCREEN = ScreenOptions.SPONSOR_CREATE_EVENT
    VIEW_ATTENDEES_SCREEN = ScreenOptions.SPONSOR_VIEW_ATTENDEES
    FILTER_EVENTS_SCREEN = ScreenOptions.SPONSOR_FILTER_EVENTS
    CAN_JOIN_EVENTS = False
    CAN_CREATE_PRIVATE_EVENTS = False

    def home_screen(self) -> ScreenOptions:
        sponsor = self._get_current_actor()
        self._utilityUI.show_box(
            "",
            "Sponsor Menu",
            f"Logged in as: {sponsor.organization}",
            "1. See Events",
            "2. Post Event As Sponsor",
            "3. View Attendees For Event",
            "4. Filter Events",
            "b. Log Out",
            "q. Quit",
            "",
        )

        response = self._utilityUI.user_input(["1", "2", "3", "4", "b", "q"])
        screen_map = {
            "1": self.SEE_EVENTS_SCREEN,
            "2": self.CREATE_EVENT_SCREEN,
            "3": self.VIEW_ATTENDEES_SCREEN,
            "4": self.FILTER_EVENTS_SCREEN,
            "b": ScreenOptions.LOGIN_SCREEN,
            "q": ScreenOptions.QUIT,
        }
        return screen_map[response]

    def create_event_screen(self) -> ScreenOptions:
        sponsor = self._get_current_actor()
        if str(getattr(sponsor, "user_status", "inactive")).lower() != "active":
            print("This sponsor is inactive and cannot post events.")
            self._utilityUI.pause()
            return self.HOME_SCREEN

        print(f"\nPosting event as: {sponsor.organization}")
        return self._run_create_event_screen(
            status=Event_status.PENDING,
            is_private_default=False,
            allow_private=False,
        )
