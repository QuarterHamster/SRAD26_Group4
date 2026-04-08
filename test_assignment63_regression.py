import sys
import unittest
from datetime import datetime
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "Project"))

import LogicLayer.CampusUserLogic as campus_user_logic_module
from LogicLayer.CampusUserLogic import CampusUserLogic
from LogicLayer.EventLogic import EventLogic
from Models.Campus_user import Campus_user
from Models.Enums import Event_status, School_type
from Models.Event import Event


def make_event(
    event_name="Test Event",
    date_time=datetime(2026, 3, 10, 18, 0),
    is_private=False,
    creator="1",
    event_tags=None,
    status="active",
    branch_type="Engineering",
):
    return Event(
        uuid="evt-1",
        event_name=event_name,
        description="desc",
        event_tags=event_tags if event_tags is not None else [],
        branch_type=branch_type,
        date_time=date_time,
        location="Room 1",
        is_private=is_private,
        status=status,
        creator=creator,
    )


def make_user(user_id="1", name="Alice Student", email="alice@campus.is"):
    return Campus_user(user_id, name, email, "active", School_type.STUDENT)


class NewFeatureTests(unittest.TestCase):
    def test_report_event_adds_report_entry(self):
        logic = EventLogic()
        event = make_event()

        added = logic.report_event(event, "Inappropriate content", "Alice Student")

        self.assertTrue(added)
        self.assertEqual(1, len(event.reports))
        self.assertEqual("Inappropriate content", event.reports[0]["reason"])
        self.assertEqual("Alice Student", event.reports[0]["reportee_name"])

    def test_report_event_rejects_blank_reason(self):
        logic = EventLogic()
        event = make_event()

        added = logic.report_event(event, "   ", "Alice Student")

        self.assertFalse(added)
        self.assertEqual([], event.reports)

    def test_favorite_event_adds_name_once(self):
        logic = CampusUserLogic()
        user = make_user()

        first_add = logic.favorite_event(user, "Campus Coding Night")
        second_add = logic.favorite_event(user, "Campus Coding Night")

        self.assertTrue(first_add)
        self.assertFalse(second_add)
        self.assertEqual(["Campus Coding Night"], user.favorites)

    def test_unfavorite_event_removes_existing_favorite(self):
        logic = CampusUserLogic()
        user = make_user()
        user.add_favorite_event("Campus Coding Night")

        removed = logic.unfavorite_event(user, "Campus Coding Night")

        self.assertTrue(removed)
        self.assertEqual([], user.favorites)

    def test_favorite_event_rejects_blank_name(self):
        logic = CampusUserLogic()
        user = make_user()

        added = logic.favorite_event(user, "   ")

        self.assertFalse(added)
        self.assertEqual([], user.favorites)

    def test_view_favorite_events_returns_only_favorited_existing_events(self):
        logic = CampusUserLogic()
        user = make_user()
        user.add_favorite_event("Event A")
        user.add_favorite_event("Missing Event")
        original_events = campus_user_logic_module.events
        campus_user_logic_module.events = [
            make_event(event_name="Event A"),
            make_event(event_name="Event B"),
        ]

        try:
            favorites = logic.view_favorite_events(user)
        finally:
            campus_user_logic_module.events = original_events

        self.assertEqual(["Event A"], favorites)

    def test_view_old_events_returns_attended_ended_events(self):
        logic = CampusUserLogic()
        user = make_user(email="alice@campus.is")
        ended_event = make_event(event_name="Ended Event", status=Event_status.ENDED)
        active_event = make_event(event_name="Active Event", status=Event_status.ACTIVE)
        ended_event.attendees.append("alice@campus.is")
        active_event.attendees.append("alice@campus.is")
        original_events = campus_user_logic_module.events
        campus_user_logic_module.events = [ended_event, active_event]

        try:
            old_events = logic.view_old_events(user)
        finally:
            campus_user_logic_module.events = original_events

        self.assertEqual(["Ended Event"], old_events)


class RegressionTests(unittest.TestCase):
    def test_regression_private_event_visibility_still_works(self):
        event = make_event(is_private=True, creator="42")
        event.invite_user("7")

        self.assertTrue(event.can_be_viewed_by("42"))
        self.assertTrue(event.can_be_viewed_by("7"))
        self.assertFalse(event.can_be_viewed_by("8"))

    def test_regression_time_tags_still_generated(self):
        event = make_event(date_time=datetime(2026, 3, 10, 18, 0))

        self.assertIn("evening", event.time_tags)
        self.assertIn("weekday", event.time_tags)
        self.assertIn("march", event.time_tags)

    def test_regression_sort_visible_events_by_branch_still_works(self):
        logic = EventLogic()
        a = make_event(event_name="A", branch_type="Science")
        b = make_event(event_name="B", branch_type="Arts")

        sorted_events = logic.sort_visible_events([a, b], user_id="1", sort_by="branch")
        self.assertEqual(["Arts", "Science"], [event.branch_type for event in sorted_events])

    def test_regression_join_event_adds_attendee_once(self):
        logic = EventLogic()
        event = make_event()

        self.assertTrue(logic.join_event(event, "Alice"))
        self.assertFalse(logic.join_event(event, "Alice"))

    def test_regression_create_event_stores_event_in_memory(self):
        logic = EventLogic()

        created = logic.create_event(
            event_name="Created Event",
            description="desc",
            event_tags=["music"],
            branch_type="Engineering",
            date_time=datetime(2026, 3, 10, 18, 0),
            location="Room 1",
            is_private=False,
            status="active",
            creator="1",
        )

        self.assertEqual(1, len(logic.events))
        self.assertEqual(created.uuid, logic.events[0].uuid)

    def test_regression_active_event_visibility_uses_event_rules(self):
        logic = EventLogic()
        event = make_event(is_private=True, creator="1", status="active")
        logic.invite_user(event, "2")

        self.assertTrue(logic.can_user_view_event(event, "2"))
        self.assertFalse(logic.can_user_view_event(event, "3"))


if __name__ == "__main__":
    unittest.main()
