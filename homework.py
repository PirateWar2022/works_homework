import random as ran


# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23 , - 0,56 -> 11

# n = input()
#
# sum1 = 0
#
# for dig in n:
#     if dig.isdigit():
#         sum1 += int(dig)  # sum1 = sum1 + float(dig)
#
# print(sum1)




# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# n = int(input())
# count = 1
# list_mult = []
#
# for i in range(1, n+1):
#     i *= count  # i = i * count
#     list_mult.append(i)
#     count = i
#
# print(list_mult)
#
#



n = int(input('Enter the number:  '))
n_minus = -n
numbers_list = []

for i in range(n_minus, n+1):
    numbers_list.append(i)

index_list_of_numbers = len(numbers_list)-1
print(index_list_of_numbers)
count = 1
print(numbers_list)

with open(file='index.txt', mode='a') as file:
    while True:
        count += 1
        index = ran.randint(0, index_list_of_numbers)
        str(index)
        file.write(f'{index}\n')
        if count == index_list_of_numbers:
            countine


prod = 1

file_with_index = open(file='index.txt')

for i in file_with_index:
    i = int(i)
    element = numbers_list[i]
    prod *= element

print(prod)


    # print(f'{26 * "*"}\n\tSomething error!!\n{26 * "*"}')








