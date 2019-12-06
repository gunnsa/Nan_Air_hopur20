from IO.IO_DestinationsFromFile import IO_DestinationsFromFile

class LL_List_Destinations:

    def get_dest_list(self):
        dest_list = IO_DestinationsFromFile().get_dest_from_file()
        return dest_list