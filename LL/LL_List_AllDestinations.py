from IO.IO_AllDestinationsFromFile import IO_AllDestinationsFromFile

class LL_List_AllDestinations:

    def get_dest_list(self):
        dest_list = IO_AllDestinationsFromFile().get_dest_from_file()
        return dest_list