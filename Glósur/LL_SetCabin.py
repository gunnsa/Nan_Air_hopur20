from IO.IO_SetCabin import SetCabin_file

class SetCabin:

    def setcabin(self):
        cabin_list = SetCabin_info().set_Cabin()
        return cabin_list

    def yes_check(self):
        yes = SetCabin_file().set_Cabin_file(SetCabin().setcabin())
        if yes == True:
            print("YES")


if __name__ == "__main__":
    cabin_list = SetCabin().setcabin()
    SetCabin().yes_check()