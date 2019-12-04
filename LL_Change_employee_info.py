

class Change_Employee_information:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def Change_employee_information():
        ''' Prints Change employee information options
            Returns input command '''

        print('{}\n{:^44}\n{}'.format((Change_Employee_information.HEADER*Change_Employee_information.MAX), 'Change employee information', (Change_Employee_information.HEADER*Change_Employee_information.MAX)))
        
        print('\n\tP - Print list of all Cabin crew',
        '\n\tF - Find by specific condition\n')

        print('\n{:<15}{:^14}{:>15}'.format(Change_Employee_information.Q, Change_Employee_information.M, Change_Employee_information.B))
        print(Change_Employee_information.CHOOSE*Change_Employee_information.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command

if __name__ == "__main__":
    employee_info_command = Change_Employee_information.Change_employee_information()
