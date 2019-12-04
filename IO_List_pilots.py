#from IO_init_Employee import Employee
from IO_AllEmployeesFromFile import EmployeeIO
from LL_List_AllEmployees import AllEmployees
class AllCabinCrew(EmployeeIO):
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
        print('{}\n{:^44}\n{}'.format((AllCabinCrew.INFO*AllCabinCrew.MAX), 'List of all Cabin crew', (AllCabinCrew.INFO*AllCabinCrew.MAX)))

        for employees, rank in self.items():
            print('\t{} - {}'.format(employees.name, employees.rank, end= ''))

        print('\n{:<15}{:^14}{:>15}'.format(AllCabinCrew.Q, AllCabinCrew.M, AllCabinCrew.B))
        print(AllCabinCrew.CHOOSE*AllCabinCrew.MAX)
        command = input('Please enter command: ').upper()
        print() 
        return command

    
if __name__ == "__main__":
    all_Pilots = AllCabinCrew.get_all_pilots(EmployeeIO.get_emp_from_file())
    command = AllCabinCrew.display(all_Pilots)
