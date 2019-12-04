from AllEmployeesFromFile import EmployeeIO

class AllEmployees:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'
    
    def display(self):
        print('{}\n{:^44}\n{}'.format((EmployeeIO.INFO*EmployeeIO.MAX), 'List of all employees', (EmployeeIO.INFO*EmployeeIO.MAX)))

        for employees in self:
            print('\t{} - {}'.format(employees.name, employees.rank, end= ''))

        print('\n{:<15}{:^14}{:>15}'.format(EmployeeIO.Q, EmployeeIO.M, EmployeeIO.B))
        print(EmployeeIO.CHOOSE*EmployeeIO.MAX)
        command = input('Please enter command: ').upper()
        print() 
        return command

    def emp_command(self):
        #while self != 'Q':
        if self == 'Q':
            pass

if __name__ == "__main__":
    command = AllEmployees.display(EmployeeIO.get_emp_from_file())
    AllEmployees.emp_command(command)

