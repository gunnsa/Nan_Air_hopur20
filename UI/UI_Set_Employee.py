from MODEL.Model_Employee import Model_Employee
from LL.LL_Set_Employee import LL_Set_Employee

class UI_Set_Employee:

    def __init__(self):
        pass

    def SetPilot(self):
        ssn = input('Social security number: ')

        name = input('Full name: ')

        role = input('Role: ') 

        rank = input('Rank: ')     

        pilot_license = input('Pilot license: ')

        address = input('Address: ')

        phone = input('Phone: ')

        email = input('Email address: ') 

        employee = Model_Employee(ssn, name, role, rank, pilot_license, address, phone, email)
        LL_Set_Employee().createEmployee(employee)
        

    def SetCabinCrew(self):
        
        ssn = input('Social security number: ')

        name = input('Full name: ')

        role = input('Role: ') 

        rank = input('Rank: ') 

        pilot_license = 'N/A'

        address = input('Address: ')

        phone = input('Phone: ')

        email = input('Email address: ') 

        employee = Model_Employee(ssn, name, role, rank, pilot_license, address, phone, email)
        LL_Set_Employee().createEmployee(employee)