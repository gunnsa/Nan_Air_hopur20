from List_of_employees import List_of_employees

class CabinOffice:

    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def Cabin_office():
        
        print('{}\n{:^44}\n{}'.format((CabinOffice.HEADER*CabinOffice.MAX), 'Cabin Office', (CabinOffice.HEADER*CabinOffice.MAX)))

        print('\n\tA - Add new employee', 
        '\n\tC - Change employee information',
        '\n\tL - List of employees', 
        '\n\tV - Voyage\n')

        print('\n{:<15}{:^14}{:>15}'.format(CabinOffice.Q, CabinOffice.M, CabinOffice.B))
        print(CabinOffice.CHOOSE*CabinOffice.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command

    def cabin_command(self):
        if cabin == 'A':
            Add_new_employee  = 0

        elif cabin == 'C':
            Change_employee_information = 0

        elif cabin == 'L':
            emp_list = List_of_employees.list_employees()
        
        elif cabin == 'V':
            voyage = 0

if __name__ == "__main__":
    cabin = CabinOffice.Cabin_office()
    CabinOffice.cabin_command(cabin)


