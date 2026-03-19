from Models.Campus_user import Campus_user
from Models.Enums import School_type, Event_tags, Branch_type, Event_status
from Models.Event import Event
from datetime import datetime
from UILayer.Place_holder_data import events, campus_users
from UILayer.AdminUI import AdminUI
from UILayer.SponsorUI import SponsorUI
from UILayer.UserUI import UserUI
from UILayer.UtilityUI import UtilityUI
from LogicLayer import LogicLayerAPI
from UILayer.ScreenOptions import ScreenOptions


class MainUI:
    def __init__(self):
        self._utilityUI = UtilityUI()
        self._adminUI = AdminUI()
        self._userUI = UserUI()
        self._sponsorUI = SponsorUI()
        self.current_screen: ScreenOptions = ScreenOptions.LOGIN_SCREEN

        # Holds a map of corresponding screens
        self.screens = {
            ScreenOptions.LOGIN_SCREEN: self.login_screen,
            ScreenOptions.ADMIN_HOME: self._adminUI.home_screen,
            # ScreenOptions.ADMIN_SEE_EVENTS: self._adminUI.see_events_screen,
            # ScreenOptions.ADMIN_CREATE_EVENT: self._adminUI.create_event_screen,
            ScreenOptions.ADMIN_ACCEPT_REJECT_EVENT: self._adminUI.accept_reject_event,
            # ScreenOptions.ADMIN_VIEW_ATTENDEES: self._adminUI.view_attendees_screen,
            # ScreenOptions.ADMIN_FILTER_EVENTS: self._adminUI.filter_events_screen,
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

    def login_screen(self) -> ScreenOptions:
        """
        Renders the login screen and returns the next screen.

        :return: Next screen to navigate to.
        :rtype: ScreenOptions
        """
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
        screen_map = {
            "1": ScreenOptions.ADMIN_HOME,
            "2": ScreenOptions.USER_HOME,
            "3": ScreenOptions.SPONSOR_HOME,
            "q": ScreenOptions.QUIT,
        }
        return screen_map[response]

    def screen_not_exist_error(self) -> ScreenOptions:
        """
        A screen that shows up if the
        main ui state machine cant find any screen

        :return: The next screen to go to
        :rtype: ScreenOptions
        """

        print("Screen doesn't exist")
        input("Input anything to go back to start: ")
        return ScreenOptions.LOGIN_SCREEN

    def run(self) -> None:
        """Main application loop."""
        while True:
            if self.current_screen is ScreenOptions.QUIT:
                print("Quitting Program")
                break

            if self.screens.get(self.current_screen) is not None:
                self.current_screen = self.screens[self.current_screen]()
            else:
                self.current_screen = self.screen_not_exist_error()
