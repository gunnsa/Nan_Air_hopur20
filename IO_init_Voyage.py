class Voyage:
    def __init__(self, dest, airp, date_out, flight_time_from_KEF, date_home, flight_time_to_KEF, dist, em_cont, em_phone):
        self.destination = dest
        self.airplane = airp
        self.date_out = date_out
        self.flight_time_from_KEF = flight_time_from_KEF
        self.date_home = date_home
        self.flight_time_to_KEF = flight_time_to_KEF
        self.distance = dist
        self.emergency_contact = em_cont
        self.emergency_phone = em_phone