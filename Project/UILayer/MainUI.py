from Models.Campus_user import Campus_user
from Models.Enums import School_type, Event_tags, Branch_type, Event_status
from Models.Events import Event
from datetime import datetime


class MainUI:
    def run(self):
        SCALE: int = 80

        def border(scale: int = SCALE) -> str:
            return f"{('-' * SCALE)[:scale]}"

        def walls(scale: int = SCALE, text: str = "") -> str:
            if scale <= 0:
                return ""
            if scale == 1:
                return "|"

            inner_width = scale - 2
            text = text[:inner_width]

            padding_left = (inner_width - len(text)) // 2
            padding_right = inner_width - len(text) - padding_left

            return "|" + " " * padding_left + text + " " * padding_right + "|"

        def user_input(valid: list[str]):
            while True:
                response: str = input(">> ").strip().lower()
                if response in valid:
                    return response

                print("Not a valid option try again")

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
                "active",
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
                "active",
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
                "active",
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
                "scheduled",
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
                "active",
                "5",
            ),
        ]

        while True:
            print(border(SCALE))
            print(walls(SCALE))
            print(walls(SCALE, "1. See Events"))
            print(walls(SCALE, "2. Create Event"))
            print(walls(SCALE, "3. Accept/Reject Events As Admin"))
            print(walls(SCALE, "q. Quit"))
            print(walls(SCALE))

            response: str = user_input(["1", "2", "3", "q"])
            print(border())

            if response == "1":
                for event in events:
                    print(event)
                    print(border())

                input("Input Anything to Continue")

            if response == "2":
                next_temp_uuid: int = 1 + events[-1].uuid

                event_name: str = input("Event Name: ")
                description: str = input("Event Description: ")
                event_tag: Event_tags = Event_tags.ACADEMIC
                branch_type: Branch_type = Branch_type.REYKJAVÍK
                date_time: datetime = datetime(2026, 3, 10, 18, 0)
                location: str = input("Event Location: ")
                is_private: bool = False
                status: Event_status = Event_status.PENDING
                creator: str = campus_users[-1].name

                events.append(
                    Event(
                        next_temp_uuid,
                        event_name,
                        description,
                        event_tag,
                        branch_type,
                        date_time,
                        location,
                        is_private,
                        status,
                        creator,
                    )
                )

            if response == "3":
                pass

            if response == "q":
                break
