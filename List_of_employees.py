
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


if __name__ == "__main__":
    emp_list = List_of_employees.list_employees()   
