import unittest

from models.pupil import *

class TestPupil(unittest.TestCase):

    def setUp(self):
        self.pupil1 = Pupil("Harry Potter", "31-07-2010", "Piano", "4", "Rubeus Hagrid", "Sat grade 4 exam in April")
        self.pupil2 = Pupil("Hermione Granger", "19-09-2015", "Recorder", "0", "Parents", "Recommended to us by school teacher")

    
    def test_pupil_has_name(self):
        self.assertEqual("Harry Potter", self.pupil1.name)

    def test_pupil_has_dob(self):
        self.assertEqual("31-07-2010", self.pupil1.dob)

    def test_pupil_has_instrument(self):
        self.assertEqual("Piano", self.pupil1.instrument)
    
    def test_pupil_has_grade(self):
        self.assertEqual("4", self.pupil1.grade)
    
    def test_pupil_has_nok(self):
        self.assertEqual("Rubeus Hagrid", self.pupil1.next_of_kin)
    
    def test_pupil_has_notes(self):
        self.assertEqual("Sat grade 4 exam in April", self.pupil1.notes)
    
    def test_pupil_has_id(self):
        self.assertEqual(None, self.pupil1.id)  
