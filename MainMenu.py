from CabinOffice import CabinOffice
from Rostering import Rostering

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
        ''' Prints Welcome and Main Menu options
            Returns input command '''

        print('\n{:^44}\n'.format(MainMenu.WELCOME))
        print('{}\n{:^44}\n{}'.format((MainMenu.HEADER*MainMenu.MAX), MainMenu.MAINMENU, (MainMenu.HEADER*MainMenu.MAX)))

        print('\n\tQ - Quit', '\n\tC - Cabin office', '\n\tR - Rostering', '\n\tH - Help\n')

        print(MainMenu.CHOOSE*MainMenu.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command

    def menu_command(self):
        ''' Says where to go according to input command '''
        
        while self != 'Q':
            if self == 'C':
                cabin = CabinOffice.Cabin_office()
                CabinOffice.cabin_command(cabin)

            elif self == 'R':
                rostering = Rostering.Rostering_office()
                Rostering.rostering_command(rostering)

            elif self == 'Q':
                game_on = False

            else:
                print("Invalid command")
                self = input('Please enter command: ').upper()

if __name__ == "__main__":
    menu_command = MainMenu.Menu()
    MainMenu.menu_command(menu_command)





