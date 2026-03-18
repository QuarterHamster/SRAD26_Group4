import json
from Models import Campus_user, ValidationError

FILE_PATH = "DataLayer/Repository/campus_user.json"


def store_campus_user(campus_user: Campus_user) -> None:
    """Stores new campus_user in a JSON file to be fetched later.

    :param campus_user:
        The campus_user object to store.
    :type campus_user: campus_user
    """
    # Changes object campus_user into a dictionary mapping attributes to keys.
    data = campus_user.__dict__

    # Reads JSON file containing campus_users and stores the contents as a
    # dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as campus_user_file:
            file_content = dict(json.load(campus_user_file))
    except Exception:
        raise ValidationError("Could not read campus_user file.")

    # Adds the new campus_user into the dictionary mapping its uuid to the
    # object for easy lookup.
    file_content[campus_user.uuid] = data

    # Writes the updated file content back into the JSON file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as campus_user_file:
            json.dump(file_content, campus_user_file, indent=4)
    except Exception:
        raise ValidationError("Could not write into campus_user file")


def load_campus_users() -> list[Campus_user]:
    """Gets a list of all campus_users stored with the store_campus_user function.

    :returns:
        The list of campus_users.
    :rtype: list[campus_user]
    """
    # Reads the JSON file containing campus_users and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as campus_user_file:
            file_content = dict(json.load(campus_user_file))
    except Exception:
        raise ValidationError("Could not read campus_user file")

    # Creates a list of all campus_users in the server file.
    # Each campus_user is stored as a campus_user model object.
    campus_user_list: list[Campus_user] = []
    for value in file_content.values():
        # Uses **value to unpack the dictionary into a campus_user model object.
        try:
            campus_user_list.append(Campus_user(**value))
        except Exception:
            raise ValidationError(
                "Could nto change file content into campus_user objects."
            )

    return campus_user_list


def update_campus_user(uuid: str, updated_campus_user: Campus_user) -> None:
    """Updates a campus_user stored with the store_campus_user function.

    Looks for a campus_user stored with the store_campus_user function which
    has the same uuid as the given uuid, then updates that campus_user.

    :param uuid:
        uuid to look up campus_user to update.
    :type uuid: str

    :param updated_campus_user:
        The campus_user object to update the campus_user to.
    :param updated_campus_user: campus_user
    """
    # Reads the JSON file containing campus_users and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as campus_user_file:
            file_content = dict(json.load(campus_user_file))
    except Exception:
        raise ValidationError("Could not read campus_user file")

    # Overwrites the object tied to the given uuid to the object
    # given after checking if it exists to prevent key error.
    if uuid in file_content:
        file_content[uuid] = updated_campus_user.__dict__
    else:
        raise ValidationError("Could not find campus_user with given uuid.")

    # Writes the updated dictionary back into the campus_user file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as campus_user_file:
            json.dump(file_content, campus_user_file, indent=4)
    except Exception:
        raise ValidationError("Could not write into campus_user file.")