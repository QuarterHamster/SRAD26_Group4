from Project.Models.User import User

class MainUI:
    def run(self):
        SCALE: int = 80

        def border(scale: int) -> str:
            return f"{('-' * SCALE)[:scale]}"

        def walls(scale: int, text: str = "") -> str:
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

        users: list[Users] = ...

        while True:
            print(border(SCALE))
            print(walls(SCALE))
            print(walls(SCALE, "1. Create Event"))
            print(walls(SCALE, "2. Accept/Reject Events As Admin"))
            print(walls(SCALE, "3. See Events"))

            response: str = user_input(["1", "2"])

            if response == "1":
                print(border(SCALE))

            break
