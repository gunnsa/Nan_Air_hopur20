
class Employee_information:

    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def employee_info():
        print('{}\n{:^44}\n{}'.format((Employee_information.HEADER*Employee_information.MAX), 'Employee information', (Employee_information.HEADER*Employee_information.MAX)))
        
        print('\n\tC - Cabin crew',
        '\n\tF - Flight crew', 
        '\n\tA - All employees\n')

        print('\n{:<15}{:^14}{:>15}'.format(Employee_information.Q, Employee_information.M, Employee_information.B))
        print(Employee_information.CHOOSE*Employee_information.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command


if __name__ == "__main__":
    emp_info_command = Employee_information.employee_info()   
