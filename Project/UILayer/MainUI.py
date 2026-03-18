

from Models.Campus_user import Campus_user
from Models.Enums import School_type, Event_tags, Branch_type, Event_status
from Models.Event import Event
from datetime import datetime
from Models.Sponsor import Sponsor
from UILayer.Place_holder_data import events, campus_users, sponsors
from UILayer.AdminUI import AdminUI
from LogicLayer import LogicLayerAPI


class MainUI:
    def __init__(self):
        self._adminUI = AdminUI()

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

        def create_event():
            event_name: str = input("Event Name: ")
            event_description: str = input("Event Description: ")
            #event_tags: str = input("Event Tags: ")
            # Branch type dropdown menu
            date_time: str = input("Event Date: ")
            event_location: str = input("Event Location: ")
            visibility = True
            while True:
                is_private: str = input("Should the event be private? Y/N: ")
                if is_private.lower() == "y":
                    visibility = False
                    break
                elif is_private.lower() == "n":
                    visibility = True
                    break
                else:
                    print("Invalid Input")
                    continue
            # creator is id:1
            new_event = LogicLayerAPI.create_event(event_name, event_description, [],Branch_type.REYKJAVÍK.value, date_time, event_location,visibility, 1)
            events.append(new_event)
            print(new_event)

        def list_events_short():
            # TODO: This will need to be changed later to Name where we fetch the id from the name
            user_id = input("Enter your user id: ").strip()
            print("Sort events by:")
            print("1. Date")
            print("2. Name")
            print("3. Branch")
            sort_choice = user_input(["1", "2", "3"])
            sort_map = {"1": "date", "2": "name", "3": "branch"}
            visible_events = LogicLayerAPI.event_logic.sort_visible_events(
                events, user_id, sort_map[sort_choice]
            )

            print(border(SCALE))
            print(walls(SCALE, "Events"))
            print(border(SCALE))

            if len(visible_events) == 0:
                print("No visible events.")
                return
            i = 0

            for e in visible_events:
                privacy = "Private" if e.is_private else "Public"
                tags_text = ", ".join(e.time_tags)
                print(
                    f"{e.event_name} [{privacy}] | {e.date_time:%Y-%m-%d %H:%M} | "
                    f"{e.branch_type} | Time tags: {tags_text}"
                )
                i += 1
                print(f"{i}. {e.event_name} [{privacy}] | Time tags: {tags_text}")
            
            print(border(SCALE))
            print(walls(SCALE, "1. send Event details to friends"))
            print(walls(SCALE, "b. Go back to home screen"))
            print(border(SCALE))

            response: str = user_input(["1", "b"])
            if response == "1":
                input("Select the event number")
                input("enter user_id of the friend")
                print("event sent")

        def filter_events_by_time_tag():
            user_id = input("Enter your user id: ").strip()
            time_tag = input("Enter a time tag (morning/afternoon/evening/night/weekday/weekend/month): ").strip().lower()
            visible_events = LogicLayerAPI.event_logic.get_visible_events(events, user_id)
            filtered_events = [e for e in visible_events if time_tag in e.time_tags]

            print(border(SCALE))
            print(walls(SCALE, f"Events with tag: {time_tag}"))
            print(border(SCALE))

            if len(filtered_events) == 0:
                print("No events found for that time tag.")
                return

            for e in filtered_events:
                privacy = "Private" if e.is_private else "Public"
                tags_text = ", ".join(e.time_tags)
                print(f"{e.event_name} [{privacy}] | Time tags: {tags_text}")

        def choose_event():
            list_events_short()
            while True:
                picked = input("Enter event Name: ").strip()
                for e in events:
                    if str(e.event_name) == picked:
                        return e
                print("Event not found, try again.")

        def post_event_as_sponsor():
            print(border(SCALE))
            print(walls(SCALE, "Sponsors"))
            print(border(SCALE))
            for s in sponsors:
                print(f"  [{s.uuid}] {s.organization}")
            print(border(SCALE))

            sponsor_id = input("Enter your sponsor ID: ").strip()
            sponsor = next((s for s in sponsors if s.uuid == sponsor_id), None)
            if sponsor is None:
                print("Sponsor not found.")
                return

            print(f"\nPosting event as: {sponsor.organization}")
            event_name = input("Event Name: ").strip()
            event_description = input("Event Description: ").strip()
            date_str = input("Event Date (YYYY-MM-DD HH:MM): ").strip()
            try:
                event_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD HH:MM.")
                return
            event_location = input("Event Location: ").strip()

            new_event = LogicLayerAPI.create_event(
                event_name, event_description, [],
                Branch_type.REYKJAVÍK.value, event_date,
                event_location, False, sponsor.uuid
            )
            events.append(new_event)
            print(border(SCALE))
            print(walls(SCALE, "Event submitted for admin review!"))
            print(border(SCALE))
            print(new_event)

        def show_attendees_for_event():
            chosen = choose_event()

            # Simple privacy rule: do not reveal attendees for private events
            if chosen.is_private:
                print(border(SCALE))
                print(walls(SCALE, "This event is private. Attendees are hidden."))
                print(border(SCALE))
                input("\nPress Enter to continue...")
                return

            print(border(SCALE))
            print(walls(SCALE, f"Attendees for: {chosen.event_name}"))
            print(border(SCALE))

            print(f"Total attendees: {len(chosen.attendees)}")

            if len(chosen.attendees) == 0:
                print("No attendees yet.")
            else:
                for a in chosen.attendees:
                    print("- " + a)

            input("\nPress Enter to continue...")

        def activate_sponsors():
            print(border(SCALE))
            number_of_sponsor = []
            number_of_sponsor.extend(sponsor_id + 1 for sponsor_id in range(len(sponsors)))
            i = 0
            for sponsor in sponsors:
                i += 1
                print(walls(SCALE, (f"{i} {sponsor.name} {sponsor.user_status}")))
            print(border(SCALE))

            select = int(input(walls(SCALE,"Select sponsor number: ")))
            while select not in number_of_sponsor:
                print(border(SCALE))
                print(walls(SCALE, f"the selected number is not available"))
                for sponsor in sponsors:
                    print(walls(SCALE, (i, sponsor.name, sponsor.user_status)))
                select = int(input(walls(SCALE, "Select sponsor number: ")))
                print(border(SCALE))
            activdeactiv = {"active": "inactive", "inactive": "active"}
            x = sponsors[select].user_status = activdeactiv[sponsor.user_status]
            if x == "inactive":
                x = "deactive"
            print(f"sponsor has been {x}ated")

        user_list = campus_users
        event_list = events

        # --- Hardcoded attendees for User Story #14 ---
        event_list[0].attendees = ["Anna Jónsdóttir", "Bjarni Sigurðsson", "Jón Þórsson"]
        event_list[1].attendees = ["Elín Guðmundsdóttir", "Kári Stefánsson"]
        event_list[2].attendees = [
            "Sara Magnúsdóttir",
            "Helga Kristinsdóttir",
            "Arnar Pétursson",
        ]
        # events[3] is private -> keep empty
        events[4].attendees = ["Ragnar Björnsson"]

        events[3].invite_user(6)
        events[3].invite_user(7)

        while True:
            print(border(SCALE))
            print(walls(SCALE))
            print(walls(SCALE, "1. See Events"))
            print(walls(SCALE, "2. Create Event"))
            print(walls(SCALE, "3. Accept/Reject Events As Admin"))
            print(walls(SCALE, "4. View Attendees For Event"))
            print(walls(SCALE, "5. Filter Events By Time Tag"))
            print(walls(SCALE, "6. Grant Sponsor permissions"))
            print(walls(SCALE, "7. Post event as sponsor"))
            print(walls(SCALE, "q. Quit"))
            print(walls(SCALE))

            response: str = user_input(["1", "2", "3", "4", "5", "6", "7", "q"])
            print(border())

            if response == "1":
                list_events_short()

            if response == "2":
                create_event()

            if response == "3":
                self._adminUI.accept_reject_event()

            if response == "4":
                show_attendees_for_event()

            if response == "5":
                filter_events_by_time_tag()
            
            if response == "6":
                activate_sponsors()

            if response == "7":
                post_event_as_sponsor()

            if response == "q":
                break
