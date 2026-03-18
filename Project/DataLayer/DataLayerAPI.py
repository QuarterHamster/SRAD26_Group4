from Models import Event, Administrator, Sponsor
from DataLayer import EventIO, AdminIO, SponsorIO
# Event API
def store_event(new_event):
    """Stores new events in a JSON file to be fetched later.

    :param new_event:
        The event object to store.
    :type new_event: Event
    """
    return EventIO.store_event(new_event)


def load_events() -> list[Event]:
    """Gets a list of all events stored with the store_event function.

    :returns:
        The list of events.
    :rtype: list[event]
    """
    return EventIO.load_events()


def update_event(uuid: str, updated_event: Event) -> None:
    """Updates an event stored with the store_event function.

    Looks for an event stored with the store_event function which
    has the same uuid as the given uuid, then updates that event.

    :param uuid:
        uuid to look up event to update.
    :type uuid: str

    :param updated_event:
        The event object to update the event to.
    :type updated_event: event
    """
    EventIO.update_event(uuid, updated_event)

# Admin API

def store_admin(admin: Administrator) -> None:
    """Stores new admins in a JSON file to be fetched later.

    :param admin:
        The admin object to store.
    :type admin: admin
    """
    AdminIO.store_admin(admin)


def load_admins() -> list[Administrator]:
    """Gets a list of all admins stored with the store_admin function.

    :returns:
        The list of admins.
    :rtype: list[admin]
    """
    return AdminIO.load_admins()


def update_admin(uuid: str, updated_admin: Administrator) -> None:
    """Updates an admin stored with the store_admin function.

    Looks for an admin stored with the store_admin function which
    has the same uuid as the given uuid, then updates that admin.

    :param uuid:
        uuid to look up admin to update.
    :type uuid: str

    :param updated_admin:
        The admin object to update the admin to.
    :type updated_admin: admin
    """
    AdminIO.update_admin(uuid, updated_admin)

# Sponsor API

def store_sponsor(sponsor: Sponsor) -> None:
    """Stores new sponsors in a JSON file to be fetched later.

    :param sponsor:
        The sponsor object to store.
    :type sponsor: sponsor
    """
    SponsorIO.store_sponsor(sponsor)


def load_sponsors() -> list[Sponsor]:
    """Gets a list of all sponsors stored with the store_sponsor function.

    :returns:
        The list of sponsors.
    :rtype: list[sponsor]
    """
    return SponsorIO.load_sponsors()


def update_sponsor(uuid: str, updated_sponsor: Sponsor) -> None:
    """Updates a sponsor stored with the store_sponsor function.

    Looks for a sponsor stored with the store_sponsor function which
    has the same uuid as the given uuid, then updates that sponsor.

    :param uuid:
        uuid to look up sponsor to update.
    :type uuid: str

    :param updated_sponsor:
        The sponsor object to update the sponsor to.
    :type updated_sponsor: sponsor
    """
    SponsorIO.update_sponsor(uuid, updated_sponsor)

