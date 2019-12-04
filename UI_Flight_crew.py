from IO_AllEmployeesFromFile import EmployeeIO
from IO_List_cabincrew import AllCabinCrew
class FlightCrew:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def flight_crew():
        ''' Prints Flight crew options
            Returns input command '''

        print('{}\n{:^44}\n{}'.format((FlightCrew.HEADER*FlightCrew.MAX), 'Flight crew', (FlightCrew.HEADER*FlightCrew.MAX)))
        
        print('\n\tP - Print list of all Flight crew',
        '\n\tF - Find by specific condition\n')

        print('\n{:<15}{:^14}{:>15}'.format(FlightCrew.Q, FlightCrew.M, FlightCrew.B))
        print(FlightCrew.CHOOSE*FlightCrew.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command

    def employee_command(self):
        ''' Says where to go according to input command '''

        while self != 'Q':
            if self == 'P':
                all_Pilots = AllCabinCrew.get_all_cabin_crew(EmployeeIO.get_emp_from_file())
                command = AllCabinCrew.display(all_Pilots)


            elif self == 'F':
                Find_by_specific_condition = 0

            else:
                print("Invalid command")
                self = input('Please enter command: ').upper()


if __name__ == "__main__":
    flight_crew_command = FlightCrew.flight_crew()  
    FlightCrew.employee_command(flight_crew_command) 