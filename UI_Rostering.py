#from Destinations import Destinations
from List_destination import DestinationIO
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
<<<<<<< HEAD
                Add_new_employee  = 0
=======
                Add_new_voyage  = 0
>>>>>>> 581c82d263ab8f018087b35c3132ee7af60d0bed

            elif self == 'A':
                Add_new_destination = 0

            elif self == 'N':
                Add_new_aircraft = 0
            
            elif self == 'L':
                List_voyage = 0

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

