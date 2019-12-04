
class CabinOffice:

    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def Cabin_office():
        
        print('{}\n{:^44}\n{}'.format((CabinOffice.HEADER*CabinOffice.MAX), 'Cabin Office', (CabinOffice.HEADER*CabinOffice.MAX)))

        print('\n\tA - Add new employee', 
        '\n\tC - Change employee information',
        '\n\tL - List of employees', 
        '\n\tV - Voyage\n')

        print('\n{:<15}{:^14}{:>15}'.format(CabinOffice.Q, CabinOffice.M, CabinOffice.B))
        print(CabinOffice.CHOOSE*CabinOffice.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command

if __name__ == "__main__":
    cabin_command = CabinOffice.Cabin_office()


