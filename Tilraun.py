from MainMenu import MainMenu
from CabinOffice import CabinOffice
from Rostering import Rostering

game_on = True
if __name__ == "__main__":
    menu_command = MainMenu.Menu()
    if menu_command == 'C':
        cabin_command = CabinOffice.Cabin_office()

    elif menu_command == 'R':
        rostering_command = Rostering.Rostering_office()

    elif menu_command == 'Q':
        game_on = False


    