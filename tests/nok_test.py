import unittest

from models.nok import NextOfKin

class TestNextOfKin(unittest.TestCase):

    def setUp(self):
        self.nok1 = NextOfKin("Lily Potter", "07777 888999", "The Potter Cottage, Godric's Hollow", "EH53 9AZ", 0.00)
    

    def test_nok_has_name(self):
        self.assertEqual("Lily Potter", self.nok1.name)

    def test_nok_has_contact_number(self):
        self.assertEqual("07777 888999", self.nok1.contact_number)
    
    def test_nok_has_address(self):
        self.assertEqual("The Potter Cottage, Godric's Hollow", self.nok1.address)

    def test_nok_has_postcode(self):
        self.assertEqual("EH53 9AZ", self.nok1.postcode)

    def test_nok_has_id(self):
        self.assertEqual(None, self.nok1.id)
    
    def test_nok_has_account(self):
        self.assertEqual(0.00, self.nok1.account)

    def test_can_charge_to_nok_account(self):
        fee = 10.00
        self.nok1.charge_nok_account(fee)
        self.assertEqual(10.00, self.nok1.account)

    def test_can_credit_payment_to_nok_account(self):
        fee = 10.00
        self.nok1.charge_nok_account(fee)
        payment = 10.00
        self.nok1.credit_nok_account(payment)
        self.assertEqual(0.00, self.nok1.account)