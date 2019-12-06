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
        result = LL_List_Employees().get_crew_list()
        for PilotMember in result:
            if PilotMember.role == 'Pilot':
                print(PilotMember.name, PilotMember.rank)

    def listCabinCrew(self):
        ''' PRENTAR ALLA CABIN CREW '''
        result = LL_List_Employees().get_crew_list()
        for CabinMember in result:
            if CabinMember.role == 'Cabincrew':
                print(CabinMember.name, CabinMember.rank)

    def listByFilter(self):
        ''' PRENTAR ALLA STARFSMENN EFTIR AKVEDNU NAFNI '''
        name_input = input("Name: ")
        usersWithName = LL_List_Employees().getOneEmployee(name_input)
        if len(usersWithName) == 0:
            print("no user with that name")
        else:
            for elem in usersWithName:
                print(elem)
        

