from UI.UI_List_Employees import UI_List_Employees
from UI.UI_Set_Employee import UI_Set_Employee

class UISubEmployeeMenu:
    def __init__(self):
        self.render()

    def render(self):
        print("-"*44)
        print("{:^44}".format('Employees'))
        print("-"*44)
        print()
        print("\t1: Get all employees") #
        print("\t2: Get all pilots") #
        print("\t3: Get all cabincrew") #
        print("\t4: Get information on employee")
        print("\t5: Create Cabin Crew")
        print("\t6: Create Pilot")
        print("\t7: Update employee")
        print("\tq: Quit")
        print()

        print("_"*44)
        command = input("Enter a valid command: ")
        if command == "1":
            ''' PRENTAR ALLA STARFSMENN '''
            nextUI = UI_List_Employees()
            nextUI.listAllEmployees()

        elif command == "2":
            ''' PRENTAR ALLA PILOTS '''
            nextUI = UI_List_Employees()
            nextUI.listAllPilots()

        elif command == "3":
            ''' PRENTAR ALLA CABIN CREW '''
            nextUI = UI_List_Employees()
            nextUI.listAllCabinCrew()

        elif command == "4":
            ''' PRENTAR UPPL. UM AKVEDINN STARFSMANN '''
            #input hvern viltu leita eftir
            nextUI = UI_List_Employees()
            nextUI.listByFilter()

        elif command == "5":
            nextUI = UI_Set_Employee()
            nextUI.SetCabinCrew()

        elif command == "6":
            nextUI = UI_Set_Employee()
            nextUI.SetPilot()

        elif command == "7":
            print("not implemented")

        else:
            print("invalid command")