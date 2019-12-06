class Model_AircraftType:
    def __init__(self, planeTypeId, manufacturer, model, capacity, emptyWeight, maxTakeoffWeight, unitThrust, serviceCeiling, length, height, wingspan):
        self.planeTypeId = planeTypeId
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.emptyWeight = emptyWeight
        self.maxTakeoffWeight = maxTakeoffWeight
        self.unitThrust = unitThrust
        self.serviceCeiling = serviceCeiling
        self.length = length
        self.height = height
        self.wingspan = wingspan

    def __str__(self):
        retString = ""
        retString += self.planeTypeId + " "
        retString += self.manufacturer + " "
        retString += self.model + " "
        retString += self.capacity + " "
        retString += self.emptyWeight + " "
        retString += self.maxTakeoffWeight + " "
        retString += self.unitThrust + " "
        retString += self.serviceCeiling + " "
        retString += self.length + " "
        retString += self.height + " "
        retString += self.wingspan + " "
        return retString