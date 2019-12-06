class Model_Employee:
    def __init__(self, ssn, name, role, rank, license, address, phonenumber, email):
        self.ssn = ssn
        self.name = name
        self.role = role
        self.rank = rank
        self.license = license
        self.address = address
        self.phonenumber = phonenumber
        self.email = email

    def __str__(self):
        retString = ""
        retString += self.ssn + " "
        retString += self.name + " "
        retString += self.role + " "
        retString += self.rank + " "
        retString += self.license + " "
        retString += self.address + " "
        retString += self.phonenumber + " "
        retString += self.email + " "
        return retString