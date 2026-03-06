import datetime

from Models.Event import Event
from DataLayer import DataLayerAPI
from uuid import uuid4


class EventLogic:
    def __init__(self):
        self.events = []

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
        :param status:
        :type status: str
        :param creator: uuid of the event creator
        :type creator: str
        :return:
        """
        uuid = str(uuid4())
        new_event = Event(uuid, event_name, description, event_tags, branch_type, date_time, location, is_private, "proposed", creator)
        self.events.append(new_event)
        DataLayerAPI.store_event(new_event)
        return new_event

    def filter_events_by_time_tag(self, time_tag):
        normalized = str(time_tag).strip().lower()
        return [event for event in self.events if normalized in event.time_tags]


# EventLogic = EventLogic()
# test_time = datetime.datetime
# a = EventLogic.create_event("Test Event", "This event is for testing project features", [],"Reykjvík", test_time, "Sindris house", False, "uuid")
# for x, y in a.__dict__.items():
#     print(f"{x}: {y}")
