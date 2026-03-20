import datetime

from Models.Event import Event
from DataLayer import DataLayerAPI
from uuid import uuid4


class EventLogic:
    def create_event(self, event_name, description, event_tags, branch_type, date_time, location, is_private, status, creator) -> Event:
        """
        :param event_name:
        :type event_name: str
        :param description:
        :type description: str
        :param event_tags:
        :type event_tags: list
        :param branch_type:
        :type branch_type: str
        :param date_time:
        :type date_time: datetime
        :param location:
        :type location: str
        :param is_private:
        :type is_private: bool
        :param creator: uuid of the event creator
        :type creator: str
        :return:
        """
        if not isinstance(date_time, datetime.datetime):
            raise ValueError("date_time must be a datetime instance")

        uuid = str(uuid4())
        normalized_status = getattr(status, "value", status)
        new_event = Event(
            uuid,
            event_name,
            description,
            event_tags,
            branch_type,
            date_time,
            location,
            is_private,
            normalized_status,
            creator,
        )
        DataLayerAPI.store_event(new_event)
        return new_event

    def _normalize_status(self, status):
        return str(getattr(status, "value", status)).strip().lower()

    def is_event_active(self, event):
        return self._normalize_status(getattr(event, "status", "")) == "active"

    def filter_events_by_time_tag(self, events, time_tag):
        normalized = str(time_tag).strip().lower()
        return [event for event in events if normalized in getattr(event, "time_tags", [])]

    def invite_user(self, event, user_id):
        event.invite_user(user_id)


    def can_user_view_event(self, event, user_id):
        if self.is_event_active(event):
            return event.can_be_viewed_by(user_id)

        return str(user_id) == str(getattr(event, "creator", ""))


    def get_visible_events(self, events, user_id):

        visible_events = []

        for event in events:
            if self.can_user_view_event(event, user_id):
                visible_events.append(event)

        return visible_events

    def sort_visible_events(self, events, user_id, sort_by="date"):
        visible_events = self.get_visible_events(events, user_id)
        criterion = str(sort_by).strip().lower()

        if criterion == "name":
            return sorted(visible_events, key=lambda event: event.event_name.lower())
        if criterion == "branch":
            return sorted(visible_events, key=lambda event: str(event.branch_type).lower())

        # Default sort is by event date/time.
        return sorted(visible_events, key=lambda event: event.date_time)

    def join_event(self, event, attendee_name):
        return event.add_attendee(attendee_name)

# EventLogic = EventLogic()
# test_time = datetime.datetime
# a = EventLogic.create_event("Test Event", "This event is for testing project features", [],"Reykjvík", test_time, "Sindris house", False, "uuid")
# for x, y in a.__dict__.items():
#     print(f"{x}: {y}")
