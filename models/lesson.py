class Lesson:

    def __init__(self, name, date, time, instrument, tutor, max_capacity, group_status=False, id=None):
        self.name = name
        self.date = date
        self.time = time
        self.instrument = instrument
        self.tutor = tutor
        self.max_capacity = max_capacity
        self.attendees = []
        self.group_status = group_status
        self.id = id


    def check_free_spaces(self, input_no_attendees):
        if len(input_no_attendees) >= self.max_capacity:
            return False
        else:
            return True
