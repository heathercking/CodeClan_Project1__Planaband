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

    
    def no_attended(self, input_attendances):
        attended = []
        for attendance in input_attendances:
            if attendance.attended == True:
                attended.append(attendance)
        no_attended = len(attended)
        return no_attended
    
    def attendance_rate(self, no_attended, attendances):
        if no_attended > 0:
            rate = no_attended / len(attendances) * 100
            result = round(rate)
            return result
        else:
            return 0