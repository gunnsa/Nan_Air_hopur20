from Employee_information import Employee_information
class List_of_employees:

    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def list_employees():
        print('{}\n{:^44}\n{}'.format((List_of_employees.HEADER*List_of_employees.MAX), 'List of employees', (List_of_employees.HEADER*List_of_employees.MAX)))
        
        print('\n\tI - Employee information', 
        '\n\tD - Destinations\n')

        print('\n{:<15}{:^14}{:>15}'.format(List_of_employees.Q, List_of_employees.M, List_of_employees.B))
        print(List_of_employees.CHOOSE*List_of_employees.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command

    def employee_command(self):
        while self != 'Q':
            if self == 'I':
                emp_info_command = Employee_information.employee_info()   
                Employee_information.info_command(emp_info_command)

            elif self == 'D':
                Destinations = 0

            else:
                print("Invalid command")
                self = input('Please enter command: ').upper()


if __name__ == "__main__":
    emp_list = List_of_employees.list_employees()
    List_of_employees.employee_command(emp_list)  
