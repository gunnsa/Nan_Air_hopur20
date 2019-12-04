# Lista áfangastaði - Notkunartilvik nr 10

#class Destinations:
#    def __init__(self, id, destination):
#        self.id = id
#        self.destination = destination

from Destinations import Destinations

class DestinationIO:
    def get_dest_from_file():
        with open('Destinations.csv', 'r', encoding= 'utf-8') as file_object:
            all_lines = file_object.readlines()
            all_dest = []
            
            for line in all_lines[1:]:
                line = line.split(',')
                dest = Destinations(line[0], line[1]) # 0 = id, 1 = destination
                all_dest.append(dest)

        return all_dest


if __name__ == "__main__":
    all_destinations = DestinationIO.get_dest_from_file()
    for dest in all_destinations:
        print('\n{} - {}'.format(dest.id, dest.destination), end= '')