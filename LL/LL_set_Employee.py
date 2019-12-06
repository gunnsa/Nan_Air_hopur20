from IO.IO_EmployeesFromFile import IO_EmployeesFromFile


class LL_Set_Employee:

    def __init__(self):
        pass

    def createEmployee(self, employeeToCreate):
        IO_EmployeesFromFile().addEmployeeToFile(employeeToCreate)