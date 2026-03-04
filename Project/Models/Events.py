class Event:
    def __init__(
            self,
            id: str,
            name: str,
            description: str,
            event_tags: str,
            branch: str,
            date_time: str,
            location: str,
            is_private: bool,
            status: str,     # Pending, Active, Ended
            creator: str,
            attending: list = []
                 ):
        
        self.id = id
        self.name = name
        self.description = description
        self.event_tags = event_tags
        self.branch = branch
        self.date_time = date_time
        self.location = location
        self.is_private = is_private
        self.status = status
        self.creator = creator
        self.attending = attending
