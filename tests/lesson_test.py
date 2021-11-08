import unittest
from datetime import date

from models.lesson import Lesson

class TestLesson(unittest.TestCase):

    def setUp(self):
        self.lesson1 = Lesson("Beginner Recorder", date(2021, 11, 27), "10am", "Recorder", "Rubeus Hagrid", 2, True)
        self.lesson2 = Lesson("Piano 1:1", date(2021, 11, 27), "11am", "Piano", "Remus Lupin", 1)

    def test_lesson_has_name(self):
        self.assertEqual("Beginner Recorder", self.lesson1.name)

    def test_lesson_has_tutor(self):
        self.assertEqual("Rubeus Hagrid", self.lesson1.tutor)
    
    def test_lesson_has_date(self):
        self.assertEqual(date(2021, 11, 27), self.lesson1.date)
    
    def test_lesson_has_instrument(self):
        self.assertEqual("Recorder", self.lesson1.instrument)
    
    def test_lesson_has_group_status(self):
        self.assertEqual(True, self.lesson1.group_status)

    def test_lesson_has_id(self):
        self.assertEqual(None, self.lesson1.id)

    def test_lesson_has_time(self):
        self.assertEqual("10am", self.lesson1.time)

    def test_lesson_has_max_capacity(self):
        self.assertEqual(2, self.lesson1.max_capacity)
    
    def test_add_attendees_to_lesson(self):
        attendees = [1, 2]
        self.lesson1.add_attendees_to_lesson(attendees)
        self.assertEqual(2, len(self.lesson1.attendees))

    def test_count_free_spaces__one(self):
        attendees = [1]
        self.lesson1.add_attendees_to_lesson(attendees)
        self.assertEqual(1, self.lesson1.count_free_spaces())