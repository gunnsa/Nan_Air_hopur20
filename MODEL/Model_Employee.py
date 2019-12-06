class Model_Employee:
    def __init__(self, ssn, name, role, rank, licens, address, phonenumber, email):
        self.ssn = ssn
        self.name = name
        self.role = role
        self.rank = rank
        self.licens = licens
        self.address = address
        self.phonenumber = phonenumber
        self.email = email

    def __str__(self):
        retString = ""
        retString += self.ssn + " "
        retString += self.name + " "
        retString += self.role + " "
        retString += self.rank + " "
        retString += self.licens + " "
        retString += self.address + " "
        retString += self.phonenumber + " "
        retString += self.email + " "
        return retString