import sys
import unittest
from datetime import datetime
from pathlib import Path

# Allow imports like "from Models.Event import Event".
sys.path.append(str(Path(__file__).resolve().parents[1] / "Project"))

from LogicLayer.EventLogic import EventLogic
from Models.Event import Event


def make_event(
    event_name="Test Event",
    date_time=datetime(2026, 3, 10, 18, 0),
    is_private=False,
    creator="1",
    event_tags=None,
):
    return Event(
        uuid="evt-1",
        event_name=event_name,
        description="desc",
        event_tags=event_tags if event_tags is not None else [],
        branch_type="Engineering",
        date_time=date_time,
        location="Room 1",
        is_private=is_private,
        status="active",
        creator=creator,
    )


class EventModelTests(unittest.TestCase):
    def test_time_tags_weekday_evening(self):
        event = make_event(date_time=datetime(2026, 3, 10, 18, 0))  # Tuesday
        self.assertIn("evening", event.time_tags)
        self.assertIn("weekday", event.time_tags)
        self.assertIn("march", event.time_tags)

    def test_time_tags_weekend_morning(self):
        event = make_event(date_time=datetime(2026, 3, 14, 9, 0))  # Saturday
        self.assertIn("morning", event.time_tags)
        self.assertIn("weekend", event.time_tags)

    def test_event_tags_are_normalized_and_merged(self):
        event = make_event(event_tags=[" Tech ", "tech", "", "AI"])
        self.assertIn("tech", event.event_tags)
        self.assertIn("ai", event.event_tags)
        self.assertEqual(1, event.event_tags.count("tech"))
        self.assertTrue(set(event.time_tags).issubset(set(event.event_tags)))

    def test_private_event_visibility_rules(self):
        event = make_event(is_private=True, creator="42")
        event.invite_user("7")
        self.assertTrue(event.can_be_viewed_by("42"))  # creator
        self.assertTrue(event.can_be_viewed_by("7"))   # invited user
        self.assertFalse(event.can_be_viewed_by("8"))  # not invited

    def test_invite_user_does_not_duplicate(self):
        event = make_event()
        event.invite_user(5)
        event.invite_user("5")
        self.assertEqual(["5"], event.invited_users)

    def test_invalid_datetime_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            make_event(date_time="2026-03-10 18:00")


class EventLogicTests(unittest.TestCase):
    def test_get_visible_events_filters_private(self):
        logic = EventLogic()
        public_event = make_event(event_name="Public", is_private=False, creator="1")
        private_event = make_event(event_name="Private", is_private=True, creator="1")
        private_event.invite_user("2")

        events = [public_event, private_event]
        visible_for_2 = logic.get_visible_events(events, "2")
        visible_for_3 = logic.get_visible_events(events, "3")

        self.assertEqual(2, len(visible_for_2))
        self.assertEqual(1, len(visible_for_3))
        self.assertEqual("Public", visible_for_3[0].event_name)

    def test_sort_visible_events_by_name(self):
        logic = EventLogic()
        a = make_event(event_name="Zebra Meetup")
        b = make_event(event_name="Alpha Meetup")

        sorted_events = logic.sort_visible_events([a, b], user_id="1", sort_by="name")
        self.assertEqual(["Alpha Meetup", "Zebra Meetup"], [event.event_name for event in sorted_events])

    def test_sort_visible_events_default_by_date_for_unknown_criterion(self):
        logic = EventLogic()
        late = make_event(event_name="Late", date_time=datetime(2026, 3, 20, 18, 0))
        early = make_event(event_name="Early", date_time=datetime(2026, 3, 10, 18, 0))

        sorted_events = logic.sort_visible_events([late, early], user_id="1", sort_by="not-a-valid-option")
        self.assertEqual(["Early", "Late"], [event.event_name for event in sorted_events])

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


if __name__ == "__main__":
    unittest.main()
