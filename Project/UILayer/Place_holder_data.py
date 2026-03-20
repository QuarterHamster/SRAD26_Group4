from datetime import datetime

from Models.Campus_user import Campus_user
from Models.Enums import Branch_type, Event_status, School_type
from Models.Event import Event
from Models.Sponsor import Sponsor


REYKJAVIK_BRANCH = next(
    branch.value for branch in Branch_type if "reyk" in branch.value.lower()
)
AKUREYRI_BRANCH = Branch_type.AKUREYRI.value


campus_users: list[Campus_user] = [
    Campus_user(1, "Anna Jonsdottir", "anna1@campus.is", "active", School_type.STUDENT),
    Campus_user(2, "Bjarni Sigurdsson", "bjarni2@campus.is", "active", School_type.STUDENT),
    Campus_user(3, "Elin Gudmundsdottir", "elin3@campus.is", "active", School_type.STUDENT),
    Campus_user(4, "Kari Stefansson", "kari4@campus.is", "active", School_type.STUDENT),
    Campus_user(5, "Sara Magnusdottir", "sara5@campus.is", "active", School_type.STUDENT),
    Campus_user(6, "Jon THorsson", "jon6@campus.is", "active", School_type.STAFF),
    Campus_user(7, "Helga Kristinsdottir", "helga7@campus.is", "active", School_type.STAFF),
    Campus_user(8, "Arnar Petursson", "arnar8@campus.is", "active", School_type.STAFF),
    Campus_user(9, "Kristin Olafsdottir", "kristin9@campus.is", "active", School_type.STAFF),
    Campus_user(10, "David Einarsson", "david10@campus.is", "active", School_type.STAFF),
    Campus_user(11, "Ragnar Bjornsson", "ragnar11@campus.is", "active", School_type.STUDENT),
    Campus_user(12, "Lilja Sigfusdottir", "lilja12@campus.is", "active", School_type.STUDENT),
    Campus_user(13, "Stefan Gislason", "stefan13@campus.is", "active", School_type.STUDENT),
    Campus_user(14, "Maria Bjork", "maria14@campus.is", "active", School_type.STUDENT),
    Campus_user(15, "Oskar THordarson", "oskar15@campus.is", "active", School_type.STUDENT),
]

events: list[Event] = [
    Event(
        1,
        "Campus Coding Night",
        "Students meet to work on coding projects together.",
        ["coding", "tech", "collaboration"],
        REYKJAVIK_BRANCH,
        datetime(2026, 3, 10, 18, 0),
        "Room E301",
        False,
        Event_status.ACTIVE,
        "1",
    ),
    Event(
        2,
        "Photography Walk",
        "Campus photo walk for students interested in photography.",
        ["photography", "creative", "outdoors"],
        AKUREYRI_BRANCH,
        datetime(2026, 3, 12, 16, 30),
        "Campus Main Entrance",
        False,
        Event_status.ACTIVE,
        "2",
    ),
    Event(
        3,
        "Startup Meetup",
        "Discussion about student startups and entrepreneurship.",
        ["business", "startup", "networking"],
        REYKJAVIK_BRANCH,
        datetime(2026, 3, 15, 17, 0),
        "Innovation Hub",
        False,
        Event_status.ACTIVE,
        "3",
    ),
    Event(
        4,
        "Staff Strategy Meeting",
        "Internal planning meeting for upcoming campus events.",
        ["staff", "planning"],
        AKUREYRI_BRANCH,
        datetime(2026, 3, 11, 9, 0),
        "Admin Building Room 2",
        True,
        Event_status.PENDING,
        "4",
    ),
    Event(
        5,
        "Training Session",
        "Open fitness training for students interested in movement.",
        ["sport", "fitness"],
        REYKJAVIK_BRANCH,
        datetime(2026, 3, 14, 19, 0),
        "Campus Gym Hall",
        False,
        Event_status.ACTIVE,
        "5",
    ),
]

sponsors: list[Sponsor] = [
    Sponsor("1", "NovaTech", "contact@novatech.is", "active", "NovaTech"),
    Sponsor("2", "Arctic Systems", "info@arcticsystems.is", "active", "Arctic Systems"),
    Sponsor("3", "BlueWave Energy", "hello@bluewave.is", "active", "BlueWave Energy"),
    Sponsor("4", "Nordic Data", "support@nordicdata.is", "inactive", "Nordic Data"),
    Sponsor("5", "IceSoft Solutions", "team@icesoft.is", "active", "IceSoft Solutions"),
    Sponsor("6", "Aurora Labs", "contact@auroralabs.is", "active", "Aurora Labs"),
    Sponsor("7", "PolarTech", "info@polartech.is", "inactive", "PolarTech"),
    Sponsor("8", "FrostByte", "admin@frostbyte.is", "active", "FrostByte"),
]
