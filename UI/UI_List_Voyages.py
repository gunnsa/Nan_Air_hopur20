from LL.LL_List_Voyages import LL_List_Voyages
import datetime
#import dateutil.parser

class UI_List_Voyages:

    def __init__(self):
        pass

    def listPastFlights(self):
        ''' PRENTAR ALLAR PAST VINNUFERDIR '''
        result = LL_List_Voyages().get_pastFlights_list()
        for pastFlights in result:
            print(pastFlights)

    def listUpcomingFlights(self):
        ''' PRENTAR ALLAR UPCOMING VINNUFERDIR '''
        result = LL_List_Voyages().get_upcomingFlights_list()
        for upcomingFlights in result:
            print(upcomingFlights)

    def listByDateFilter(self):
        year = input("Year: ")
        month = input("Month: ")
        day = input("Day: ")
        hour = input("Hour: ")
        minute = input("Minute: ")


        print()
        result = LL_List_Voyages().get_upcomingFlights_list()
        for date in result:
            if date.departure == date_input or date.arrival.strip('\n') == date_input:
                print(date)

    def listByWeekFilter(self):
        week_input = input("Week: ")
        print()
        result = LL_List_Voyages().get_upcomingFlights_list()
        for date in result:
            if date.departure == week_input or date.arrival.strip('\n') == week_input:
                print(date)
    