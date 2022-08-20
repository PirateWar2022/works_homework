n = [1, 4, 6, 4, 2]

count = 1

for i in range(len(n)):
    if i % 2 != 0:
        multiply = n[i] * n[count]
        count = i

# print(multiply)


n_1 = [1, 5, 8, 9, 2]
answers = []

lenght_of_list = len(n_1) - len(n_1)//2
lenght = 0

for i in range(lenght_of_list):
    i += 1
    i = -i
    multply_1 = n_1[lenght] + n_1[i]
    lenght += 1
    i += -1

    # print(i)
    # print(lenght)

    answers.append(multply_1)

# print(answers)


