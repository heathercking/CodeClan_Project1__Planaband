class NextOfKin:
    
    def __init__(self, name, contact_number, address, postcode, account=0.00, id=None):
        self.name = name
        self.contact_number = contact_number
        self.address = address
        self.postcode = postcode
        self.account = account
        self.id = id

    
    def charge_nok_account(self, input_fee):
        self.account += input_fee

    def credit_nok_account(self, input_payment):
        self.account -= input_payment