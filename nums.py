num = [1, 2, 3, 3, 5, 3, 6, 10, 6]
res = []
for i in num:
    if num.count(i) == 1:
        res.append(i)


print(res)