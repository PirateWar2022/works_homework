<<<<<<< HEAD
import random

all_candy = 2021
first_player = 0
second_player = 0
name_first_player = 'ПЕРВЫЙ ИГРОК'
name_second_player = 'ВТОРОЙ ИГРОК'

def Assign_names(first_name, second_name):
    global name_first_player
    global name_second_player
    name_first_player = first_name
    name_second_player = second_name

def Assign_names_game_with_bot(name):
    global name_first_player
    name_first_player = name

def Who_did_win_game_with_bot(fate):
    if fate == 0:
        return name_first_player
    else:
        return 'БОТ Серофим'


def Who_did_win(fate):
    if fate == 0:
        return name_first_player
    else:
        return name_second_player

def Game():
    fate = random.randint(0, 1)
    print(f'ХОД НАЧИНАЕТ : {Who_did_win(fate)}')
    print('Правила игры: Конфеты берем от 1 до 28. Выигрывает тот, кто последний заберет конфеты из положенного диапазона')
    n_candy = 0
    global all_candy
    global first_player
    global second_player
    while all_candy > 29:
        if fate == 0:
            try:
                while True:
                    n_candy = int(input(f'{Who_did_win(fate)} сколько конфет вы возьмете: '))
                    if n_candy > 0 and n_candy < 29:
                        break
            except ValueError:
                print('Вы ввели не целое число. Попробуй еще раз!')
                n_candy = int(input(f'{Who_did_win(fate)} сколько конфет вы возьмете: '))
            first_player += n_candy
            all_candy -= n_candy
            fate = 1
            print(f'{name_first_player} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')
        else:
            try:
                while True:
                    n_candy = int(input(f'{Who_did_win(fate)} сколько конфет вы возьмете: '))
                    if n_candy > 0 and n_candy < 29:
                        break
            except ValueError:
                print('Вы ввели не целое число. Попробуй еще раз!')
                n_candy = int(input(f'{Who_did_win(fate)} сколько конфет вы возьмете: '))
            second_player += n_candy
            all_candy -= n_candy
            fate = 0
            print(f'{name_second_player} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')
    if fate == 0:
        fate = 0
        n_candy = all_candy
        first_player += n_candy
        all_candy -= n_candy
        print(f'{name_first_player} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')
    else:
        fate = 1
        n_candy = all_candy
        second_player += n_candy
        all_candy -= n_candy
        print(f'{name_second_player} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')

    print(f'Победил : {Who_did_win(fate)}\nВсего у {name_first_player} = {first_player} - конфет\nУ {name_second_player} = {second_player} - конфет')

def Game_with_bot():
    fate = random.randint(0, 1)
    print(f'ХОД НАЧИНАЕТ : {Who_did_win_game_with_bot(fate)}')
    print('Правила игры: Конфеты берем от 1 до 28. Выигрывает тот, кто последний заберет конфеты из положенного диапазона')
    n_candy = 0
    global all_candy
    global first_player
    global second_player
    while all_candy > 29:
        if fate == 0:
            try:
                while True:
                    n_candy = int(input(f'{name_first_player} сколько конфет вы возьмете: '))
                    if n_candy > 0 and n_candy < 500:
                        break
            except ValueError:
                print('Вы ввели не целое число. Попробуй еще раз!')
                n_candy = int(input(f'{name_first_player} сколько конфет вы возьмете: '))
            first_player += n_candy
            all_candy -= n_candy
            fate = 1
            print(f'{name_first_player} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')
        else:
            n_candy = random.randint(1, 28)
            second_player += n_candy
            all_candy -= n_candy
            fate = 0
            print(f'{Who_did_win_game_with_bot(1)} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')
    if fate == 0:
        fate = 0
        n_candy = all_candy
        first_player += n_candy
        all_candy -= n_candy
        print(f'{name_first_player} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')
    else:
        fate = 1
        n_candy = all_candy
        second_player += n_candy
        all_candy -= n_candy
        print(f'{Who_did_win_game_with_bot(fate)} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')

    print(f'Победил : {Who_did_win_game_with_bot(fate)}\nВсего у {name_first_player} = {first_player} - конфет\nУ {Who_did_win_game_with_bot(1)} = {second_player} - конфет')


name_second_player = input('Имя второго игрока: ')
Assign_names(name_first_player, name_second_player)
=======
import random

