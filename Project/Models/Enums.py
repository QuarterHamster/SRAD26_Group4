from enum import Enum


class School_type(Enum):
    STUDENT = "Student"
    STAFF = "Staff"

class Event_tags(Enum):
    ACADEMIC = "Academic"
    SPORT = "Sport"
    SOCIAL = "Social"

class Branch_type(Enum):
    REYKJAVÍK = "Reykjavík"
    AKUREYRI = "Akureyri"

class Event_status(Enum):
    PENDING = "Pending"
    ACTIVE = "Active"
    ENDED = "Ended"
    