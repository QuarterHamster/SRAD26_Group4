import json
from Models import Event, ValidationError

FILE_PATH = "DataLayer/Repository/events.json"


def store_event(event: Event) -> None:
    """Stores new event in a JSON file to be fetched later.

    :param event:
        The event object to store.
    :type event: Event
    """
    # Changes object event into a dictionary mapping attributes to keys.
    data = event.__dict__

    # Reads JSON file containing events and stores the contents as a
    # dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as event_file:
            file_content = dict(json.load(event_file))
    except Exception:
        raise ValidationError("Could not read event file.")

    # Adds the new Event into the dictionary mapping its uuid to the
    # object for easy lookup.
    file_content[event.uuid] = data

    # Writes the updated file content back into the JSON file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as event_file:
            json.dump(file_content, event_file, indent=4)
    except Exception:
        raise ValidationError("Could not write into event file")


def load_events() -> list[Event]:
    """Gets a list of all events stored with the store_event function.

    :returns:
        The list of events.
    :rtype: list[event]
    """
    # Reads the JSON file containing events and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as event_file:
            file_content = dict(json.load(event_file))
    except Exception:
        raise ValidationError("Could not read event file")

    # Creates a list of all events in the server file.
    # Each event is stored as an event model object.
    event_list: list[Event] = []
    for value in file_content.values():
        # Uses **value to unpack the dictionary into an event model object.
        try:
            event_list.append(Event(**value))
        except Exception:
            raise ValidationError(
                "Could nto change file content into event objects."
            )

    return event_list


def update_event(uuid: str, updated_event: Event) -> None:
    """Updates an event stored with the store_event function.

    Looks for an event stored with the store_event function which
    has the same uuid as the given uuid, then updates that event.

    :param uuid:
        uuid to look up event to update.
    :type uuid: str

    :param updated_event:
        The event object to update the event to.
    :param updated_event: event
    """
    # Reads the JSON file containing events and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as event_file:
            file_content = dict(json.load(event_file))
    except Exception:
        raise ValidationError("Could not read event file")

    # Overwrites the object tied to the given uuid to the object
    # given after checking if it exists to prevent key error.
    if uuid in file_content:
        file_content[uuid] = updated_event.__dict__
    else:
        raise ValidationError("Could not find event with given uuid.")

    # Writes the updated dictionary back into the event file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as event_file:
            json.dump(file_content, event_file, indent=4)
    except Exception:
        raise ValidationError("Could not write into event file.")