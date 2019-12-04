from CabinOffice import CabinOffice
from Rostering import Rostering
from List_of_employees import List_of_employees

class MainMenu:

    WELCOME = "WELCOME TO NaN AIR"
    MAINMENU = 'MAIN MENU'
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def Menu():
        print('\n{:^44}\n'.format(MainMenu.WELCOME))
        print('{}\n{:^44}\n{}'.format((MainMenu.HEADER*MainMenu.MAX), MainMenu.MAINMENU, (MainMenu.HEADER*MainMenu.MAX)))


        print('\n\tQ - Quit', '\n\tC - Cabin office', '\n\tR - Rostering', '\n\tH - Help\n')

        print(MainMenu.CHOOSE*MainMenu.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command
        #print('\n{:<15}{:^14}{:>15}'.format(MainMenu.Q, MainMenu.M, MainMenu.B))

    def menu_command(self):
        if menu_command == 'C':
            cabin = CabinOffice.Cabin_office()
            CabinOffice.cabin_command(cabin)

        elif menu_command == 'R':
            rostering_command = Rostering.Rostering_office()

        elif menu_command == 'Q':
            game_on = False

if __name__ == "__main__":
    menu_command = MainMenu.Menu()
    MainMenu.menu_command(menu_command)





