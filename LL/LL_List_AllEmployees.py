from IO.IO_AllEmployeesFromFile import IO_AllEmployeesFromFile

class LL_List_AllEmployees:

    def get_crew_list(self):
        crew_list = IO_AllEmployeesFromFile().get_emp_from_file()
        return crew_list

    def getOneEmployee(self, userName):
        allCrew = self.get_crew_list()
        retList = []
        for elem in allCrew:
            if userName in elem.name:
                retList.append(elem)
        return retList