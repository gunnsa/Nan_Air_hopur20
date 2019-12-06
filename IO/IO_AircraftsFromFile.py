from MODEL.Model_AircraftType import Model_AircraftType
from MODEL.Model_Aircrafts import Model_Aircrafts


class IO_AircraftsFromFile:

    def get_aircraftType_from_file(self):
        ''' Returns All Aircraft Types from file '''

        with open("AircraftType.csv", "r", encoding="utf-8") as aircraftType_file:
            all_lines = aircraftType_file.readlines()
            all_aircraftType = []
            
            for line in all_lines[1:]:
                line = line.split(',')
                aircraftType = Model_AircraftType(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10])
                all_aircraftType.append(aircraftType)

        return all_aircraftType


    def get_aircraft_from_file(self):
        ''' Returns All Aircrafts from file '''

        with open("Aircraft.csv", "r", encoding="utf-8") as aircraft_file:
            all_lines = aircraft_file.readlines()
            all_aircraft = []
            
            for line in all_lines[1:]:
                line = line.split(',')
                aircraft = Model_Aircrafts(line[0], line[1])
                all_aircraft.append(aircraft)

        return all_aircraft