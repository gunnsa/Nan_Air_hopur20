from LL.LL_List_Employees import LL_List_Employees

class UI_List_Employees:

    def __init__(self):
        pass

    def listEmployees(self):
        ''' PRENTAR ALLA STARFSMENN '''
        result = LL_List_Employees().get_crew_list()
        for crewMember in result:
            print(crewMember.name, crewMember.rank)

    def listPilots(self):
        ''' PRENTAR ALLA PILOTS '''
        pilot_str = 'Pilot'
        pilot_list = LL_List_Employees().get_Pilots(pilot_str)
        for pilot in pilot_list:
            print(pilot)


    def listCabinCrew(self):
        ''' PRENTAR ALLA CABIN CREW '''
        cabin_str = 'Cabincrew'
        cabin_list = LL_List_Employees().get_Cabin(cabin_str)
        for cabin in cabin_list:
            print(cabin)


    def listByFilter(self):
        ''' PRENTAR ALLA STARFSMENN EFTIR AKVEDNU NAFNI '''
        name_input = input("Name: ")
        usersWithName = LL_List_Employees().getOneEmployee(name_input)
        if len(usersWithName) == 0:
            print("no user with that name")
        else:
            for elem in usersWithName:
                print(elem)
        

