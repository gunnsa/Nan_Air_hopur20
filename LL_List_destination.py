# Lista áfangastaði - Notkunartilvik nr 10

#class Destinations:
#    def __init__(self, id, destination):
#        self.id = id
#        self.destination = destination

from Destinations import Destinations

class DestinationIO:
    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def get_dest_from_file():
        with open('Destinations.csv', 'r', encoding= 'utf-8') as file_object:
            all_lines = file_object.readlines()
            all_dest = []
            
            for line in all_lines[1:]:
                line = line.split(',')
                dest = Destinations(line[0], line[1]) # 0 = id, 1 = destination
                all_dest.append(dest)

        return all_dest


    def display(self):
        print('{}\n{:^44}\n{}'.format((DestinationIO.INFO*DestinationIO.MAX), 'List of all destinations', (DestinationIO.INFO*DestinationIO.MAX)))

        for dest in self:
            print('\n\t{} - {}'.format(dest.id, dest.destination), end= '')

        print('\n{:<15}{:^14}{:>15}'.format(DestinationIO.Q, DestinationIO.M, DestinationIO.B))
        print(DestinationIO.CHOOSE*DestinationIO.MAX)
        command = input('Please enter command: ').upper()
        print() 
        return command

if __name__ == "__main__":
    all_destinations = DestinationIO.get_dest_from_file()
    DestinationIO.display(all_destinations)





