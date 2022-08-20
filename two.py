# n = int(input())
# i = 1
# count = 0
# num_list = []
# while count < n:
#     num_list.append(str(i))
#     # print(i, end=',')
#     i *= -3
#     count = count + 1
# print(','.join(num_list))
#

first: str = input()
second: str = input()
count = 0

while first in second:
    tmp = second.find(first)
    count += 1
    if second == first:
        break
    second = second[tmp + len(first):]

print(count)