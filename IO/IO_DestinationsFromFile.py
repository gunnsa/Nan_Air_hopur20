from MODEL.Model_Destinations import Model_Destinations

class IO_DestinationsFromFile:

    def get_dest_from_file(self):
        ''' Returns All Destinations from file '''

        with open("Destinations.csv", "r", encoding="utf-8") as dest_file:
            all_lines = dest_file.readlines()
            all_dest = []
            
            for line in all_lines[1:]:
                line = line.split(',')
                dest = Model_Destinations(line[0], line[1], line[2], line[3], line[4], line[5])
                all_dest.append(dest)

        return all_dest