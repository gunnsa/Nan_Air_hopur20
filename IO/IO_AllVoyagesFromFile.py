from MODEL.Model_PastFlights import Model_PastFlights
from MODEL.Model_UpcomingFlights import Model_UpcomingFlights
import datetime

class IO_AllVoyagesFromFile:

    def get_pastFlights_from_file(self):
        ''' Returns All Past Flights from file '''

        with open("PastFlights.csv", "r", encoding="utf-8") as past_file:
            all_lines = past_file.readlines()
            all_past = []
            
            for line in all_lines[1:]:
                line = line.split(',')
                past = Model_PastFlights(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10])
                all_past.append(past)

        return all_past     

    def get_upcomingFlights_from_file(self):
        ''' Returns All Upcoming Flights from file '''

        with open("UpcomingFlights.csv", "r", encoding="utf-8") as upcoming_file:
            all_lines = upcoming_file.readlines()
            all_upcoming = []
            
            for line in all_lines[1:]:
                line = line.split(',')
                upcoming = Model_UpcomingFlights(line[0], line[1], line[2], line[3], line[4])
                all_upcoming.append(upcoming)

        return all_upcoming