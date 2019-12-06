from LL.LL_SetPilot import SetPilot

import csv

class SetPilot_file:

    def set_Pilot_file(self, other):
        with open('Crew.csv', 'a', newline='') as destination_file:
            wr = csv.writer(destination_file, dialect='excel')
            wr.writerow(other)

if __name__ == "__main__":
    SetPilot_file().set_Pilot_file(SetPilot().setpilot())