from random import choice, randint
from time import sleep



class sweets_game():

    def __init__(self, lot, name1, name2, sweets_on_table=2021):       
        self.sweets_on_table = sweets_on_table
        self.name1 = name1
        self.name2 = name2
        self.lot = lot

        self.who_first()

    def who_first(self):
        print(f'{self.lot} go first')
        if self.name2 == 'BOT':
            self.with_bot()

        elif self.name1 == 'BOT':
            self.with_bot()      

        else:
            self.two_players()



    def two_players(self):
    
        while self.sweets_on_table > 0:

            if self.sweets_on_table == 0:
                break

            self.num_min = int(input('Enter number, now much sweets u want to take: '))

            if self.num_min < 28:
                self.num_min = 28
            elif self.num_min <= 0:
                self.num_min = 1

            print(f'{self.lot}: {self.num_min}')
            self.sweets_on_table -= self.num_min

            if self.lot == self.name1:
                self.lot = self.name2
            elif self.lot == self.name2:
                self.lot = self.name1

            print('Left: ',self.sweets_on_table)
            print('-' * 10)
            

        self.win()

    def with_bot(self):
        
        while self.sweets_on_table > 0:
            sleep(0.20)
            if self.sweets_on_table == 0:
                break

            if self.lot == 'BOT':
                self.num_min = randint(1, 28)
            else:
                self.num_min = int(input('Enter number, now much sweets u want to take: '))

                if self.num_min > 28:
                    self.num_min = 28
                elif self.num_min <= 0:
                    self.num_min = 1

            print(f'{self.lot}: {self.num_min}')
            self.sweets_on_table -= self.num_min

            if self.lot == self.name1:
                self.lot = self.name2
            elif self.lot == self.name2:
                self.lot = self.name1

            print('Left: ',self.sweets_on_table)
            print('-' * 10)
            

    def win(self):
        
        print(f'{self.lot}: 2021\nYou winnn')
    
name1 = str(input('Name of first palyer: '))
name2  = str(input('Name of second player, if it bot write "BOT": '))

list_with_names = [name1, name2]
lot = choice(list_with_names)

run_game = sweets_game(lot, name1, name2)



