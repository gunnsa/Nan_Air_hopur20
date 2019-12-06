# VAR SEINNI HLUTI AF ListaAllaStarfsmenn.py !!!!!!

from IO_AllEmployeesFromFile import EmployeeIO

from 

class AllEmployees:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def get_crew_list(self):
        crew_list = EmployeeIO().get_emp_from_file()
        return crew_list



    # færa í UI list of employees
    '''def display(self):
        print('{}\n{:^44}\n{}'.format((AllEmployees.INFO*AllEmployees.MAX), 'List of all employees', (AllEmployees.INFO*AllEmployees.MAX)))

        for employees in self:
            print('\t{} - {}'.format(employees.name, employees.rank, end= ''))

        print('\n{:<15}{:^14}{:>15}'.format(AllEmployees.Q, AllEmployees.M, AllEmployees.B))
        print(AllEmployees.CHOOSE*AllEmployees.MAX)
        command = input('Please enter command: ').upper()
        print() 
        return command

    def emp_command(self):
        if self == 'Q':
            pass '''



if __name__ == "__main__":
    get_crew_list()

    '''command = AllEmployees.display(EmployeeIO.get_emp_from_file())
    AllEmployees.emp_command(command)'''

