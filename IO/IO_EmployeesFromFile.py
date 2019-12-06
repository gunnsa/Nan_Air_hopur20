from MODEL.Model_Employee import Model_Employee
import csv

class IO_EmployeesFromFile:

    def get_emp_from_file(self):
        ''' Returns All Employees from file '''

        with open("Crew.csv", "r", encoding="utf-8") as crew_file:
            all_lines = crew_file.readlines()
            all_emps = []
            
            for line in all_lines[1:]:
                line = line.split(',')
                emp = Model_Employee(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
                all_emps.append(emp)

        return all_emps

    def addEmployeeToFile(self, employee):
        with open("Crew.csv", "a", encoding="utf-8") as crew_file:
            fieldnames = ["ssn","name","role","rank","license","address","phonenumber","email"]
            writer = csv.DictWriter(crew_file, fieldnames = fieldnames)
            writer.writerow({"ssn": employee.ssn, "name": employee.name, "role": employee.role, "rank": employee.rank, "license": employee.license, "address": employee.address, "phonenumber": employee.phonenumber, "email": employee.email} )