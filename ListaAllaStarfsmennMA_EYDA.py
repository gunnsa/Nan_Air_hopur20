# Lista alla starfsmenn - Notkunartilvik nr 2
#   Nafn - Starfsheiti (rank)
#       Captain
#       Copilot
#       Flight Service Manager
#       Flight Attendant

from Employee import Employee

class EmployeeIO:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def get_emp_from_file():
        path = "Crew.csv"
        with open(path, "r", encoding="utf-8") as crew_file:
            all_lines = crew_file.readlines()
            all_emps = []
            
            for line in all_lines[1:]:
                line = line.split(',')
                emp = Employee(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                all_emps.append(emp)

        return all_emps

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
    all_employees = EmployeeIO.get_emp_from_file()
    command = EmployeeIO.display(all_employees)
    EmployeeIO.emp_command(command)
    
 
