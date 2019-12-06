from LL_set_Employee import SetEmployee
from LL_set_FlightCrew import SetFlightCrew
from LL_set_Cabincrew import SetCabinCrew

class SetNewEmployee:
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

    def set_new_employee():
        ''' Prints Add new employee options
            Returns input command '''

        print('{}\n{:^44}\n{}'.format((SetNewEmployee.HEADER*SetNewEmployee.MAX), 'Add new employee', (SetNewEmployee.HEADER*SetNewEmployee.MAX)))
        
        print('\n\tC - Cabin crew',
        '\n\tF - Flight crew'
        '\n\tE - Employee\n')

        print('\n{:<15}{:^14}{:>15}'.format(SetNewEmployee.Q, SetNewEmployee.M, SetNewEmployee.B))
        print(SetNewEmployee.CHOOSE*SetNewEmployee.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command

    def set_employee_command(self):
        ''' Says where to go according to input command '''

        while self != 'Q':
            if self == 'C':
                employee_list = SetCabinCrew.set_CabinCrew()
                SetCabinCrew.set_CabinCrew_file(employee_list)

            elif self == 'F':
                employee_list = SetFlightCrew.set_FlightCrew()
                SetFlightCrew.set_FlightCrew_file(employee_list)

            elif self == 'E':
                employee_list = SetEmployee.set_Employee()
                SetEmployee.set_employee_file(employee_list)

            else:
                print("Invalid command")
                self = input('Please enter command: ').upper()


if __name__ == "__main__":
    set_emp_command = SetNewEmployee.set_new_employee()  
    SetNewEmployee.set_employee_command(set_emp_command) 