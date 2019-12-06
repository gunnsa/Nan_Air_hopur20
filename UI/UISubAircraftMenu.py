from UI.UI_List_Aircrafts import UI_List_Aircrafts

class UISubAircraftsMenu:
    def __init__(self):
        self.render()

    def render(self):
        print("-"*44)
        print("{:^44}".format('Aircrafts'))
        print("-"*44)
        print()
        print("\t1: Get all Aircrafts") #
        print("\t2: Update Aircraft information")
        print("\t3: Add new Aircraft")
        print("\tQ: Quit")
        print()

        print("_"*44)
        command = input("Enter a valid command: ")
        if command == "1":
            nextUI = UI_List_Aircrafts()
            nextUI.listAircraftTypes()
            #nextUI.listAircrafts()

        elif command == "2":
            print("not implemented")

        elif command == "3":
            print("not implemented")

        else:
            print("invalid command")