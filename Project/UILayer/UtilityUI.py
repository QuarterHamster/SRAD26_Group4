class UtilityUI:
    """Holds utility function used widely in the UI layer"""

    def __init__(self) -> None:
        self.SCALE: int = 80

    def border(self, scale: int = 0) -> str:
        """
        Returns a horizontal border line.

        :param scale: Width of the border. Uses default scale when omitted.
        :type scale: int
        :return: Border string.
        :rtype: str
        """
        if scale <= 0:
            scale = self.SCALE
            
        return f"{('-' * self.SCALE)[:scale]}"

    def walls(self, scale: int = 0, text: str = "") -> str:
        """
        Returns a centered text line wrapped in vertical borders.

        :param scale: Width of the line. Uses default scale when omitted.
        :type scale: int
        :param text: Text to center within the borders.
        :type text: str
        :return: Formatted line surrounded by walls.
        :rtype: str
        """
        if scale <= 0:
            scale = self.SCALE

        if scale == 1:
            return "|"

        inner_width = scale - 2
        text = text[:inner_width]

        padding_left = (inner_width - len(text)) // 2
        padding_right = inner_width - len(text) - padding_left

        return "|" + " " * padding_left + text + " " * padding_right + "|"
    
    def show_box(self, *lines: str, scale: int = 0) -> None:
        """
        Prints a bordered text box.

        :param lines: Lines to print inside the box.
        :type lines: str
        :param scale: Width of the box.
        :type scale: int
        :return: None
        :rtype: None
        """
        if scale <= 0:
            scale = self.SCALE

        print(self.border(scale))
        for line in lines:
            print(self.walls(scale, line))
        print(self.border(scale))

    def user_input(self, valid: list[str], prompt: str = ">> ") -> str:
        """
        Prompts until the user enters a valid value.

        :param valid: Allowed inputs.
        :type valid: list[str]
        :param prompt: Prompt shown to the user.
        :type prompt: str
        :return: Validated user input.
        :rtype: str
        """
        while True:
            response: str = input(prompt).strip().lower()
            if response in valid:
                return response

            print("Not a valid option, try again")
        
    def pause(self, message: str = "\nPress Enter to continue...") -> None:
        """
        Pauses the flow until the user presses enter.

        :param message: Prompt shown while pausing.
        :type message: str
        :return: None
        :rtype: None
        """
        input(message)
