from UI.UISubEmployeeMenu import UISubEmployeeMenu
from UI.UISubDestinationsMenu import UISubDestinationMenu
from UI.UISubAircraftMenu import UISubAircraftsMenu
from UI.UISubVoyageMenu import UISubVoyageMenu

class UIMain:
    def __init__(self):
        self.render()

    def render(self):
        while True:
            print("-"*44)
            print("{:^44}".format('Main menu'))
            print("-"*44)
            print()
            print("\t1: Employee")
            print("\t2: Voyage")
            print("\t3: Aircrafts")
            print("\t4: Destinations")
            print("\tq: Quit")
            print()

            print("_"*44)
            command = input("Enter a valid command: ")
            print()
            if command == "1":
                UISubEmployeeMenu()

            elif command == "2":
                UISubVoyageMenu()

            elif command == "3":
                UISubAircraftsMenu()

            elif command == "4":
                UISubDestinationMenu()

            elif command == "q":
                break

            else:
                print("invalid command")