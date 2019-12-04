from IO_AllEmployeesFromFile import EmployeeIO

class AllCabinCrew:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def get_all_cabin_crew(self):
        
        all_cabin_crew = {}
        
        for employee in self:
            if employee.role == 'Cabincrew':
                all_cabin_crew[employee.name] = employee.rank

        return all_cabin_crew

    def display(self):
        print('{}\n{:^44}\n{}'.format((AllCabinCrew.INFO*AllCabinCrew.MAX), 'List of all Cabin crew', (AllCabinCrew.INFO*AllCabinCrew.MAX)))

        for employees, rank in self.items():
            print('\t{} - {}'.format(employees, rank, end= ''))

        print('\n{:<15}{:^14}{:>15}'.format(AllCabinCrew.Q, AllCabinCrew.M, AllCabinCrew.B))
        print(AllCabinCrew.CHOOSE*AllCabinCrew.MAX)
        command = input('Please enter command: ').upper()
        print() 
        return command

    
if __name__ == "__main__":
    all_cabin_crew = AllCabinCrew.get_all_cabin_crew(EmployeeIO.get_emp_from_file())
    command = AllCabinCrew.display(all_cabin_crew)
