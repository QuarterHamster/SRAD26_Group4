from Models import Event
from DataLayer import EventIO
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
