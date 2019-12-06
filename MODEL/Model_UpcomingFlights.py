class Model_UpcomingFlights:
    #def __init__(self, flightNumber, departingFrom, arrivingAt, departure, arrival, aircraftID='', captain='', copilot='', fsm='', fa1='', fa2=''):

    def __init__(self, flightNumber, departingFrom, arrivingAt, departure, arrival):
        self.flightNumber = flightNumber
        self.departingFrom = departingFrom
        self.arrivingAt = arrivingAt
        self.departure = departure
        self.arrival = arrival
        #self.aircraftID = aircraftID
        #self.captain = captain
        #self.copilot = copilot
        #self.fsm = fsm
        #self.fa1 = fa1
        #self.fa2 = fa2

    def __str__(self):
        retString = ""
        retString += self.flightNumber + " "
        retString += self.departingFrom + " "
        retString += self.arrivingAt + " "
        retString += self.departure + " "
        retString += self.arrival + " "
        #retString += self.aircraftID + " "
        #retString += self.captain + " "
        #retString += self.copilot + " "
        #retString += self.fsm + " "
        #retString += self.fa1 + " "
        #retString += self.fa2 + " "
        return retString