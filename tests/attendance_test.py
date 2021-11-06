import unittest

from models.attendance import Attendance
from models.pupil import Pupil

class TestAttendance(unittest.TestCase):

    def setUp(self):
        self.attendance1 = Attendance("Beginner Recorder", "Harry Potter")
        self.attendance2 = Attendance("Beginner Recorder", "")
        self.pupil1 = Pupil("Hermione Granger", "19-09-2009", "Recorder", "0", "Parents", "Recommended to us by school teacher")

    def test_attendance_has_lesson(self):
        self.assertEqual("Beginner Recorder", self.attendance1.lesson)

    def test_attendance_has_pupil(self):
        self.assertEqual("Harry Potter", self.attendance1.pupil)

    def test_attendance_has_attended(self):
        self.assertEqual(False, self.attendance1.attended)

    def test_attendance_has_id(self):
        self.assertEqual(None, self.attendance1.id)

    def test_attendace_status_can_be_updated_to_True(self):
        self.attendance1.mark_attended()
        self.assertEqual(True, self.attendance1.attended)
