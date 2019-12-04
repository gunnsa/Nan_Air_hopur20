# Lista alla flugmenn - Notkunartilvik nr 4
#   Nafn - Starfsheiti (rank)
#       Captain
#       Copilot

class Employee:
    def __init__(self, ssn, name, role, rank, licens, address, phonenumber):
        self.ssn = ssn
        self.name = name
        self.role = role
        self.rank = rank
        self.licens = licens
        self.address = address
        self.phonenumber = phonenumber

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

        return all_emps
    
    def get_all_pilots(self):
        
        all_Pilots = {}
        
        for employee in all_emps:
            if employee.role == 'Pilot':
                all_Pilots[employee.name] = employee.rank

        return all_Pilots


if __name__ == "__main__":
    all_emps = EmployeeIO.get_emp_from_file()
    all_Pilots = EmployeeIO.get_all_pilots(all_emps)
    for employee, rank in all_Pilots.items():
        print('\n{} - {}'.format(employee, rank, end= ''))