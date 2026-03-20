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

    def __init__(
        self,
        uuid,
        event_name,
        description,
        event_tags,
        branch_type,
        date_time,
        location,
        is_private,
        status,
        creator,
    ):
        self.uuid = uuid
        self.event_name = event_name
        self.description = description
        self.time_tags = self._derive_time_tags(date_time)
        base_tags = [tag.strip().lower() for tag in (event_tags or []) if isinstance(tag, str) and tag.strip()]
        self.event_tags = sorted(set(base_tags + self.time_tags))
        self.branch_type = branch_type
        self.date_time = date_time
        self.location = location
        self.is_private = is_private
        self.status = status
        self.creator = creator
        self.attendees = []
        self.invitees = []
        self.invited_users = []

    def invite_user(self, user_id):
        user_id = str(user_id)
        if user_id not in self.attendees:
            self.attendees.append(user_id)

    def add_attendee(self, attendee_name):
        attendee_name = str(attendee_name).strip()
        if attendee_name == "":
            return False

        if attendee_name not in self.attendees:
            self.attendees.append(attendee_name)
            return True

        return False

    def can_be_viewed_by(self, user_id):
        if not self.is_private:
            return True

        if str(user_id) == str(self.creator):
            return True

        for invited_user in self.invited_users:
            if str(invited_user) == str(user_id):
                return True

        return False

    def _derive_time_tags(self, date_time):
        hour = date_time.hour
        if 5 <= hour <= 11:
            day_part = "morning"
        elif 12 <= hour <= 16:
            day_part = "afternoon"
        elif 17 <= hour <= 21:
            day_part = "evening"
        else:
            day_part = "night"

        weekday_type = "weekend" if date_time.weekday() >= 5 else "weekday"
        month_tag = date_time.strftime("%B").lower()
        return [day_part, weekday_type, month_tag]
    def __str__(self):
        tags_text = ", ".join(str(i) for i in self.event_tags)
        return (
            f"Creator: {self.creator}\n"
            f"Name: {self.event_name}\n"
            f"Description: {self.description}\n"
            f"Tags: {tags_text}\n"
            f"Branch: {self.branch_type}\n"
            f"The event is at: {self.date_time}\n"
            f"Location: {self.location}"
        )
    

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
