from LL_List_destination import DestinationIO
from LL_set_destination import SetDestination
from IO_List_Voyage import VoyageIO
class Rostering:

    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def Rostering_office():
        
        print('{}\n{:^44}\n{}'.format((Rostering.HEADER*Rostering.MAX), 'Rostering', (Rostering.HEADER*Rostering.MAX)))

        print('\n\tV - Add new voyage', 
        '\n\tA - Add new destination',
        '\n\tN - Add new aircraft', 
        '\n\tL - List voyage', 
        '\n\tD - List destinations', 
        '\n\tF - List aircrafts',
        '\n\tC - Change information\n')

        print('\n{:<15}{:^14}{:>15}'.format(Rostering.Q, Rostering.M, Rostering.B))
        print(Rostering.CHOOSE*Rostering.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command

    def rostering_command(self):
        while self != 'Q':
            if self == 'V':
                Add_new_voyage  = 0

            elif self == 'A':
                new_destination = SetDestination.display_main_menu()
                SetDestination.set_destination(new_destination)

            elif self == 'N':
                Add_new_aircraft = 0
            
            elif self == 'L':
                all_voyages = VoyageIO.get_voyage()
                VoyageIO.display(all_voyages)

            elif self == 'D':
                all_destinations = DestinationIO.get_dest_from_file()
                DestinationIO.display(all_destinations)

            elif self == 'F':
                List_aircrafts = 0

            elif self == 'C':
                Change_information = 0

            else:
                print("Invalid command")
                self = input('Please enter command: ').upper()

if __name__ == "__main__":
    rostering_com = Rostering.Rostering_office()
    Rostering.rostering_command(rostering_com)

