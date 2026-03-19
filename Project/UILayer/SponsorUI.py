from UILayer.ScreenOptions import ScreenOptions
from UILayer.UserUI import UserUI


class SponsorUI(UserUI):
    """Handles sponsor-facing screens."""

    ROLE_TITLE = "Sponsor"
    HOME_SCREEN = ScreenOptions.SPONSOR_HOME
    SEE_EVENTS_SCREEN = ScreenOptions.SPONSOR_SEE_EVENTS
    CREATE_EVENT_SCREEN = ScreenOptions.SPONSOR_CREATE_EVENT
    VIEW_ATTENDEES_SCREEN = ScreenOptions.SPONSOR_VIEW_ATTENDEES
    FILTER_EVENTS_SCREEN = ScreenOptions.SPONSOR_FILTER_EVENTS
