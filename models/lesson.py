class Lesson:

    def __init__(self, name, date, time, instrument, tutor, group_status=False, id=None):
        self.name = name
        self.date = date
        self.time = time
        self.instrument = instrument
        self.tutor = tutor
        self.group_status = group_status
        self.id = id