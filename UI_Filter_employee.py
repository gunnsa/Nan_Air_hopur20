from IO_AllEmployeesFromFile import EmployeeIO
from UI_filter_by_name import FilterByName
from UI_filter_by_ssn import FilterBySSN

class FilterEmployee:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def specific_condition():
        ''' Prints Find by specific condition options
            Returns input command '''
    
        print('{}\n{:^44}\n{}'.format((FilterEmployee.HEADER*FilterEmployee.MAX), 'Find by specific condition', (FilterEmployee.HEADER*FilterEmployee.MAX)))
        
        print('\n\tN - Find employee by name', 
        '\n\tS - Find employee by social security number\n')

        print('\n{:<15}{:^14}{:>15}'.format(FilterEmployee.Q, FilterEmployee.M, FilterEmployee.B))
        print(FilterEmployee.CHOOSE*FilterEmployee.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command

    def employee_command(self):
        ''' Says where to go according to input command '''

        while self != 'Q':
            if self == 'N':
                emp_name = FilterByName.specific_name()
                FilterByName.find_employee(EmployeeIO.get_emp_from_file(), emp_name)

            elif self == 'S':
                emp_ssn = FilterBySSN.specific_ssn()
                FilterBySSN.find_employee(EmployeeIO.get_emp_from_file(), emp_ssn)

            else:
                print("Invalid command")
                self = input('Please enter command: ').upper()


if __name__ == "__main__":
    all_emp_command = FilterEmployee.specific_condition()
    FilterEmployee.employee_command(all_emp_command)
