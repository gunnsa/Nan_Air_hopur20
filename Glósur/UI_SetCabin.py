from LL.LL_SetCabin import SetCabin 

class SetCabin_info:
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    MAX = 44
    Q = 'Q - Quit'

    def set_Cabin(self):
        cabin_list = []
        print('\n{}\n{:^44}\n{}\n'.format((SetCabin_info.INFO*SetCabin_info.MAX), 'Please enter information below', (SetCabin_info.INFO*SetCabin_info.MAX)))
        ssn = input('Social security number: ')
        cabin_list.append(ssn)

        name = input('Full name: ')
        cabin_list.append(name)

        status = input('Role: ') 
        cabin_list.append(status)   

        status = input('Rank: ') 
        cabin_list.append(status)    

        pilot_license = 'N/A'
        cabin_list.append(pilot_license)

        address = input('Address: ')
        cabin_list.append(address)

        phone = input('Phone: ')
        cabin_list.append(phone)

        email = input('Email address: ') 
        cabin_list.append(email)

        print('\n:: {} has been added to Cabin crew ::'.format(name))
        return cabin_list

    def return_to_LL(self, other):
        SetCabin().setcabin()

if __name__ == "__main__":
    cabin_list = SetCabin_info().set_Cabin()
    SetCabin_info().return_to_LL(cabin_list)
