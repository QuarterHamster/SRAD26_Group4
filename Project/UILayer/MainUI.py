from types import SimpleNamespace

from UILayer.AdminUI import AdminUI
from UILayer.Place_holder_data import campus_users, events, sponsors
from UILayer.ScreenOptions import ScreenOptions
from UILayer.SponsorUI import SponsorUI
from UILayer.UserUI import UserUI
from UILayer.UtilityUI import UtilityUI


class MainUI:
    """Coordinates screen routing across the UI layer."""

    def __init__(self) -> None:
        self._utilityUI = UtilityUI()
        self._adminUI = AdminUI()
        self._userUI = UserUI()
        self._sponsorUI = SponsorUI()
        self._adminUI.set_current_actor(
            SimpleNamespace(uuid="admin", name="Administrator")
        )
        self.current_screen: ScreenOptions = ScreenOptions.LOGIN_SCREEN

        self._seed_demo_event_state()

        self.screens = {
            ScreenOptions.LOGIN_SCREEN: self.login_screen,
            ScreenOptions.ADMIN_HOME: self._adminUI.home_screen,
            ScreenOptions.ADMIN_SEE_EVENTS: self._adminUI.see_events_screen,
            ScreenOptions.ADMIN_CREATE_EVENT: self._adminUI.create_event_screen,
            ScreenOptions.ADMIN_ACCEPT_REJECT_EVENT: self._adminUI.accept_reject_event,
            ScreenOptions.ADMIN_VIEW_ATTENDEES: self._adminUI.view_attendees_screen,
            ScreenOptions.ADMIN_FILTER_EVENTS: self._adminUI.filter_events_screen,
            ScreenOptions.ADMIN_MANAGE_SPONSORS: self._adminUI.manage_sponsors_screen,
            ScreenOptions.USER_HOME: self._userUI.home_screen,
            ScreenOptions.USER_SEE_EVENTS: self._userUI.see_events_screen,
            ScreenOptions.USER_CREATE_EVENT: self._userUI.create_event_screen,
            ScreenOptions.USER_VIEW_ATTENDEES: self._userUI.view_attendees_screen,
            ScreenOptions.USER_FILTER_EVENTS: self._userUI.filter_events_screen,
            ScreenOptions.SPONSOR_HOME: self._sponsorUI.home_screen,
            ScreenOptions.SPONSOR_SEE_EVENTS: self._sponsorUI.see_events_screen,
            ScreenOptions.SPONSOR_CREATE_EVENT: self._sponsorUI.create_event_screen,
            ScreenOptions.SPONSOR_VIEW_ATTENDEES: self._sponsorUI.view_attendees_screen,
            ScreenOptions.SPONSOR_FILTER_EVENTS: self._sponsorUI.filter_events_screen,
        }

    def _seed_demo_event_state(self) -> None:
        attendee_map = {
            0: [0, 1, 5],
            1: [2, 3],
            2: [4, 6, 7],
            4: [10],
        }

        for event_index, user_indexes in attendee_map.items():
            if event_index >= len(events):
                continue

            attendees = []
            for user_index in user_indexes:
                if user_index < len(campus_users):
                    attendees.append(campus_users[user_index].name)
            events[event_index].attendees = attendees

        if len(events) > 3:
            events[3].invite_user(6)
            events[3].invite_user(7)

    def login_screen(self) -> ScreenOptions:
        self._utilityUI.show_box(
            "",
            "Login",
            "1. Login as Admin",
            "2. Login as User",
            "3. Login as Sponsor",
            "q. Quit",
            "",
        )

        response = self._utilityUI.user_input(["1", "2", "3", "q"])
        if response == "1":
            return ScreenOptions.ADMIN_HOME

        if response == "2":
            selected_user = self._select_campus_user()
            if selected_user is None:
                return ScreenOptions.LOGIN_SCREEN

            self._userUI.set_current_actor(selected_user)
            return ScreenOptions.USER_HOME

        if response == "3":
            selected_sponsor = self._select_sponsor()
            if selected_sponsor is None:
                return ScreenOptions.LOGIN_SCREEN

            self._sponsorUI.set_current_actor(selected_sponsor)
            return ScreenOptions.SPONSOR_HOME

        return ScreenOptions.QUIT

    def _select_campus_user(self):
        active_users = [
            user
            for user in campus_users
            if str(getattr(user, "user_status", "")).lower() == "active"
        ]

        self._utilityUI.show_box(
            "",
            "Select User",
            "",
        )
        for index, user in enumerate(active_users, start=1):
            print(f"{index}. {user.name} [{user.user_type.value}]")
        print("b. Back")

        valid_options = [str(i) for i in range(1, len(active_users) + 1)] + ["b"]
        selection = self._utilityUI.user_input(valid_options)
        if selection == "b":
            return None

        return active_users[int(selection) - 1]

    def _select_sponsor(self):
        self._utilityUI.show_box(
            "",
            "Select Sponsor",
            "",
        )
        for index, sponsor in enumerate(sponsors, start=1):
            print(f"{index}. {sponsor.organization} [{sponsor.user_status}]")
        print("b. Back")

        valid_options = [str(i) for i in range(1, len(sponsors) + 1)] + ["b"]
        selection = self._utilityUI.user_input(valid_options)
        if selection == "b":
            return None

        sponsor = sponsors[int(selection) - 1]
        if str(getattr(sponsor, "user_status", "inactive")).lower() != "active":
            print("This sponsor does not currently have access to the system.")
            self._utilityUI.pause()
            return None

        return sponsor

    def screen_not_exist_error(self) -> ScreenOptions:
        print("Screen does not exist.")
        self._utilityUI.pause("Press Enter to go back to start: ")
        return ScreenOptions.LOGIN_SCREEN

    def run(self) -> None:
        while True:
            if self.current_screen is ScreenOptions.QUIT:
                print("Quitting program")
                break

            current_handler = self.screens.get(self.current_screen)
            if current_handler is None:
                self.current_screen = self.screen_not_exist_error()
                continue

            self.current_screen = current_handler()
