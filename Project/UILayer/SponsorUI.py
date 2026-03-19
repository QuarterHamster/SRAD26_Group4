from UILayer.Place_holder_data import sponsors, events
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

    def home_screen(self) -> ScreenOptions:
        """
        Renders the sponsor home screen and returns the next screen.

        :return: Next screen to navigate to.
        :rtype: ScreenOptions
        """
        self._utilityUI.show_box(
            "",
            "Sponsor Menu",
            "1. See Events",
            "2. Post Event As Sponsor",
            "3. View Attendees For Event",
            "4. Filter Events By Time Tag",
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
        """
        Lets a sponsor post an event.

        :return: Next screen to navigate to.
        :rtype: ScreenOptions
        """
        self._utilityUI.show_box(
            "",
            "Sponsors",
            "",
        )

        if len(sponsors) == 0:
            print("No sponsors available.")
            self._utilityUI.pause()
            return self.HOME_SCREEN

        for sponsor in sponsors:
            sponsor_name = getattr(sponsor, "organization", getattr(sponsor, "name", ""))
            sponsor_status = getattr(sponsor, "user_status", "unknown")
            print(f"[{sponsor.uuid}] {sponsor_name} [{sponsor_status}]")
        print("b. Back")

        valid_options = [str(sponsor.uuid).lower() for sponsor in sponsors] + ["b"]
        sponsor_id = self._utilityUI.user_input(
            valid_options,
            prompt="Enter your sponsor ID: ",
        )

        if sponsor_id == "b":
            return self.HOME_SCREEN

        sponsor = next((item for item in sponsors if str(item.uuid).lower() == sponsor_id), None)
        if sponsor is None:
            print("Sponsor not found.")
            self._utilityUI.pause()
            return self.HOME_SCREEN

        if str(getattr(sponsor, "user_status", "inactive")).lower() != "active":
            print("This sponsor is inactive and cannot post events.")
            self._utilityUI.pause()
            return self.HOME_SCREEN

        sponsor_name = getattr(sponsor, "organization", getattr(sponsor, "name", "Sponsor"))
        print(f"\nPosting event as: {sponsor_name}")
        event_name = input("Event Name: ").strip()
        event_description = input("Event Description: ").strip()
        tags_input = input("Event Tags (comma separated): ").strip()
        raw_date_time = input("Event Date (YYYY-MM-DD HH:MM): ").strip()
        event_location = input("Event Location: ").strip()

        event_tags = [tag.strip() for tag in tags_input.split(",") if tag.strip() != ""]
        event_date = self._parse_event_datetime(raw_date_time)
        new_event = self._create_event_through_logic(
            event_name,
            event_description,
            event_tags,
            event_date,
            event_location,
            False,
            sponsor.uuid,
        )
        events.append(new_event)

        self._utilityUI.show_box(
            "",
            "Event submitted for admin review!",
            "",
        )
        print(new_event)
        self._utilityUI.pause()
        return self.HOME_SCREEN
