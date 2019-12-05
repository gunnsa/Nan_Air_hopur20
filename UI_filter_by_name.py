from IO_AllEmployeesFromFile import EmployeeIO

class FilterByName:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def specific_name():
        print('\n{}\n{:^44}\n{}\n'.format((FilterByName.INFO*FilterByName.MAX), 'Please enter information below', (FilterByName.INFO*FilterByName.MAX)))
        emp_name = input('Name: ')

        return emp_name

    def find_employee(self, other):
        for employees in self:
            if employees.name == other:
                print('\n\tSocial security no: {}'
                '\n\tFull name: {}'
                '\n\tRole: {}'
                '\n\tRank: {}'
                '\n\tLicence: {}'
                '\n\tAddress: {}'
                '\n\tPhonenumber: {}'
                '\n\tEmail address: {}'
                .format(employees.ssn, employees.name, employees.role, employees.rank, employees.licens, employees.address, employees.phonenumber, employees.email))
                         
if __name__ == "__main__":
    emp_name = FilterByName.specific_name()
    FilterByName.find_employee(EmployeeIO.get_emp_from_file(), emp_name)