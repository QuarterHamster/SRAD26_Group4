import json
from Models import Sponsor, ValidationError

FILE_PATH = "DataLayer/Repository/sponsor.json"


def store_sponsor(sponsor: Sponsor) -> None:
    """Stores new sponsor in a JSON file to be fetched later.

    :param sponsor:
        The sponsor object to store.
    :type sponsor: sponsor
    """
    # Changes object sponsor into a dictionary mapping attributes to keys.
    data = sponsor.__dict__

    # Reads JSON file containing sponsors and stores the contents as a
    # dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as sponsor_file:
            file_content = dict(json.load(sponsor_file))
    except Exception:
        raise ValidationError("Could not read sponsor file.")

    # Adds the new sponsor into the dictionary mapping its uuid to the
    # object for easy lookup.
    file_content[sponsor.uuid] = data

    # Writes the updated file content back into the JSON file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as sponsor_file:
            json.dump(file_content, sponsor_file, indent=4)
    except Exception:
        raise ValidationError("Could not write into sponsor file")


def load_sponsors() -> list[Sponsor]:
    """Gets a list of all sponsors stored with the store_sponsor function.

    :returns:
        The list of sponsors.
    :rtype: list[sponsor]
    """
    # Reads the JSON file containing sponsors and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as sponsor_file:
            file_content = dict(json.load(sponsor_file))
    except Exception:
        raise ValidationError("Could not read sponsor file")

    # Creates a list of all sponsors in the server file.
    # Each sponsor is stored as a sponsor model object.
    sponsor_list: list[Sponsor] = []
    for value in file_content.values():
        # Uses **value to unpack the dictionary into a sponsor model object.
        try:
            sponsor_list.append(Sponsor(**value))
        except Exception:
            raise ValidationError(
                "Could nto change file content into sponsor objects."
            )

    return sponsor_list


def update_sponsor(uuid: str, updated_sponsor: Sponsor) -> None:
    """Updates a sponsor stored with the store_sponsor function.

    Looks for a sponsor stored with the store_sponsor function which
    has the same uuid as the given uuid, then updates that sponsor.

    :param uuid:
        uuid to look up sponsor to update.
    :type uuid: str

    :param updated_sponsor:
        The sponsor object to update the sponsor to.
    :param updated_sponsor: sponsor
    """
    # Reads the JSON file containing sponsors and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as sponsor_file:
            file_content = dict(json.load(sponsor_file))
    except Exception:
        raise ValidationError("Could not read sponsor file")

    # Overwrites the object tied to the given uuid to the object
    # given after checking if it exists to prevent key error.
    if uuid in file_content:
        file_content[uuid] = updated_sponsor.__dict__
    else:
        raise ValidationError("Could not find sponsor with given uuid.")

    # Writes the updated dictionary back into the sponsor file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as sponsor_file:
            json.dump(file_content, sponsor_file, indent=4)
    except Exception:
        raise ValidationError("Could not write into sponsor file.")