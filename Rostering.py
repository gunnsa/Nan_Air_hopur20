
class Rostering:

    HEADER = '#'    # 44
    INFO = '*'      # 44
    CHOOSE = '_'    # 44
    COMMENT = ':'   # 2
    MAX = 44
    B = 'B - Go back'
    M = 'M - Main menu'
    Q = 'Q - Quit'

    def Rostering_office():
        
        print('{}\n{:^44}\n{}'.format((Rostering.HEADER*Rostering.MAX), 'Rostering', (Rostering.HEADER*Rostering.MAX)))

        print('\n\tV - Add new voyage', 
        '\n\tA - Add new destination',
        '\n\tN - Add new aircraft', 
        '\n\tL - List voyage', 
        '\n\tD - List destinations', 
        '\n\tF - List aircrafts',
        '\n\tC - Change information\n')

        print('\n{:<15}{:^14}{:>15}'.format(Rostering.Q, Rostering.M, Rostering.B))
        print(Rostering.CHOOSE*Rostering.MAX)
        command = input('Please enter command: ').upper()
        print()
        return command

if __name__ == "__main__":
    rostering_command = Rostering.Rostering_office()


