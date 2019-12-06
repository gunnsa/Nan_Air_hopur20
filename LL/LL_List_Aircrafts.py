from IO.IO_AircraftsFromFile import IO_AircraftsFromFile

class LL_List_Aircrafts:

    def get_aircraftType_list(self):
        aircraftType_list = IO_AircraftsFromFile().get_aircraftType_from_file()
        return aircraftType_list

    def get_aircrafts_list(self):
        aircraft_list = IO_AircraftsFromFile().get_aircraft_from_file()
        return aircraft_list