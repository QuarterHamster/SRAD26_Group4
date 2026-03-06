class Event:
    """
    Represents an event including its name, description, tags, date and location.

    :param uuid: Unique identifier for the player
    :type uuid: str
    :param event_name: Name of the event
    :type event_name: str
    :param description: Description of the event
    :type description: str
    :param event_tags: tags of the event
    :type event_tags: list
    :param branch_type: Type of branch of the event
    :type branch_type: str
    :param date_time: Date and time of the event
    :type date_time: datetime
    :param location: Location of the event
    :type location: str
    :param is_private: Whether the event is private
    :type is_private: bool
    :param status: Status of the event
    :type status: str
    :param creator: Creator of the event
    :type creator: str
    """
    def __init__(self, uuid, event_name, description, event_tags, branch_type, date_time, location, is_private, status, creator):
        self.uuid = uuid
        self.event_name = event_name
        self.description = description
        self.event_tags = event_tags
        self.branch_type = branch_type
        self.date_time = date_time
        self.location = location
        self.is_private = is_private
        self.status = status
        self.creator = creator
        self.attendees = []
        self.invitees = []