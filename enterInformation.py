WELCOME = "WELCOME TO NaN AIR"
MAINMENU = 'MAIN MENU'
ENTER_INFO = 'Please enter information below'
HEADER = '#'    # 44
INFO = '*'      # 44
CHOOSE = '_'    # 44
COMMENT = ':'   # 2
MAX = 44
B = 'B - Go back'
M = 'M - Main menu'
Q = 'Q - Quit'

def display_main_menu():
    print('\n{}\n{:^44}\n{}\n'.format((INFO*MAX), ENTER_INFO, (INFO*MAX)))
    dest = input('Destination: ')
    input('Airport: ') 
    input('Flight time: ') 
    input('Distance: ') 
    input('Emergency contact: ') 
    input('Emergency phone: ')
    print('\n:: {} has been added to flight route ::'.format(dest))

display_main_menu()