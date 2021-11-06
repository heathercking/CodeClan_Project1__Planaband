import unittest

from models.tutor import *

class TestTutor(unittest.TestCase):

    def setUp(self):
        self.tutor1 = Tutor("Rubeus Hagrid", "07999 777888", "Hagrid's Hut, Hogwarts School", "EH42 2DD")
    
    def test_tutor_has_name(self):
        self.assertEqual("Rubeus Hagrid", self.tutor1.name)
    
    def test_tutor_has_contact_number(self):
        self.assertEqual("07999 777888", self.tutor1.contact_number)

    def test_tutor_has_address(self):
        self.assertEqual("Hagrid's Hut, Hogwarts School", self.tutor1.address)

    def test_tutor_has_postcode(self):
        self.assertEqual("EH42 2DD", self.tutor1.postcode)

    def test_tutor_has_id(self):
        self.assertEqual(None, self.tutor1.id)