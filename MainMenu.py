
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

if __name__ == "__main__":
    menu_command = MainMenu.Menu()





