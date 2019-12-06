from IO.IO_AllAircraftsFromFile import IO_AllAircraftsFromFile

class LL_List_AllAircrafts:

    def get_aircraftType_list(self):
        aircraftType_list = IO_AllAircraftsFromFile().get_aircraftType_from_file()
        return aircraftType_list

    def get_aircrafts_list(self):
        aircraft_list = IO_AllAircraftsFromFile().get_aircraft_from_file()
        return aircraft_list