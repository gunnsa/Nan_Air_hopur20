from UI.UI_SetPilot import SetPilot_info

class SetPilot:

    def setpilot(self):
        pilot_list = SetPilot_info().set_Pilot()
        return pilot_list

if __name__ == "__main__":
    pilot_list = SetPilot().setpilot()