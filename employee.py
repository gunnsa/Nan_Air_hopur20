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
                print(line)
                all_emps.append(emp)
        return all_emps


if __name__ == "__main__":
    emps = EmployeeIO.get_emp_from_file()
    for employee in emps:
        print(employee.name)
