from IO_AllEmployeesFromFile import EmployeeIO

class FilterBySSN:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def specific_ssn():
        print('\n{}\n{:^44}\n{}\n'.format((FilterBySSN.INFO*FilterBySSN.MAX), 'Please enter information below', (FilterBySSN.INFO*FilterBySSN.MAX)))
        emp_ssn = input('Social security no: ')

        return emp_ssn

    def find_employee(self, other):
        for employees in self:
            if employees.ssn == other:
                print('\n\tSocial security no: {}'
                '\n\tFull name: {}'
                '\n\tRole: {}'
                '\n\tRank: {}'
                '\n\tLicence: {}'
                '\n\tAddress: {}'
                '\n\tPhonenumber: {}'
                .format(employees.ssn, employees.name, employees.role, employees.rank, employees.licens, employees.address, employees.phonenumber))
                        


if __name__ == "__main__":
    emp_ssn = FilterBySSN.specific_ssn()
    FilterBySSN.find_employee(EmployeeIO.get_emp_from_file(), emp_ssn)