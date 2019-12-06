from LL.LL_List_AllDestinations import LL_List_AllDestinations

class UI_List_Destinations:

    def __init__(self):
        pass

    def listAllDestinations(self):
        ''' PRENTAR ALLA ÁFANGASTAÐI '''
        result = LL_List_AllDestinations().get_dest_list()
        for dest in result:
            print(dest)