from IO_AllEmployeesFromFile import EmployeeIO

class AllFlightCrew:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def get_all_pilots(self):
        
        all_Pilots = {}
        
        for employee in self:
            if employee.role == 'Pilot':
                all_Pilots[employee.name] = employee.rank

        return all_Pilots

    def display(self):
        print('{}\n{:^44}\n{}'.format((AllFlightCrew.INFO*AllFlightCrew.MAX), 'List of all Flight crew', (AllFlightCrew.INFO*AllFlightCrew.MAX)))

        for employees, rank in self.items():
            print('\t{} - {}'.format(employees, rank, end= ''))

        print('\n{:<15}{:^14}{:>15}'.format(AllFlightCrew.Q, AllFlightCrew.M, AllFlightCrew.B))
        print(AllFlightCrew.CHOOSE*AllFlightCrew.MAX)
        command = input('Please enter command: ').upper()
        print() 
        return command

    
if __name__ == "__main__":
    all_Pilots = AllFlightCrew.get_all_pilots(EmployeeIO.get_emp_from_file())
    command = AllFlightCrew.display(all_Pilots)
