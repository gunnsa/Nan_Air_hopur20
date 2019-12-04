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

def display_main_menu():
    print('\n{:^44}\n'.format(WELCOME))
    print('{}\n{:^44}\n{}'.format((HEADER*MAX), MAINMENU, (HEADER*MAX)))

def display_main_menu_options():
    print('\n\tQ - Quit', 
    '\n\tC - Cabin office', 
    '\n\tR - Rostering', 
    '\n\t? - Help\n')

def display_input():
    print(CHOOSE*MAX)
    command = input('Please enter command: ').upper()
    print()
    if command == 'C':
        # open Cabin Office
        Cabin_Office()

    elif command == 'R':
        # open Rostering
        Rostering()


def Rostering():
    print('{}\n{:^44}\n{}'.format((HEADER*MAX), 'Rostering ', (HEADER*MAX)))

    print('\n\tV - Add new voyage', 
    '\n\tA - Add new destination',
    '\n\tN - Add new aircraft', 
    '\n\tL - List voyage', 
    '\n\tD - List destinations', 
    '\n\tF - List aircrafts',
    '\n\tC - Change information\n')

    print('\n{:<15}{:^14}{:>15}'.format(Q, M, B))
    print(CHOOSE*MAX)
    command = input('Please enter command: ').upper()
    print()

def Cabin_Office():
    print('{}\n{:^44}\n{}'.format((HEADER*MAX), 'Cabin Office', (HEADER*MAX)))

    print('\n\tA - Add new employee', 
    '\n\tC - Change employee information',
    '\n\tL - List of employees', 
    '\n\tV - Voyage\n')

    print('\n{:<15}{:^14}{:>15}'.format(Q, M, B))
    print(CHOOSE*MAX)
    command = input('Please enter command: ').upper()
    print()

    
display_main_menu()
display_main_menu_options()
display_input()




