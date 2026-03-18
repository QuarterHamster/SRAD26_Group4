"""
Defines MenuOptions, an enum containing all valid navigation targets
used by the UI layer.
"""

from enum import StrEnum


class ScreenOptions(StrEnum):
    """
    Enum representing all available screens in the UI layer.

    Each value corresponds to a navigation target used by the
    application's screen-routing system.
    """

    START_SCREEN = "StartScreen"
    QUIT = "Quit"

    ACCEPT_REJECT_EVENT = "Accept_reject_event"
