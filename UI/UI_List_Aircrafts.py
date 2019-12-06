from LL.LL_List_AllAircrafts import LL_List_AllAircrafts

class UI_List_Aircrafts:

    def __init__(self):
        pass

    def listAllAircraftTypes(self):
        ''' PRENTAR ALLA AIRCRAFT TYPES '''
        result = LL_List_AllAircrafts().get_aircraftType_list()
        for aircraftType in result:
            print(aircraftType)

    def listAllAircrafts(self):
        ''' PRENTAR ALLA AIRCRAFTS '''
        result = LL_List_AllAircrafts().get_aircrafts_list()
        for aircrafts in result:
            print(aircrafts)