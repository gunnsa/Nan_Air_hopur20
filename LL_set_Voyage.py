
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

class SetVoyage:
    def display_main_menu():
        voyage_list = []
        print('\n{}\n{:^44}\n{}\n'.format((INFO*MAX), ENTER_INFO, (INFO*MAX)))
        dest = input('Destination: ')
        voyage_list.append(dest)
        airp = input('Airport: ')
        voyage_list.append(airp)
        date_out = input('Date from KEF: ')
        voyage_list.append(date_out)
        flight_time_from_KEF = input('Time of departure from KEF: ')
        voyage_list.append(flight_time_from_KEF)
        date_home = input('Date to KEF: ')
        voyage_list.append(date_home)
        flight_time_to_KEF = input('Time of departure from destination to KEF: ') 
        voyage_list.append(flight_time_to_KEF)
        dist = input('Distance: ')
        voyage_list.append(dist)
        em_cont = input('Emergency contact: ') 
        voyage_list.append(em_cont)
        em_phone = input('Emergency phone: ')
        voyage_list.append(em_phone)
        print('\n:: {} has been added to flight route ::'.format(dest))
        return voyage_list


    def set_voyage(self):
        import csv
        with open('Voyage.csv', 'a', newline='') as voyage_file:
            wr = csv.writer(voyage_file, dialect='excel')#very interesting, skrifa lista inn í csv file
            wr.writerow(self)#self er semsagt listinn

if __name__ == "__main__":
    new_voyage = SetVoyage.display_main_menu()
    SetVoyage.set_voyage(new_voyage)



#dest, airp, date_out, flight_time_from_KEF, date_home, flight_time_to_KEF, dist, em_cont, em_phone = 
# display_main_menu()
#set_voyage(dest, airp, date_out, flight_time_from_KEF, date_home, flight_time_to_KEF, dist, em_cont, em_phone)