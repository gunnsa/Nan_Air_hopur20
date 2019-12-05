from IO_init_Voyage import Voyage

class VoyageIO:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def get_voyage():
        path = "csv_Voyage.csv"
        with open(path, "r", encoding="utf-8") as voyage_file:
            all_lines = voyage_file.readlines()
            all_voyages = []
        
            for line in all_lines[1:]:
                line = line.split(',')
                voyages = Voyage(line[0], line[1], line[2], line[3], line[4], line[5])
                all_voyages.append(voyages)

        return all_voyages

    
    def display(self):
        print('{}\n{:^44}\n{}'.format((VoyageIO.INFO*VoyageIO.MAX), 'List of all Voyages', (VoyageIO.INFO*VoyageIO.MAX)))
        print()

        counter = 1
        for voyage in self:
            print('VOYAGE NUMBER {}:'.format(counter))     
            print("_________________")       
            print('\nDestination: {}\nAirport: {}\nDate of departure from KEF: {}\nTime of departure from KEF: {}\nDate of departure from destination to KEF: {}\nTime of departure to KEF: {}\n'.format(voyage.destination, voyage.airport, voyage.date_out, voyage.flight_time_from_KEF, voyage.date_home, voyage.flight_time_to_KEF))
            counter += 1

        print('\n{:<15}{:^14}{:>15}'.format(VoyageIO.Q, VoyageIO.M, VoyageIO.B))
        print(VoyageIO.CHOOSE*VoyageIO.MAX)
        command = input('Please enter command: ').upper()
        print() 
        return command

if __name__ == "__main__":
    all_voyages = VoyageIO.get_voyage()
    VoyageIO.display(all_voyages)


