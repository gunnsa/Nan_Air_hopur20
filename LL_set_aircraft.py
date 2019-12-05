from IO_init_AircraftType import AircraftType

class SetAircraft:
    WELCOME = "WELCOME TO NaN AIR"
    MAINMENU = 'MAIN MENU'
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def display_main_menu():
        aircraft_list = []
        print('\n{}\n{:^44}\n{}\n'.format((SetAircraft.INFO*SetAircraft.MAX), 'Please enter information below', (SetAircraft.INFO*SetAircraft.MAX)))
        
        planeTypeId = input('ID: ')
        aircraft_list.append(planeTypeId)

        manufacturer = input('Manufacturer: ')
        aircraft_list.append(manufacturer)

        model = input('Model: ')
        aircraft_list.append(model)

        capacity = input('Capacity: ')
        aircraft_list.append(capacity)

        emptyWeight = input('Empty weight: ')
        aircraft_list.append(emptyWeight)

        maxTakeoffWeight = input('Max takeoff weight: ')
        aircraft_list.append(maxTakeoffWeight)

        unitThrust = input('Unit thrust: ')
        aircraft_list.append(unitThrust)

        serviceCeiling = input('Service ceiling: ')
        aircraft_list.append(serviceCeiling)

        length = input('Length: ')
        aircraft_list.append(length)

        height = input('Height: ')
        aircraft_list.append(height)

        wingspan = input('Wingspan: ')
        aircraft_list.append(wingspan)

        print('\n:: {} has been added as a new Aircraft ::'.format(planeTypeId))
        return aircraft_list

    def display_command():
        print('\n{:<15}{:^14}{:>15}'.format(SetAircraft.Q, SetAircraft.M, SetAircraft.B))
        print(SetAircraft.CHOOSE*SetAircraft.MAX)
        command = input('Please enter command: ').upper()
        print() 
        return command


    def set_voyage(self):
        import csv
        with open('AircraftType.csv', 'a', newline='') as aircraft_file:
            wr = csv.writer(aircraft_file, dialect='excel')
            wr.writerow(self) 

if __name__ == "__main__":
    new_aircraft = SetAircraft.display_main_menu()
    SetAircraft.set_voyage(new_aircraft)
    SetAircraft.display_command()
