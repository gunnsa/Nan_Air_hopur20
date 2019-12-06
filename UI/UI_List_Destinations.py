from LL.LL_List_Destinations import LL_List_Destinations

class UI_List_Destinations:

    def __init__(self):
        pass

    def listDestinations(self):
        ''' PRENTAR ALLA ÁFANGASTAÐI '''
        result = LL_List_Destinations().get_dest_list()
        for dest in result:
            print(dest)