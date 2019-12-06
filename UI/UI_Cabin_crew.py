from IO_AllEmployeesFromFile import EmployeeIO
from IO_List_cabincrew import AllCabinCrew
class CabinCrew:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def cabin_crew():
        ''' Prints Flight crew options
            Returns input command '''

        print('{}\n{:^44}\n{}'.format((CabinCrew.HEADER*CabinCrew.MAX), 'Cabin crew', (CabinCrew.HEADER*CabinCrew.MAX)))
        
        print('\n\tP - Print list of all Cabin crew',
        '\n\tF - Find by specific condition\n')

        print('\n{:<15}{:^14}{:>15}'.format(CabinCrew.Q, CabinCrew.M, CabinCrew.B))
        print(CabinCrew.CHOOSE*CabinCrew.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command

    def employee_command(self):
        ''' Says where to go according to input command '''

        while self != 'Q':
            if self == 'P':
                all_cabin_crew = AllCabinCrew.get_all_cabin_crew(EmployeeIO.get_emp_from_file())
                command = AllCabinCrew.display(all_cabin_crew)


            elif self == 'F':
                Find_by_specific_condition = 0

            else:
                print("Invalid command")
                self = input('Please enter command: ').upper()


if __name__ == "__main__":
    cabin_crew_command = CabinCrew.cabin_crew()  
    CabinCrew.employee_command(cabin_crew_command) 