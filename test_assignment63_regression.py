import sys
import unittest
from datetime import datetime
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "Project"))

from LogicLayer.EventLogic import EventLogic
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


class NewFeatureTests(unittest.TestCase):
    # New feature 1: sorting available events.
    def test_sort_visible_events_by_branch(self):
        logic = EventLogic()
        a = make_event(event_name="A", branch_type="Science")
        b = make_event(event_name="B", branch_type="Arts")

        sorted_events = logic.sort_visible_events([a, b], user_id="1", sort_by="branch")
        self.assertEqual(["Arts", "Science"], [event.branch_type for event in sorted_events])

    # New feature 2: filtering available events by time tags.
    def test_filter_events_by_time_tag(self):
        logic = EventLogic()
        morning = make_event(event_name="Morning", date_time=datetime(2026, 3, 11, 9, 0))
        evening = make_event(event_name="Evening", date_time=datetime(2026, 3, 11, 18, 0))

        filtered = logic.filter_events_by_time_tag([morning, evening], "morning")
        self.assertEqual(["Morning"], [event.event_name for event in filtered])

    def test_join_event_adds_attendee_once(self):
        logic = EventLogic()
        event = make_event()

        self.assertTrue(logic.join_event(event, "Alice"))
        self.assertFalse(logic.join_event(event, "Alice"))

    def test_create_event_stores_event_in_memory(self):
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

    def test_create_event_rejects_invalid_datetime(self):
        logic = EventLogic()
        with self.assertRaises(ValueError):
            logic.create_event(
                event_name="Bad Event",
                description="desc",
                event_tags=[],
                branch_type="Engineering",
                date_time="2026-03-10 18:00",
                location="Room 1",
                is_private=False,
                status="active",
                creator="1",
            )

    def test_sort_visible_events_by_name(self):
        logic = EventLogic()
        a = make_event(event_name="Zebra Meetup")
        b = make_event(event_name="Alpha Meetup")

        sorted_events = logic.sort_visible_events([a, b], user_id="1", sort_by="name")
        self.assertEqual(["Alpha Meetup", "Zebra Meetup"], [event.event_name for event in sorted_events])


class RegressionTests(unittest.TestCase):
    # Regression test 1: existing visibility behavior still works.
    def test_regression_private_event_visibility_still_works(self):
        event = make_event(is_private=True, creator="42")
        event.invite_user("7")

        self.assertTrue(event.can_be_viewed_by("42"))
        self.assertTrue(event.can_be_viewed_by("7"))
        self.assertFalse(event.can_be_viewed_by("8"))

    # Regression test 2: existing time-tag generation still works.
    def test_regression_time_tags_still_generated(self):
        event = make_event(date_time=datetime(2026, 3, 10, 18, 0))

        self.assertIn("evening", event.time_tags)
        self.assertIn("weekday", event.time_tags)
        self.assertIn("march", event.time_tags)

    def test_regression_non_active_event_visible_only_to_creator(self):
        logic = EventLogic()
        pending_event = make_event(is_private=True, creator="10", status="pending")
        pending_event.invite_user("5")

        self.assertTrue(logic.can_user_view_event(pending_event, "10"))
        self.assertFalse(logic.can_user_view_event(pending_event, "5"))


if __name__ == "__main__":
    unittest.main()
