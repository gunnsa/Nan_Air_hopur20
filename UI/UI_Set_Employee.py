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

        e = Model_Employee(ssn, name, role, rank, pilot_license, address, phone, email)
        LL_Set_Employee().createEmployee(e)
        

    def SetCabinCrew(self):
        cabin_list = []
        
        ssn = input('Social security number: ')
        cabin_list.append(ssn)

        name = input('Full name: ')
        cabin_list.append(name)

        status = input('Role: ') 
        cabin_list.append(status)   

        status = input('Rank: ') 
        cabin_list.append(status)    

        pilot_license = 'N/A'
        cabin_list.append(pilot_license)

        address = input('Address: ')
        cabin_list.append(address)

        phone = input('Phone: ')
        cabin_list.append(phone)

        email = input('Email address: ') 
        cabin_list.append(email)

        #print('\n:: {} has been added to Cabin crew ::'.format(name))
        return cabin_list