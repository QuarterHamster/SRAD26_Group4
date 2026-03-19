from datetime import datetime
from typing import Any

from LogicLayer import LogicLayerAPI
from Models.Enums import Branch_type, Event_status
from UILayer.Place_holder_data import campus_users, events
from UILayer.ScreenOptions import ScreenOptions
from UILayer.UtilityUI import UtilityUI


class UserUI:
    """Handles user-facing screens and shared event flows."""

    ROLE_TITLE = "User"
    HOME_SCREEN = ScreenOptions.USER_HOME
    SEE_EVENTS_SCREEN = ScreenOptions.USER_SEE_EVENTS
    CREATE_EVENT_SCREEN = ScreenOptions.USER_CREATE_EVENT
    VIEW_ATTENDEES_SCREEN = ScreenOptions.USER_VIEW_ATTENDEES
    FILTER_EVENTS_SCREEN = ScreenOptions.USER_FILTER_EVENTS

    def __init__(self) -> None:
        self._utilityUI = UtilityUI()
        self.SCALE = self._utilityUI.SCALE

    def home_screen(self) -> ScreenOptions:
        """
        Renders the user home screen and returns the next screen.

        :return: Next screen to navigate to.
        :rtype: ScreenOptions
        """
        self._utilityUI.show_box(
            "",
            f"{self.ROLE_TITLE} Menu",
            "1. See Events",
            "2. Create Event",
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

    def _prompt_user_id(self) -> str:
        """
        Prompts for a campus user id.

        :return: Entered user id.
        :rtype: str
        """
        return input("Enter your user id: ").strip()

    def _parse_event_datetime(self, raw_value: str) -> Any:
        """
        Parses a user-provided event date when possible.

        Falls back to the raw string if parsing fails so the UI stays
        compatible with older logic-layer signatures.

        :param raw_value: User-entered date value.
        :type raw_value: str
        :return: Parsed datetime or original string.
        :rtype: Any
        """
        cleaned_value = raw_value.strip()
        for fmt in ["%Y-%m-%d %H:%M", "%Y-%m-%d"]:
            try:
                return datetime.strptime(cleaned_value, fmt)
            except ValueError:
                continue
        return cleaned_value

    def _prompt_sort_choice(self) -> str:
        """
        Prompts for the event sorting method.

        :return: Sort key.
        :rtype: str
        """
        print("Sort events by:")
        print("1. Date")
        print("2. Name")
        print("3. Branch")

        response = self._utilityUI.user_input(["1", "2", "3"])
        sort_map = {"1": "date", "2": "name", "3": "branch"}
        return sort_map[response]

    def _get_visible_events(self, user_id: str) -> list:
        """
        Returns all events visible to the given user.

        :param user_id: Campus user id.
        :type user_id: str
        :return: Visible events.
        :rtype: list
        """
        return LogicLayerAPI.event_logic.get_visible_events(events, user_id)

    def _get_sorted_visible_events(self, user_id: str, sort_key: str) -> list:
        """
        Returns visible events sorted by the requested key.

        :param user_id: Campus user id.
        :type user_id: str
        :param sort_key: Sort field.
        :type sort_key: str
        :return: Visible sorted events.
        :rtype: list
        """
        event_logic = LogicLayerAPI.event_logic

        if hasattr(event_logic, "sort_visible_events"):
            return event_logic.sort_visible_events(events, user_id, sort_key)

        visible_events = self._get_visible_events(user_id)
        sort_functions = {
            "date": lambda event: getattr(event, "date_time", datetime.min),
            "name": lambda event: str(getattr(event, "event_name", "")).lower(),
            "branch": lambda event: str(getattr(event, "branch_type", "")).lower(),
        }
        return sorted(visible_events, key=sort_functions[sort_key])

    def _print_events(self, event_list: list, title: str) -> None:
        """
        Prints a short overview of events.

        :param event_list: Events to print.
        :type event_list: list
        :param title: Box title.
        :type title: str
        :return: None
        :rtype: None
        """
        self._utilityUI.show_box("", title, "")

        if len(event_list) == 0:
            print("No visible events.")
            return

        for index, event in enumerate(event_list, start=1):
            privacy = "Private" if event.is_private else "Public"
            tags_text = ", ".join(str(tag) for tag in getattr(event, "time_tags", []))
            event_date = getattr(event, "date_time", "")
            branch_type = getattr(event, "branch_type", "")

            if isinstance(event_date, datetime):
                event_date_text = event_date.strftime("%Y-%m-%d %H:%M")
            else:
                event_date_text = str(event_date)

            print(
                f"{index}. {event.event_name} [{privacy}] | {event_date_text} | "
                f"{branch_type} | Time tags: {tags_text}"
            )

    def _choose_visible_event(self, user_id: str, sort_key: str = "date"):
        """
        Lets the user pick one visible event.

        :param user_id: Campus user id.
        :type user_id: str
        :param sort_key: Sort field used when listing events.
        :type sort_key: str
        :return: Selected event or None.
        :rtype: object | None
        """
        visible_events = self._get_sorted_visible_events(user_id, sort_key)
        self._print_events(visible_events, "Events")

        if len(visible_events) == 0:
            return None

        print("b. Back")
        valid_options = [str(i) for i in range(1, len(visible_events) + 1)] + ["b"]
        selection = self._utilityUI.user_input(valid_options)

        if selection == "b":
            return None

        return visible_events[int(selection) - 1]

    def _create_event_through_logic(
        self,
        event_name: str,
        event_description: str,
        event_tags: list[str],
        date_time: Any,
        event_location: str,
        visibility: bool,
        creator_id: Any,
        status: Event_status = Event_status.PENDING,
    ):
        """
        Creates an event using the available logic-layer signature.

        :param event_name: Name of the event.
        :type event_name: str
        :param event_description: Description of the event.
        :type event_description: str
        :param event_tags: Event tags.
        :type event_tags: list[str]
        :param date_time: Event date value.
        :type date_time: Any
        :param event_location: Event location.
        :type event_location: str
        :param visibility: Whether event is public.
        :type visibility: bool
        :param creator_id: Creating user or sponsor id.
        :type creator_id: Any
        :param status: New event status.
        :type status: Event_status
        :return: Created event object.
        :rtype: object
        """
        creation_attempts = [
            (
                event_name,
                event_description,
                event_tags,
                Branch_type.REYKJAVÍK.value,
                date_time,
                event_location,
                visibility,
                status,
                creator_id,
            ),
            (
                event_name,
                event_description,
                event_tags,
                Branch_type.REYKJAVÍK.value,
                date_time,
                event_location,
                visibility,
                creator_id,
                self.ROLE_TITLE,
            ),
            (
                event_name,
                event_description,
                event_tags,
                Branch_type.REYKJAVÍK.value,
                date_time,
                event_location,
                visibility,
                creator_id,
            ),
        ]

        last_error = None
        for attempt in creation_attempts:
            try:
                return LogicLayerAPI.create_event(*attempt)
            except TypeError as error:
                last_error = error

        if last_error is not None:
            raise last_error

        raise RuntimeError("Unable to create event")

    def _send_event_details_placeholder(self, visible_events: list) -> None:
        """
        Placeholder flow for sending event details to a friend.

        :param visible_events: Currently listed visible events.
        :type visible_events: list
        :return: None
        :rtype: None
        """
        if len(visible_events) == 0:
            self._utilityUI.pause()
            return

        valid_event_numbers = [str(i) for i in range(1, len(visible_events) + 1)]
        selected_event_number = self._utilityUI.user_input(
            valid_event_numbers,
            prompt="Select the event number: ",
        )
        friend_user_id = input("Enter user id of the friend: ").strip()

        _ = visible_events[int(selected_event_number) - 1]
        _ = friend_user_id
        print("Event sent")

    def see_events_screen(self) -> ScreenOptions:
        """
        Shows visible events for the chosen user.

        :return: Next screen to navigate to.
        :rtype: ScreenOptions
        """
        user_id = self._prompt_user_id()
        sort_key = self._prompt_sort_choice()
        visible_events = self._get_sorted_visible_events(user_id, sort_key)
        self._print_events(visible_events, "Events")

        if len(visible_events) > 0:
            self._utilityUI.show_box(
                "",
                "1. Send event details to friend",
                "b. Go back to home screen",
                "",
            )
            response = self._utilityUI.user_input(["1", "b"])
            if response == "1":
                self._send_event_details_placeholder(visible_events)
        else:
            self._utilityUI.pause()
            return self.HOME_SCREEN

        self._utilityUI.pause()
        return self.HOME_SCREEN

    def create_event_screen(self) -> ScreenOptions:
        """
        Creates a new event.

        :return: Next screen to navigate to.
        :rtype: ScreenOptions
        """
        event_name = input("Event Name: ").strip()
        event_description = input("Event Description: ").strip()
        tags_input = input("Event Tags (comma separated): ").strip()
        raw_date_time = input("Event Date (YYYY-MM-DD HH:MM): ").strip()
        event_location = input("Event Location: ").strip()

        print("Should the event be private? Y/N")
        is_private = self._utilityUI.user_input(["y", "n"])
        visibility = is_private == "n"

        event_tags = [tag.strip() for tag in tags_input.split(",") if tag.strip() != ""]
        event_date = self._parse_event_datetime(raw_date_time)
        new_event = self._create_event_through_logic(
            event_name,
            event_description,
            event_tags,
            event_date,
            event_location,
            visibility,
            1,
        )
        events.append(new_event)

        print("\nEvent created successfully:\n")
        print(new_event)
        self._utilityUI.pause()
        return self.HOME_SCREEN

    def view_attendees_screen(self) -> ScreenOptions:
        """
        Shows attendees for a selected event.

        :return: Next screen to navigate to.
        :rtype: ScreenOptions
        """
        user_id = self._prompt_user_id()
        chosen_event = self._choose_visible_event(user_id)

        if chosen_event is None:
            return self.HOME_SCREEN

        if chosen_event.is_private:
            self._utilityUI.show_box(
                "",
                "This event is private. Attendees are hidden.",
                "",
            )
            self._utilityUI.pause()
            return self.HOME_SCREEN

        self._utilityUI.show_box(
            "",
            f"Attendees for: {chosen_event.event_name}",
            "",
        )

        attendees = getattr(chosen_event, "attendees", [])
        print(f"Total attendees: {len(attendees)}")

        if len(attendees) == 0:
            print("No attendees yet.")
        else:
            for attendee in attendees:
                print(f"- {attendee}")

        self._utilityUI.pause()
        return self.HOME_SCREEN

    def filter_events_screen(self) -> ScreenOptions:
        """
        Filters visible events by a time tag.

        :return: Next screen to navigate to.
        :rtype: ScreenOptions
        """
        user_id = self._prompt_user_id()
        time_tag = (
            input(
                "Enter a time tag (morning/afternoon/evening/night/weekday/weekend/month): "
            )
            .strip()
            .lower()
        )

        visible_events = self._get_visible_events(user_id)
        filtered_events = [
            event
            for event in visible_events
            if time_tag in [str(tag).lower() for tag in getattr(event, "time_tags", [])]
        ]

        self._print_events(filtered_events, f"Events with tag: {time_tag}")
        self._utilityUI.pause()
        return self.HOME_SCREEN
