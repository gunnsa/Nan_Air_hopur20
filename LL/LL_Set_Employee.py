from IO.IO_AllEmployeesFromFile import IO_AllEmployeesFromFile


class LL_Set_Employee:

    def __init__(self):
        pass

    def createEmployee(self, employeeToCreate):
        IO_AllEmployeesFromFile().createEmployee(employeeToCreate)