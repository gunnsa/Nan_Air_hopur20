from MainMenu import MainMenu
from CabinOffice import CabinOffice
from Rostering import Rostering
from List_of_employees import List_of_employees
from Employee_information import Employee_information
from All_emloyees import All_emloyees
from Employee import Employee
from ListaAllaStarfsmenn import EmployeeIO


# setja def inn í allar -- 

game_on = True
if __name__ == "__main__":
    menu_command = MainMenu.Menu()
    if menu_command == 'C':
        cabin_command = CabinOffice.Cabin_office()


        if cabin_command == 'A':
            Add_new_employee  = 0


        elif cabin_command == 'C':
            Change_employee_information = 0


        elif cabin_command == 'L':
            emp_list = List_of_employees.list_employees()


            if emp_list == 'I':
                emp_info_command = Employee_information.employee_info() 


                if emp_info_command == 'C':
                    Cabin_crew = 0
                

                elif emp_info_command == 'F':
                    Flight_crew = 0
                

                elif emp_info_command == 'A':
                    all_emp_command = All_emloyees.all_emp() 


                    if all_emp_command == 'P':
                        all_employees = EmployeeIO.get_emp_from_file()
                        
                        for employees in all_employees:
                            all_employees = EmployeeIO.get_emp_from_file()
                            print('{}\n{:^44}\n{}'.format((EmployeeIO.INFO*EmployeeIO.MAX), 'List of all employees', (EmployeeIO.INFO*EmployeeIO.MAX)))
                            
                            for employees in all_employees:
                                print('\t{} - {}'.format(employees.name, employees.rank, end= ''))

                            print('\n{:<15}{:^14}{:>15}'.format(EmployeeIO.Q, EmployeeIO.M, EmployeeIO.B))
                            print(EmployeeIO.CHOOSE*EmployeeIO.MAX)
                            command = input('Please enter command: ').upper()
                            print() 


                            if command == 'Q':
                                game_on = False


                    elif all_emp_command == 'F':
                        Find_by_specific_condition = 0


            elif emp_list == 'D':
                Destinations = 0


        elif cabin_command == 'V':
            voyage = 0


    elif menu_command == 'R':
        rostering_command = Rostering.Rostering_office()


        if rostering_command == 'V':
            Add_new_voyage = 0


        elif rostering_command == 'A':
            Add_new_destination = 0


        elif rostering_command == 'N':
            Add_new_aircraft = 0


        elif rostering_command == 'L':
            List_voyage = 0


        elif rostering_command == 'D':
            List_destinations = 0


        elif rostering_command == 'F':
            List_aircrafts = 0


        elif rostering_command == 'C':
            Change_information = 0


    elif menu_command == 'Q':
        game_on = False


