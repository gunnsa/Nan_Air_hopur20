# Lista alla flugthjona - Notkunartilvik nr 6
#   Nafn - Starfsheiti (rank)
#       Flight Service Manager
#       Flight Attendant

#from ListaAllaStarfsmenn import EmployeeIO

from AllEmployeesFromFile import EmployeeIO


class AllFlightCrew:
        
        all_cabincrew = {}
        
        for employee in all_emps:
            if employee.role == 'Cabincrew':
                all_cabincrew[employee.name] = employee.rank

        return all_cabincrew

if __name__ == "__main__":
    all_cabincrew = EmployeeIO.get_emp_from_file()
    for employee, rank in all_cabincrew.items():
        print('\n{} - {}'.format(employee, rank, end= ''))
