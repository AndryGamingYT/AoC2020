num = open('input.txt').readlines()

for i, n in enumerate(num):
    num[i] = int(n)

for x in num:
    for y in num:
        sum = x + y
        if sum == 2020:
            p = x * y
            print(x, y, p)
            break
