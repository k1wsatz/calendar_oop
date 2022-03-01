from event import Event


class Meeting(Event):
    def __init__(self, name, start_time, duration, location, owner, participants, room):
        super().__init__(name, start_time, duration, location, owner, participants)
        self.room = room
