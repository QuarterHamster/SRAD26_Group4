from datetime import datetime

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

    def __str__(self):
        return (f"Creator: {self.creator}\nName: {self.event_name}\nDescription: {self.description}\nTags: {", ".join(i for i in (self.event_tags))}\nBranch: {self.branch_type}\nThe event is at: {self.date_time}\nLocation: {self.location}")
    

events = [
    Event(
        1,
        "Campus Coding Night",
        "Students meet to work on coding projects together.",
        ["coding", "tech", "collaboration"],
        "Engineering",
        datetime(2026, 3, 10, 18, 0),
        "Room E301",
        False,
        "active",
        "1"
    ),

    Event(
        2,
        "Photography Walk",
        "Campus photo walk for students interested in photography.",
        ["photography", "creative", "outdoors"],
        "Arts",
        datetime(2026, 3, 12, 16, 30),
        "Campus Main Entrance",
        False,
        "active",
        "2"
    ),

    Event(
        3,
        "Startup Meetup",
        "Discussion about student startups and entrepreneurship.",
        ["business", "startup", "networking"],
        "Business",
        datetime(2026, 3, 15, 17, 0),
        "Innovation Hub",
        False,
        "active",
        "3"
    ),

    Event(
        4,
        "Staff Strategy Meeting",
        "Internal planning meeting for upcoming campus events.",
        ["staff", "planning"],
        "Administration",
        datetime(2026, 3, 11, 9, 0),
        "Admin Building Room 2",
        True,
        "scheduled",
        "4"
    ),

    Event(
        5,
        "Training Session",
        "Open fitness training for students interested in movement.",
        ["sport", "fitness"],
        "Sports",
        datetime(2026, 3, 14, 19, 0),
        "Campus Gym Hall",
        False,
        "active",
        "5"
    )
]