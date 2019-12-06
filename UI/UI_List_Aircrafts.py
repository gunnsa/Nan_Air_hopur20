from LL.LL_List_Aircrafts import LL_List_Aircrafts

class UI_List_Aircrafts:

    def __init__(self):
        pass

    def listAircraftTypes(self):
        ''' PRENTAR ALLA AIRCRAFT TYPES '''
        result = LL_List_Aircrafts().get_aircraftType_list()
        for aircraftType in result:
            print(aircraftType)

    def listAircrafts(self):
        ''' PRENTAR ALLA AIRCRAFTS '''
        result = LL_List_Aircrafts().get_aircrafts_list()
        for aircrafts in result:
            print(aircrafts)