


from random import *
import time as t

sweets_on_table = 2021

name1 = str(input('Name of first palyer: '))
name2 = str(input('Name of second player: '))
name_list = [name1, name2]

lot = choice(name_list)
while sweets_on_table > 0:
    if sweets_on_table == 0:
        break
    random_num = randint(0, 28)
    print(f'{lot}: {random_num}')
    sweets_on_table -= random_num
    if lot == name1:
        lot = name2
    elif lot == name2:
        lot = name1
    print(sweets_on_table)
    print('-' * 10)
    t.sleep(0.10)


if lot == name1:
    print(f'{name1}: 2021\nYou winnn')
    
elif lot == name2:
    print(f'{name2}: 2021\nYou winnn')