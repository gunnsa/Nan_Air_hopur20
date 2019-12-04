# VAR FYRRI HLUTI AF ListaAllaStarfsmenn.py !!!!!!

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
        ''' Returns All employees from file '''

        path = "Crew.csv"
        with open(path, "r", encoding="utf-8") as crew_file:
            all_lines = crew_file.readlines()
            all_emps = []
            
            for line in all_lines[1:]:
                line = line.split(',')
                emp = Employee(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                all_emps.append(emp)

        return all_emps


if __name__ == "__main__":
    all_employees = EmployeeIO.get_emp_from_file()

    
 
