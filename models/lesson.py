class Lesson:

    def __init__(self, name, tutor, date, instrument, group=False, id=None):
        self.name = name
        self.tutor = tutor
        self.date = date
        self.instrument = instrument
        self.group = group
        self.id = id