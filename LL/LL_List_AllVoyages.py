from IO.IO_AllVoyagesFromFile import IO_AllVoyagesFromFile
#import datetime
#import dateutil.parser

class LL_List_AllVoyages:

    def get_pastFlights_list(self):
        pastFlight_list = IO_AllVoyagesFromFile().get_pastFlights_from_file()
        return pastFlight_list

    def get_upcomingFlights_list(self):
        upcomingFlight_list = IO_AllVoyagesFromFile().get_upcomingFlights_from_file()
        return upcomingFlight_list

    def date_time(self):
        pastFlight_list = IO_AllVoyagesFromFile().get_pastFlights_from_file()
        for line in pastFlight_list:
            date = dateutil.parser.parse(line.departure)          
        return date


