#from UI_Rostering import Rostering
from IO_init_Destinations import Destinations

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

class SetDestination:
    def display_main_menu():
        destination_list = []
        print('\n{}\n{:^44}\n{}\n'.format((INFO*MAX), ENTER_INFO, (INFO*MAX)))
        id_dest = input('ID: ')
        destination_list.append(id_dest)
        dest = input('Destination: ')
        destination_list.append(dest)
        flight_time = input('Flight time: ')
        destination_list.append(flight_time)
        distance = input('Distance: ')
        destination_list.append(distance)
        em_cont = input('Emergency contact: ') 
        destination_list.append(em_cont)
        em_phone = input('Emergency phone: ')
        destination_list.append(em_phone)

        print('\n:: {} has been added to destinations ::'.format(dest))
        return destination_list

    def set_destination(self):
        import csv
        with open('csv_Destinations.csv', 'a', newline='') as destination_file:
            wr = csv.writer(destination_file, dialect='excel')#very interesting, skrifa lista inn í csv file
            wr.writerow(self)#self er semsagt listinn

if __name__ == "__main__":
    new_destination = SetDestination.display_main_menu()
    SetDestination.set_destination(new_destination)



#dest, airp, date_out, flight_time_from_KEF, date_home, flight_time_to_KEF, dist, em_cont, em_phone = 
# display_main_menu()
#set_voyage(dest, airp, date_out, flight_time_from_KEF, date_home, flight_time_to_KEF, dist, em_cont, em_phone)