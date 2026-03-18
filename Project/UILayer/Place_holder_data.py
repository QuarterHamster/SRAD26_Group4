from Models.Campus_user import Campus_user
from Models.Enums import School_type, Event_tags, Branch_type, Event_status
from Models.Event import Event
from Models.Sponsor import Sponsor
from datetime import datetime


sponsors: list[Sponsor] = [
    Sponsor("1", "TechCorp Iceland", "contact@techcorp.is", "active", "TechCorp Iceland"),
    Sponsor("2", "Nordic Startup Fund", "info@nordicfund.is", "active", "Nordic Startup Fund"),
    Sponsor("3", "Reykjavík Sports Club", "hello@rsc.is", "active", "Reykjavík Sports Club"),
]

campus_users: list[Campus_user] = [
    Campus_user(
        1, "Anna Jónsdóttir", "anna1@campus.is", "active", School_type.STUDENT
    ),
    Campus_user(
        2,
        "Bjarni Sigurðsson",
        "bjarni2@campus.is",
        "active",
        School_type.STUDENT,
    ),
    Campus_user(
        3,
        "Elín Guðmundsdóttir",
        "elin3@campus.is",
        "active",
        School_type.STUDENT,
    ),
    Campus_user(
        4, "Kári Stefánsson", "kari4@campus.is", "active", School_type.STUDENT
    ),
    Campus_user(
        5, "Sara Magnúsdóttir", "sara5@campus.is", "active", School_type.STUDENT
    ),
    Campus_user(
        6, "Jón Þórsson", "jon6@campus.is", "active", School_type.STAFF
    ),
    Campus_user(
        7,
        "Helga Kristinsdóttir",
        "helga7@campus.is",
        "active",
        School_type.STAFF,
    ),
    Campus_user(
        8, "Arnar Pétursson", "arnar8@campus.is", "active", School_type.STAFF
    ),
    Campus_user(
        9,
        "Kristín Ólafsdóttir",
        "kristin9@campus.is",
        "active",
        School_type.STAFF,
    ),
    Campus_user(
        10, "Davíð Einarsson", "david10@campus.is", "active", School_type.STAFF
    ),
    Campus_user(
        11,
        "Ragnar Björnsson",
        "ragnar11@campus.is",
        "active",
        School_type.STUDENT,
    ),
    Campus_user(
        12,
        "Lilja Sigfúsdóttir",
        "lilja12@campus.is",
        "active",
        School_type.STUDENT,
    ),
    Campus_user(
        13,
        "Stefán Gíslason",
        "stefan13@campus.is",
        "active",
        School_type.STUDENT,
    ),
    Campus_user(
        14, "María Björk", "maria14@campus.is", "active", School_type.STUDENT
    ),
    Campus_user(
        15,
        "Óskar Þórðarson",
        "oskar15@campus.is",
        "active",
        School_type.STUDENT,
    ),
]

events: list[Event] = [
    Event(
        1,
        "Campus Coding Night",
        "Students meet to work on coding projects together.",
        ["coding", "tech", "collaboration"],
        "Engineering",
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
        "Arts",
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
        "Business",
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
        "Administration",
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
        "Sports",
        datetime(2026, 3, 14, 19, 0),
        "Campus Gym Hall",
        False,
        Event_status.ACTIVE,
        "5",
    ),
]

sponsors = [
    Sponsor("1", "NovaTech", "contact@novatech.is", "active"),
    Sponsor("2", "Arctic Systems", "info@arcticsystems.is", "active"),
    Sponsor("3", "BlueWave Energy", "hello@bluewave.is", "active"),
    Sponsor("4", "Nordic Data", "support@nordicdata.is", "inactive"),
    Sponsor("5", "IceSoft Solutions", "team@icesoft.is", "active"),
    Sponsor("6", "Aurora Labs", "contact@auroralabs.is", "active"),
    Sponsor("7", "PolarTech", "info@polartech.is", "inactive"),
    Sponsor("8", "FrostByte", "admin@frostbyte.is", "active"),
]