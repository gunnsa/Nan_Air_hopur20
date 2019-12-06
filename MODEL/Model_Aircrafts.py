class Model_Aircrafts:
    def __init__(self, planeInsignia, planeTypeId):
        self.Insignia = planeInsignia
        self.TypeId = planeTypeId

    def __str__(self):
        retString = ""
        retString += self.Insignia + " "
        retString += self.TypeId + " "
        return retString