from IO.IO_EmployeesFromFile import IO_EmployeesFromFile

class LL_List_Employees:

    def get_crew_list(self):
        crew_list = IO_EmployeesFromFile().get_emp_from_file()
        return crew_list

    def get_Pilots(self, pilot):
        allCrew = self.get_crew_list()
        retList = []
        for PilotMember in allCrew:
            if pilot == PilotMember.role:
                retList.append(PilotMember.name)
                retList.append(PilotMember.rank)
        return retList

    def get_Cabin(self, cabin):
        allCrew = self.get_crew_list()
        retList = []
        for CabinMember in allCrew:
            if cabin== CabinMember.role:
                retList.append(CabinMember.name)
                retList.append(CabinMember.rank)
        return retList  


    def getOneEmployee(self, userName):
        allCrew = self.get_crew_list()
        retList = []
        for elem in allCrew:
            if userName in elem.name:
                retList.append(elem)
        return retList
