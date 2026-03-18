import json
from Models import Administrator, ValidationError

FILE_PATH = "DataLayer/Repository/admin.json"


def store_admin(admin: Administrator) -> None:
    """Stores new admin in a JSON file to be fetched later.

    :param admin:
        The admin object to store.
    :type admin: admin
    """
    # Changes object admin into a dictionary mapping attributes to keys.
    data = admin.__dict__

    # Reads JSON file containing admins and stores the contents as a
    # dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as admin_file:
            file_content = dict(json.load(admin_file))
    except Exception:
        raise ValidationError("Could not read admin file.")

    # Adds the new admin into the dictionary mapping its uuid to the
    # object for easy lookup.
    file_content[admin.uuid] = data

    # Writes the updated file content back into the JSON file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as admin_file:
            json.dump(file_content, admin_file, indent=4)
    except Exception:
        raise ValidationError("Could not write into admin file")


def load_admins() -> list[Administrator]:
    """Gets a list of all admins stored with the store_admin function.

    :returns:
        The list of admins.
    :rtype: list[admin]
    """
    # Reads the JSON file containing admins and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as admin_file:
            file_content = dict(json.load(admin_file))
    except Exception:
        raise ValidationError("Could not read admin file")

    # Creates a list of all admins in the server file.
    # Each admin is stored as an admin model object.
    admin_list: list[Administrator] = []
    for value in file_content.values():
        # Uses **value to unpack the dictionary into an admin model object.
        try:
            admin_list.append(Administrator(**value))
        except Exception:
            raise ValidationError(
                "Could nto change file content into admin objects."
            )

    return admin_list


def update_admin(uuid: str, updated_admin: Administrator) -> None:
    """Updates an admin stored with the store_admin function.

    Looks for an admin stored with the store_admin function which
    has the same uuid as the given uuid, then updates that admin.

    :param uuid:
        uuid to look up admin to update.
    :type uuid: str

    :param updated_admin:
        The admin object to update the admin to.
    :param updated_admin: admin
    """
    # Reads the JSON file containing admins and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as admin_file:
            file_content = dict(json.load(admin_file))
    except Exception:
        raise ValidationError("Could not read admin file")

    # Overwrites the object tied to the given uuid to the object
    # given after checking if it exists to prevent key error.
    if uuid in file_content:
        file_content[uuid] = updated_admin.__dict__
    else:
        raise ValidationError("Could not find admin with given uuid.")

    # Writes the updated dictionary back into the admin file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as admin_file:
            json.dump(file_content, admin_file, indent=4)
    except Exception:
        raise ValidationError("Could not write into admin file.")