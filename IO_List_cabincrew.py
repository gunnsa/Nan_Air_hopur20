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
        
        all_cabincrew = {}
        
        for employee in all_emps:
            if employee.role == 'Cabincrew':
                all_cabincrew[employee.name] = employee.rank

        return all_cabincrew

if __name__ == "__main__":
    all_cabincrew = EmployeeIO.get_emp_from_file()
    for employee, rank in all_cabincrew.items():
        print('\n{} - {}'.format(employee, rank, end= ''))
