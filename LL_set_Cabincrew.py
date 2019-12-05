
import csv

class SetCabinCrew:
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

    def set_CabinCrew():
        employee_list = []
        print('\n{}\n{:^44}\n{}\n'.format((SetCabinCrew.INFO*SetCabinCrew.MAX), 'Please enter information below', (SetCabinCrew.INFO*SetCabinCrew.MAX)))
        ssn = input('Social security number: ')
        employee_list.append(ssn)

        name = input('Full name: ')
        employee_list.append(name)

        status = input('Role: ') 
        employee_list.append(status)   

        status = input('Rank: ') 
        employee_list.append(status)    

        pilot_license = 'N/A'
        employee_list.append(pilot_license)

        address = input('Address: ')
        employee_list.append(address)

        phone = input('Phone: ')
        employee_list.append(phone)

        email = input('Email address: ') 
        employee_list.append(email)

        print('\n:: {} has been added to Cabin crew ::'.format(name))
        return employee_list
   
    def set_CabinCrew_file(self):
        with open('Crew.csv', 'a', newline='') as destination_file:
            wr = csv.writer(destination_file, dialect='excel')#very interesting, skrifa lista inn í csv file
            wr.writerow(self)#self er semsagt listinn

if __name__ == "__main__":
    employee_list = SetCabinCrew.set_CabinCrew()
    SetCabinCrew.set_CabinCrew_file(employee_list)

# 1107951952
# Elizabeth Mcfadden
# Cabincrew
# Flight Attendant
# N/A
# Fellsmúli 35
# 8998835
# vero@nan.is
