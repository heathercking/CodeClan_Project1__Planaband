class Lesson:

    def __init__(self, name, date, instrument, tutor, group=False, id=None):
        self.name = name
        self.date = date
        self.instrument = instrument
        self.tutor = tutor
        self.group = group
        self.id = id