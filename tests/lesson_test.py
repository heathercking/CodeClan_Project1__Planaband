import unittest

from models.lesson import Lesson

class TestLesson(unittest.TestCase):

    def setUp(self):
        self.lesson1 = Lesson("Beginner Recorder", "Rubeus Hagrid", "27-11-2021", "Recorder", True)
        self.lesson2 = Lesson("Piano 1:1", "Remus Lupin", "27-11-2021", "Piano")

    def test_lesson_has_name(self):
        self.assertEqual("Beginner Recorder", self.lesson1.name)

    def test_lesson_has_tutor(self):
        self.assertEqual("Rubeus Hagrid", self.lesson1.tutor)
    
    def test_lesson_has_date(self):
        self.assertEqual("27-11-2021", self.lesson1.date)
    
    def test_lesson_has_instrument(self):
        self.assertEqual("Recorder", self.lesson1.instrument)
    
    def test_lesson_has_group_status(self):
        self.assertEqual(True, self.lesson1.group)

    def test_lesson_has_id(self):
        self.assertEqual(None, self.lesson1.id)