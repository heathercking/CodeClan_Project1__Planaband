class Attendance:

    def __init__(self, lesson, pupil, attended=False, id=None):
        self.lesson = lesson
        self.pupil = pupil
        self.attended = attended
        self.id = id


    def mark_attended(self):
        self.attended = True
