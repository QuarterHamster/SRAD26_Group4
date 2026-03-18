class UtilityUI:
    """Holds utility function used widely in the UI layer"""

    def __init__(self) -> None:
        self.SCALE: int = 80

    def border(self, scale: int = 0) -> str:
        if scale <= 0:
            scale = self.SCALE
            
        return f"{('-' * self.SCALE)[:scale]}"

    def walls(self, scale: int = 0, text: str = "") -> str:
        if scale <= 0:
            scale = self.SCALE

        if scale == 1:
            return "|"

        inner_width = scale - 2
        text = text[:inner_width]

        padding_left = (inner_width - len(text)) // 2
        padding_right = inner_width - len(text) - padding_left

        return "|" + " " * padding_left + text + " " * padding_right + "|"

    def user_input(self, valid: list[str]):
        while True:
            response: str = input(">> ").strip().lower()
            if response in valid:
                return response

            print("Not a valid option try again")