all_candy = 2021
first_player = 0
second_player = 0
name_first_player = 'ПЕРВЫЙ ИГРОК'
name_second_player = 'ВТОРОЙ ИГРОК'

def Assign_names(first_name, second_name):
    global name_first_player
    global name_second_player
    name_first_player = first_name
    name_second_player = second_name

def Assign_names_game_with_bot(name):
    global name_first_player
    name_first_player = name

def Who_did_win_game_with_bot(fate):
    if fate == 0:
        return name_first_player
    else:
        return 'БОТ Серофим'


def Who_did_win(fate):
    if fate == 0:
        return name_first_player
    else:
        return name_second_player

def Game():
    fate = random.randint(0, 1)
    print(f'ХОД НАЧИНАЕТ : {Who_did_win(fate)}')
    print('Правила игры: Конфеты берем от 1 до 28. Выигрывает тот, кто последний заберет конфеты из положенного диапазона')
    n_candy = 0
    global all_candy
    global first_player
    global second_player
    while all_candy > 29:
        if fate == 0:
            try:
                while True:
                    n_candy = int(input(f'{Who_did_win(fate)} сколько конфет вы возьмете: '))
                    if n_candy > 0 and n_candy < 29:
                        break
            except ValueError:
                print('Вы ввели не целое число. Попробуй еще раз!')
                n_candy = int(input(f'{Who_did_win(fate)} сколько конфет вы возьмете: '))
            first_player += n_candy
            all_candy -= n_candy
            fate = 1
            print(f'{name_first_player} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')
        else:
            try:
                while True:
                    n_candy = int(input(f'{Who_did_win(fate)} сколько конфет вы возьмете: '))
                    if n_candy > 0 and n_candy < 29:
                        break
            except ValueError:
                print('Вы ввели не целое число. Попробуй еще раз!')
                n_candy = int(input(f'{Who_did_win(fate)} сколько конфет вы возьмете: '))
            second_player += n_candy
            all_candy -= n_candy
            fate = 0
            print(f'{name_second_player} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')
    if fate == 0:
        fate = 0
        n_candy = all_candy
        first_player += n_candy
        all_candy -= n_candy
        print(f'{name_first_player} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')
    else:
        fate = 1
        n_candy = all_candy
        second_player += n_candy
        all_candy -= n_candy
        print(f'{name_second_player} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')

    print(f'Победил : {Who_did_win(fate)}\nВсего у {name_first_player} = {first_player} - конфет\nУ {name_second_player} = {second_player} - конфет')

def Game_with_bot():
    fate = random.randint(0, 1)
    print(f'ХОД НАЧИНАЕТ : {Who_did_win_game_with_bot(fate)}')
    print('Правила игры: Конфеты берем от 1 до 28. Выигрывает тот, кто последний заберет конфеты из положенного диапазона')
    n_candy = 0
    global all_candy
    global first_player
    global second_player
    while all_candy > 29:
        if fate == 0:
            try:
                while True:
                    n_candy = int(input(f'{name_first_player} сколько конфет вы возьмете: '))
                    if n_candy > 0 and n_candy < 500:
                        break
            except ValueError:
                print('Вы ввели не целое число. Попробуй еще раз!')
                n_candy = int(input(f'{name_first_player} сколько конфет вы возьмете: '))
            first_player += n_candy
            all_candy -= n_candy
            fate = 1
            print(f'{name_first_player} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')
        else:
            n_candy = random.randint(1, 28)
            second_player += n_candy
            all_candy -= n_candy
            fate = 0
            print(f'{Who_did_win_game_with_bot(1)} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')
    if fate == 0:
        fate = 0
        n_candy = all_candy
        first_player += n_candy
        all_candy -= n_candy
        print(f'{name_first_player} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')
    else:
        fate = 1
        n_candy = all_candy
        second_player += n_candy
        all_candy -= n_candy
        print(f'{Who_did_win_game_with_bot(fate)} взял: {n_candy} - конфет и осталось в куче: {all_candy} - конфет\n')

    print(f'Победил : {Who_did_win_game_with_bot(fate)}\nВсего у {name_first_player} = {first_player} - конфет\nУ {Who_did_win_game_with_bot(1)} = {second_player} - конфет')


name_second_player = input('Имя второго игрока: ')
Assign_names(name_first_player, name_second_player)
>>>>>>> main
Game()