# Lista alla flugthjona - Notkunartilvik nr 6
#   Nafn - Starfsheiti (rank)
#       Flight Service Manager
#       Flight Attendant

from Employee import Employee

class EmployeeIO:
    def get_emp_from_file():
        path = "Crew.csv"
        with open(path, "r", encoding="utf-8") as crew_file:
            all_lines = crew_file.readlines()
            all_emps = []
            
            for line in all_lines[1:]:
                line = line.split(',')
                emp = Employee(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                all_emps.append(emp)
        
        all_cabincrew = {}
        
        for employee in all_emps:
            if employee.role == 'Cabincrew':
                all_cabincrew[employee.name] = employee.rank

        return all_cabincrew

if __name__ == "__main__":
    all_cabincrew = EmployeeIO.get_emp_from_file()
    for employee, rank in all_cabincrew.items():
        print('\n{} - {}'.format(employee, rank, end= ''))
