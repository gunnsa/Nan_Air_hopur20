from IO.IO_AllEmployeesFromFile import EmployeeIO

class AllCabin:

    def get_cabin_list(self):
        crew_list = EmployeeIO().get_emp_from_file()

        cabin_dict = {}

        for employee in crew_list:
            if employee.role == 'Cabincrew':
                cabin_dict[employee.name] = employee.rank

        return cabin_dict

if __name__ == "__main__":
    cabin_dict = AllCabin().get_cabin_list()
