from UI_All_employees import All_employees
from UI_Flight_crew import FlightCrew
from UI_Cabin_crew import CabinCrew


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
        ''' Prints Employee information options
            Returns input command '''

        print('{}\n{:^44}\n{}'.format((Employee_information.HEADER*Employee_information.MAX), 'Employee information', (Employee_information.HEADER*Employee_information.MAX)))
        
        print('\n\tC - Cabin crew',
        '\n\tF - Flight crew', 
        '\n\tA - All employees\n')

        print('\n{:<15}{:^14}{:>15}'.format(Employee_information.Q, Employee_information.M, Employee_information.B))
        print(Employee_information.CHOOSE*Employee_information.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command

    def info_command(self):
        ''' Says where to go according to input command '''

        while self != 'Q':
            if self == 'C':
                flight_crew_command = CabinCrew.flight_crew()  
                CabinCrew.employee_command(flight_crew_command)
                    
            elif self == 'F':
                flight_crew_command = FlightCrew.flight_crew()  
                FlightCrew.employee_command(flight_crew_command) 
                    
            elif self == 'A':
                all_emp_command = All_employees.all_emp()  
                All_employees.employee_command(all_emp_command)

            else:
                print("Invalid command")
                self = input('Please enter command: ').upper()


if __name__ == "__main__":
    emp_info_command = Employee_information.employee_info()   
    Employee_information.info_command(emp_info_command)
