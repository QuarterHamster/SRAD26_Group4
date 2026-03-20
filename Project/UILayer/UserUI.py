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
    CAN_JOIN_EVENTS = True
    CAN_CREATE_PRIVATE_EVENTS = True
    CAN_VIEW_PRIVATE_ATTENDEES = False

    def __init__(self) -> None:
        self._utilityUI = UtilityUI()
        self.SCALE = self._utilityUI.SCALE
        self.current_actor: Any | None = None

    def set_current_actor(self, actor: Any | None) -> None:
        self.current_actor = actor

    def clear_current_actor(self) -> None:
        self.current_actor = None

    def _get_current_actor(self) -> Any:
        if self.current_actor is None:
            raise RuntimeError("No active user is selected")

        return self.current_actor

    def _get_current_actor_id(self) -> str:
        return str(self._get_current_actor().uuid)

    def _get_current_actor_name(self) -> str:
        return str(self._get_current_actor().name)

    def home_screen(self) -> ScreenOptions:
        actor = self._get_current_actor()
        self._utilityUI.show_box(
            "",
            f"{self.ROLE_TITLE} Menu",
            f"Logged in as: {actor.name}",
            "1. See Events",
            "2. Create Event",
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

    def _parse_event_datetime(self, raw_value: str) -> datetime | None:
        cleaned_value = raw_value.strip()
        for fmt in ["%Y-%m-%d %H:%M", "%Y-%m-%d"]:
            try:
                return datetime.strptime(cleaned_value, fmt)
            except ValueError:
                continue

        return None

    def _prompt_event_datetime(self) -> datetime:
        while True:
            raw_value = input("Event Date (YYYY-MM-DD HH:MM): ").strip()
            parsed_value = self._parse_event_datetime(raw_value)
            if parsed_value is not None:
                return parsed_value

            print("Invalid date format. Use YYYY-MM-DD HH:MM or YYYY-MM-DD.")

    def _prompt_sort_choice(self) -> str:
        print("Sort events by:")
        print("1. Date")
        print("2. Name")
        print("3. Branch")

        response = self._utilityUI.user_input(["1", "2", "3"])
        sort_map = {"1": "date", "2": "name", "3": "branch"}
        return sort_map[response]

    def _prompt_branch_choice(self, allow_all: bool = False) -> str:
        print("Choose a branch:")
        branch_map = {}
        for index, branch in enumerate(Branch_type, start=1):
            print(f"{index}. {branch.value}")
            branch_map[str(index)] = branch.value

        valid_options = list(branch_map.keys())
        if allow_all:
            print("a. All branches")
            valid_options.append("a")

        response = self._utilityUI.user_input(valid_options)
        if response == "a":
            return "all"

        return branch_map[response]

    def _normalize_status(self, status: Any) -> str:
        return str(getattr(status, "value", status)).strip().lower()

    def _format_status(self, status: Any) -> str:
        raw_status = str(getattr(status, "value", status)).strip()
        return raw_status.title()

    def _get_visible_events(self, user_id: str | None = None) -> list:
        if user_id is None:
            user_id = self._get_current_actor_id()

        return LogicLayerAPI.event_logic.get_visible_events(events, user_id)

    def _get_sorted_visible_events(self, user_id: str | None, sort_key: str) -> list:
        if user_id is None:
            user_id = self._get_current_actor_id()

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
        self._utilityUI.show_box("", title, "")

        if len(event_list) == 0:
            print("No events found.")
            return

        for index, event in enumerate(event_list, start=1):
            privacy = "Private" if event.is_private else "Public"
            tags_text = ", ".join(str(tag) for tag in getattr(event, "time_tags", []))
            event_date = getattr(event, "date_time", "")
            branch_type = getattr(event, "branch_type", "")
            status_text = self._format_status(getattr(event, "status", ""))

            if isinstance(event_date, datetime):
                event_date_text = event_date.strftime("%Y-%m-%d %H:%M")
            else:
                event_date_text = str(event_date)

            print(
                f"{index}. {event.event_name} [{privacy}] | {status_text} | "
                f"{event_date_text} | {branch_type} | Time tags: {tags_text}"
            )

    def _choose_visible_event(self, sort_key: str = "date"):
        visible_events = self._get_sorted_visible_events(None, sort_key)
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
        branch_type: str,
        date_time: datetime,
        event_location: str,
        is_private: bool,
        creator_id: Any,
        status: Event_status = Event_status.PENDING,
    ):
        return LogicLayerAPI.create_event(
            event_name,
            event_description,
            event_tags,
            branch_type,
            date_time,
            event_location,
            is_private,
            creator_id,
            status,
        )

    def _prompt_invited_users(self) -> list[str]:
        current_user_id = self._get_current_actor_id()
        eligible_users = [
            user for user in campus_users if str(user.uuid) != current_user_id
        ]

        if len(eligible_users) == 0:
            return []

        print("Invite users to this private event:")
        for index, user in enumerate(eligible_users, start=1):
            print(f"{index}. {user.name} [{user.user_type.value}]")
        print("Press Enter to skip inviting anyone right now.")

        while True:
            raw_selection = input("Invite user numbers (comma separated): ").strip()
            if raw_selection == "":
                return []

            chosen_ids = []
            is_valid = True
            for item in raw_selection.split(","):
                normalized_item = item.strip()
                if not normalized_item.isdigit():
                    is_valid = False
                    break

                selected_index = int(normalized_item)
                if not 1 <= selected_index <= len(eligible_users):
                    is_valid = False
                    break

                chosen_ids.append(str(eligible_users[selected_index - 1].uuid))

            if is_valid:
                return list(dict.fromkeys(chosen_ids))

            print("Enter valid numbers separated by commas, or press Enter to skip.")

    def _is_joinable_event(self, event) -> bool:
        return LogicLayerAPI.event_logic.is_event_active(event)

    def _join_event_flow(self, visible_events: list) -> None:
        joinable_events = [
            event for event in visible_events if self._is_joinable_event(event)
        ]

        if len(joinable_events) == 0:
            print("There are no joinable events right now.")
            return

        print("Choose an event to join:")
        for index, event in enumerate(joinable_events, start=1):
            print(f"{index}. {event.event_name}")
        print("b. Back")

        valid_options = [str(i) for i in range(1, len(joinable_events) + 1)] + ["b"]
        selection = self._utilityUI.user_input(valid_options)
        if selection == "b":
            return

        chosen_event = joinable_events[int(selection) - 1]
        joined = LogicLayerAPI.event_logic.join_event(
            chosen_event,
            self._get_current_actor_name(),
        )

        if joined:
            print(f"You are now attending {chosen_event.event_name}.")
        else:
            print(f"You are already attending {chosen_event.event_name}.")

    def see_events_screen(self) -> ScreenOptions:
        sort_key = self._prompt_sort_choice()
        visible_events = self._get_sorted_visible_events(None, sort_key)
        self._print_events(visible_events, "Events")

        if len(visible_events) == 0:
            self._utilityUI.pause()
            return self.HOME_SCREEN

        if self.CAN_JOIN_EVENTS and any(self._is_joinable_event(event) for event in visible_events):
            self._utilityUI.show_box(
                "",
                "1. Join Event",
                "b. Go back to home screen",
                "",
            )
            response = self._utilityUI.user_input(["1", "b"])
            if response == "1":
                self._join_event_flow(visible_events)
        else:
            self._utilityUI.pause()
            return self.HOME_SCREEN

        self._utilityUI.pause()
        return self.HOME_SCREEN

    def _run_create_event_screen(
        self,
        *,
        status: Event_status = Event_status.PENDING,
        is_private_default: bool = False,
        allow_private: bool = True,
    ) -> ScreenOptions:
        event_name = input("Event Name: ").strip()
        event_description = input("Event Description: ").strip()
        tags_input = input("Event Tags (comma separated): ").strip()
        branch_type = self._prompt_branch_choice()
        event_date = self._prompt_event_datetime()
        event_location = input("Event Location: ").strip()

        is_private = is_private_default
        invited_user_ids: list[str] = []
        if allow_private:
            print("Should the event be private? Y/N")
            is_private = self._utilityUI.user_input(["y", "n"]) == "y"
            if is_private:
                invited_user_ids = self._prompt_invited_users()

        event_tags = [tag.strip() for tag in tags_input.split(",") if tag.strip() != ""]
        new_event = self._create_event_through_logic(
            event_name,
            event_description,
            event_tags,
            branch_type,
            event_date,
            event_location,
            is_private,
            self._get_current_actor_id(),
            status,
        )

        for invited_user_id in invited_user_ids:
            LogicLayerAPI.event_logic.invite_user(new_event, invited_user_id)

        events.append(new_event)

        print("\nEvent created successfully:\n")
        print(new_event)
        if is_private and len(invited_user_ids) > 0:
            print(f"Invited {len(invited_user_ids)} user(s) to this private event.")

        self._utilityUI.pause()
        return self.HOME_SCREEN

    def create_event_screen(self) -> ScreenOptions:
        return self._run_create_event_screen()

    def view_attendees_screen(self) -> ScreenOptions:
        chosen_event = self._choose_visible_event()
        if chosen_event is None:
            return self.HOME_SCREEN

        if (
            chosen_event.is_private
            and not self.CAN_VIEW_PRIVATE_ATTENDEES
            and str(chosen_event.creator) != self._get_current_actor_id()
        ):
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
        visible_events = self._get_visible_events()

        print("Filter events by:")
        print("1. Time tag")
        print("2. Branch")
        print("3. Time tag and branch")
        response = self._utilityUI.user_input(["1", "2", "3"])

        time_tag = None
        branch_filter = None
        if response in ["1", "3"]:
            time_tag = (
                input(
                    "Enter a time tag (morning/afternoon/evening/night/weekday/weekend/month): "
                )
                .strip()
                .lower()
            )

        if response in ["2", "3"]:
            branch_filter = self._prompt_branch_choice()

        filtered_events = visible_events
        if time_tag is not None:
            filtered_events = [
                event
                for event in filtered_events
                if time_tag in [str(tag).lower() for tag in getattr(event, "time_tags", [])]
            ]

        if branch_filter is not None:
            filtered_events = [
                event
                for event in filtered_events
                if str(getattr(event, "branch_type", "")).strip().lower()
                == branch_filter.lower()
            ]

        self._print_events(filtered_events, "Filtered Events")
        self._utilityUI.pause()
        return self.HOME_SCREEN
