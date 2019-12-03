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
    # all_emps = []
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
        all_pilots = []
        all_cabincrew = []
        for employee in all_emps:
            # print(line)
            if employee.role == 'Pilot':
                all_pilots.append(employee.name)
            else:
                all_cabincrew.append(employee.name)
        print('cabin crew:', all_cabincrew)
        print('pilots: ', all_pilots)
        return all_emps

# class EmployeeFilter():
#     def __init__(self, all_emps):
#         self.all_emps = all_emps

#     def list_role(self):
#         all_pilots = []
#         all_cabincrew = []
#         for line in all_emps:
#             print(line)
#             if line[2] == 'Pilot':
#                 all_pilots.append(line[1])
#             else:
#                 all_cabincrew.append(line[1])
#         print(all_cabincrew)
#         print(all_pilots)



if __name__ == "__main__":
    emps = EmployeeIO.get_emp_from_file()
    # roles = EmployeeFilter.list_role(emps)
    # for employee in emps:
        # print(employee.ssn)
