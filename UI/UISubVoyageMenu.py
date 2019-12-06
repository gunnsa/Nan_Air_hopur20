from UI.UI_List_Voyages import UI_List_Voyages

class UISubVoyageMenu:
    def __init__(self):
        self.render()

    def render(self):
        print("-"*44)
        print("{:^44}".format('Voyage'))
        print("-"*44)
        print()
        print("\t1: Get all Voyages")
        print("\t2: Get all Voyages on specific date")
        print("\t3: Get all Voyages on specific week")
        print("\t4: Update Voyage information")
        print("\t5: Add new Voyage")
        print("\tQ: Quit")
        print()

        print("_"*44)
        command = input("Enter a valid command: ")
        print()
        if command == "1":
            nextUI = UI_List_Voyages()
            #nextUI.listPastFlights()
            nextUI.listUpcomingFlights()

        elif command == "2":
            nextUI = UI_List_Voyages()
            nextUI.listByDateFilter()

        elif command == "3":
            nextUI = UI_List_Voyages()
            nextUI.ath()

        elif command == "4":
            print("not implemented")

        elif command == "5":
            print("not implemented")

        else:
            print("invalid command")