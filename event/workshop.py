from event import Event


class Workshop(Event):
    def __init__(self, name, start_time, duration, location, owner, participants, kind='stationary'):
        super().__init__(name, start_time, duration, location, owner, participants)
        self.kind = kind
