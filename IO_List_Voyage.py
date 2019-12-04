from IO_init_Voyage import Voyage

class VoyageIO:
    def get_voyage():
        path = "csv_Voyage.csv"
        with open(path, "r", encoding="utf-8") as voyage_file:
            all_lines = voyage_file.readlines()
            all_voyages = []
        
            for line in all_lines[2:]:
                line = line.split(',')
                voyages = Voyage(line[0], line[1], line[2], line[3], line[4], line[5])
                all_voyages.append(voyages)
        return all_voyages

if __name__ == "__main__":
    all_voyages = VoyageIO.get_voyage()
    counter = 1
    for voyage in all_voyages:
        print('Voyage number: {}'.format(counter))
        print('Destination: {}\n Airplane: {}\n Date of departure from KEF: {}\n \
Time of departure from KEF: {}\n Date of departure from destination to KEF:{}\n \
Time of departure to KEF: {}\n Distance: {}\n Emergency contact: {}\n \
Emergency phone: {}\n\
'.format(voyage.destination, voyage.airplane, voyage.date_out, voyage.flight_time_from_KEF, voyage.date_home, voyage.flight_time_to_KEF, voyage.distance, voyage.emergency_contact, voyage.emergency_phone))
        counter += 1

