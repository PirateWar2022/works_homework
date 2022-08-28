# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

n = [1, 4, 6, 4, 2]

count = 1

for i in range(len(n)):
    if i % 2 != 0:
        multiply = n[i] + n[count]
        count = i

print(multiply)

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

n_1 = [2, 3, 4, 5, 6]
answers = []                                                                                      
lenght = 0

for i in range(len()len(n_1)//2):
    i += 1
    i = -i
    multply_1 = n_1[lenght] * n_1[i]
    lenght += 1
    i += -1

    print(i)
    print(lenght)

    answers.append(multply_1)

print(answers)

# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

n_2 = [1.1, 1.2, 3.1, 5, 10.01]
list_with_remainder = []

for i in n_2:
    remainder = i % 1
    
    round_up_the_remainder = round(remainder, 2)    
    list_with_remainder.append(round_up_the_remainder)

print(list_with_remainder)

action = max(list_with_remainder) - min(list_with_remainder)

print(action)


# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.

num = int(input('Enter the number: '))

b = ''

while num > 0:
    b = str(num % 2) + b
    num //= 2
    
# print(b)


#  F−n = (−1)n+1Fn.

# 5.) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:  - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

try:
    mas = []
    f0, f1 = 1, 1
    while True:
       n = int(input('Введите число N: '))
       if n > 2 and n < 20:
        break
    nn = -n
    i = 1
    f_1 = f1 - f0
    while i >= nn:
        f0, f1 = f1 - f0, f0
        mas.append(f1)
        i = i - 1
    mas.reverse()
    mas.append(1)
    f0, f1 = 1, 1
    for i in range(2, n):
         f0, f1 = f1, f0 + f1
         mas.append(f1)
    print(*mas)
except ValueError:
    print('Упс! Что-то пошло не так, попробуй ввести число!')


