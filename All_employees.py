#from Employee import Employee

from AllEmployeesFromFile import EmployeeIO


class All_employees:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def all_emp():
        ''' Prints All employees options
            Returns input command '''
    
        print('{}\n{:^44}\n{}'.format((All_employees.HEADER*All_employees.MAX), 'All employees', (All_employees.HEADER*All_employees.MAX)))
        
        print('\n\tP - Print list of all employees', 
        '\n\tF - Find by specific condition\n')

        print('\n{:<15}{:^14}{:>15}'.format(All_employees.Q, All_employees.M, All_employees.B))
        print(All_employees.CHOOSE*All_employees.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command


    def employee_command(self):
        ''' Says where to go according to input command '''

        while self != 'Q':
            if self == 'P':
                all_employees = EmployeeIO.get_emp_from_file()
                print('{}\n{:^44}\n{}'.format((EmployeeIO.INFO*EmployeeIO.MAX), 'List of all employees', (EmployeeIO.INFO*EmployeeIO.MAX)))

                for employees in all_employees:
                    print('\t{} - {}'.format(employees.name, employees.rank, end= ''))

                print('\n{:<15}{:^14}{:>15}'.format(EmployeeIO.Q, EmployeeIO.M, EmployeeIO.B))
                print(EmployeeIO.CHOOSE*EmployeeIO.MAX)
                command = input('Please enter command: ').upper()
                print() 

            elif self == 'F':
                Find_by_specific_condition = 0

            else:
                print("Invalid command")
                self = input('Please enter command: ').upper()


if __name__ == "__main__":
    all_emp_command = All_employees.all_emp()  
    All_employees.employee_command(all_emp_command) 
