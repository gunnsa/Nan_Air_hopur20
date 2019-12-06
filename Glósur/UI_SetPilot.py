class SetPilot_info:
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    MAX = 44
    Q = 'Q - Quit'

    def set_Pilot(self):
        pilot_list = []
        print('\n{}\n{:^44}\n{}\n'.format((SetPilot_info.INFO*SetPilot_info.MAX), 'Please enter information below', (SetPilot_info.INFO*SetPilot_info.MAX)))
        ssn = input('Social security number: ')
        pilot_list.append(ssn)

        name = input('Full name: ')
        pilot_list.append(name)

        status = input('Role: ') 
        pilot_list.append(status)   

        status = input('Rank: ') 
        pilot_list.append(status)    

        pilot_license = input('Pilot license: ')
        pilot_list.append(pilot_license)

        address = input('Address: ')
        pilot_list.append(address)

        phone = input('Phone: ')
        pilot_list.append(phone)

        email = input('Email address: ') 
        pilot_list.append(email)

        print('\n:: {} has been added to Flight crew ::'.format(name))
        
        return pilot_list

if __name__ == "__main__":
    pilot_list = SetPilot_info().set_Pilot()
