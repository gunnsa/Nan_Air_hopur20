from UI.UI_List_Destinations import UI_List_Destinations

class UISubDestinationMenu:
    def __init__(self):
        self.render()

    def render(self):
        print("-"*44)
        print("{:^44}".format('Destinations'))
        print("-"*44)
        print()
        print("\t1: Get all Destinations") #
        print("\t2: Update Destination information")
        print("\t3: Add new Destination")
        print("\tQ: Quit")
        print()
        
        print("_"*44)
        command = input("Enter a valid command: ")
        if command == "1":
            nextUI = UI_List_Destinations()
            nextUI.listDestinations()

        elif command == "2":
            print("not implemented")

        elif command == "3":
            print("not implemented")

        else:
            print("invalid command")