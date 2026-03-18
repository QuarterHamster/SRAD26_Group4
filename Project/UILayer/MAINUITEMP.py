from Models.Campus_user import Campus_user
from Models.Enums import School_type, Event_tags, Branch_type, Event_status
from Models.Event import Event
from datetime import datetime
from UILayer.Place_holder_data import events, campus_users
from UILayer.AdminUI import AdminUI
from LogicLayer import LogicLayerAPI
from UILayer.ScreenOptions import ScreenOptions


class MainUI:
    def __init__(self):
        self._adminUI = AdminUI()
        self.current_screen: ScreenOptions = ScreenOptions.START_SCREEN

        # Holds a map of corresponding screens
        self.screens = {
            ScreenOptions.START_SCREEN: self._adminUI.start_screen,
        }

    def screen_not_exist_error(self) -> ScreenOptions:
        """
        A screen that shows up if the
        main ui state machine cant find any screen

        :return: The next screen to go to
        :rtype: ScreenOptions
        """

        print("Screen doesn't exist")
        input("Input anything to go back to start: ")
        return ScreenOptions.START_SCREEN

    def run(self) -> None:
        """
        Main application loop.

        Handles user input and transitions to the appropriate screen.
        """

        while True:
            if self.screens.get(self.current_screen) is not None:
                self.current_screen = self.screens[self.current_screen]()

            # stop when quit
            elif self.current_screen is ScreenOptions.QUIT:
                print("Quitting Program")
                break

            else:
                self.current_screen = self.screen_not_exist_error()
