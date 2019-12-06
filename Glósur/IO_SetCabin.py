from LL.LL_SetCabin import SetCabin

import csv

class SetCabin_file:

    def set_Cabin_file(self, other):
        with open('Crew.csv', 'a', newline='') as destination_file:
            wr = csv.writer(destination_file, dialect='excel')
            wr.writerow(other)
        return True

if __name__ == "__main__":
    yes = SetCabin_file().set_Cabin_file(SetCabin().setcabin())
