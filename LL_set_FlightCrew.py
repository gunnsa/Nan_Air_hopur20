
import csv

class SetFlightCrew:
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

    def set_FlightCrew():
        employee_list = []
        print('\n{}\n{:^44}\n{}\n'.format((SetFlightCrew.INFO*SetFlightCrew.MAX), 'Please enter information below', (SetFlightCrew.INFO*SetFlightCrew.MAX)))
        ssn = input('Social security number: ')
        employee_list.append(ssn)

        name = input('Full name: ')
        employee_list.append(name)

        status = input('Role: ') 
        employee_list.append(status)   

        status = input('Rank: ') 
        employee_list.append(status)    

        pilot_license = input('Pilot license: ')
        employee_list.append(pilot_license)

        address = input('Address: ')
        employee_list.append(address)

        phone = input('Phone: ')
        employee_list.append(phone)

        email = input('Email address: ') 
        employee_list.append(email)

        print('\n:: {} has been added to Flight crew ::'.format(name))
        return employee_list
   
    def set_FlightCrew_file(self):
        with open('Crew.csv', 'a', newline='') as destination_file:
            wr = csv.writer(destination_file, dialect='excel')#very interesting, skrifa lista inn í csv file
            wr.writerow(self)#self er semsagt listinn

if __name__ == "__main__":
    employee_list = SetFlightCrew.set_FlightCrew()
    SetFlightCrew.set_FlightCrew_file(employee_list)

# 1107951952
# Elizabeth Mcfadden
# Cabincrew
# Flight Attendant
# N/A
# Fellsmúli 35
# 8998835
# vero@nan.is
