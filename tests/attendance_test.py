import unittest

from models.attendance import Attendance

class TestAttendance(unittest.TestCase):

    def setUp(self):
        self.attendance1 = Attendance("Beginner Recorder", "Jilly Jo")

    def test_attendance_has_lesson(self):
        self.assertEqual("Beginner Recorder", self.attendance1.lesson)

    def test_attendance_has_pupil(self):
        self.assertEqual("Jilly Jo", self.attendance1.pupil)

    def test_attendance_has_attendance(self):
        self.assertEqual(False, self.attendance1.attendance)

    def test_attendance_has_id(self):
        self.assertEqual(None, self.attendance1.id)