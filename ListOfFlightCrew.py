


    
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