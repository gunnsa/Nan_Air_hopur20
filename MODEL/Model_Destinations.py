class Model_Destinations:
    def __init__(self, id, destination, flighttime, distance, name_emergencycontact, number_emergencycontact):
        self.id = id
        self.destination = destination
        self.flighttime = flighttime
        self.distance = distance
        self.name_emergencycontact = name_emergencycontact
        self.number_emergencycontact = number_emergencycontact

    def __str__(self):
        retString = ""
        retString += self.id + " "
        retString += self.destination + " "
        retString += self.flighttime + " "
        retString += self.distance + " "
        retString += self.name_emergencycontact + " "
        retString += self.number_emergencycontact + " "
        return retString