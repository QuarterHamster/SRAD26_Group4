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

    LOGIN_SCREEN = "LoginScreen"

    ADMIN_HOME = "AdminHomeScreen"
    ADMIN_SEE_EVENTS = "AdminSeeEvents"
    ADMIN_CREATE_EVENT = "AdminCreateEvent"
    ADMIN_ACCEPT_REJECT_EVENT = "AdminAcceptRejectEvent"
    ADMIN_VIEW_ATTENDEES = "AdminViewAttendees"
    ADMIN_FILTER_EVENTS = "AdminFilterEvents"

    USER_HOME = "UserHomeScreen"
    USER_SEE_EVENTS = "UserSeeEvents"
    USER_CREATE_EVENT = "UserCreateEvent"
    USER_VIEW_ATTENDEES = "UserViewAttendees"
    USER_FILTER_EVENTS = "UserFilterEvents"

    SPONSOR_HOME = "SponsorHomeScreen"
    SPONSOR_SEE_EVENTS = "SponsorSeeEvents"
    SPONSOR_CREATE_EVENT = "SponsorCreateEvent"
    SPONSOR_VIEW_ATTENDEES = "SponsorViewAttendees"
    SPONSOR_FILTER_EVENTS = "SponsorFilterEvents"

    QUIT = "Quit"
