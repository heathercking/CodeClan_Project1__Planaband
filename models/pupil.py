class Pupil:

    def __init__(self, name, dob, instrument, grade, nok, notes, active=True, id=None):
        self.name = name
        self.dob = dob
        self.instrument = instrument
        self.grade = grade
        self.nok = nok
        self.notes = notes
        self.active = active
        self.id = id