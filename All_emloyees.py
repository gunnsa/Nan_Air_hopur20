#from Employee import Employee

from ListaAllaStarfsmenn import EmployeeIO


class All_emloyees:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def all_emp():
        print('{}\n{:^44}\n{}'.format((All_emloyees.HEADER*All_emloyees.MAX), 'All employees', (All_emloyees.HEADER*All_emloyees.MAX)))
        
        print('\n\tP - Print list of all employees', 
        '\n\tF - Find by specific condition\n')

        print('\n{:<15}{:^14}{:>15}'.format(All_emloyees.Q, All_emloyees.M, All_emloyees.B))
        print(All_emloyees.CHOOSE*All_emloyees.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command


    def employee_command(self):
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
    all_emp_command = All_emloyees.all_emp()  
    All_emloyees.employee_command(all_emp_command) 
