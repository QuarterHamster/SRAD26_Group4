from Models.Campus_user import Campus_user
from Models.Enums import School_type, Event_tags, Branch_type, Event_status
from Models.Events import Event
from datetime import datetime
from UILayer.Place_holder_data import events, campus_users
from UILayer.AdminUI import AdminUI


class MainUI:
    def __init__(self):
        self._adminUI = AdminUI()

    def run(self):
        SCALE: int = 80

        def border(scale: int = SCALE) -> str:
            return f"{('-' * SCALE)[:scale]}"

        def walls(scale: int = SCALE, text: str = "") -> str:
            if scale <= 0:
                return ""
            if scale == 1:
                return "|"

            inner_width = scale - 2
            text = text[:inner_width]

            padding_left = (inner_width - len(text)) // 2
            padding_right = inner_width - len(text) - padding_left

            return "|" + " " * padding_left + text + " " * padding_right + "|"

        def user_input(valid: list[str]):
            while True:
                response: str = input(">> ").strip().lower()
                if response in valid:
                    return response

                print("Not a valid option try again")

        user_list = campus_users
        event_list = events

        while True:
            print(border(SCALE))
            print(walls(SCALE))
            print(walls(SCALE, "1. See Events"))
            print(walls(SCALE, "2. Create Event"))
            print(walls(SCALE, "3. Accept/Reject Events As Admin"))
            print(walls(SCALE, "q. Quit"))
            print(walls(SCALE))

            response: str = user_input(["1", "2", "3", "q"])
            print(border())

            if response == "1":
                pass

            if response == "2":
                pass

            if response == "3":
                self._adminUI.accept_reject_event()

            if response == "q":
                break
