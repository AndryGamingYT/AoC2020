num = open('input.txt').readlines()

for i, n in enumerate(num):
    num[i] = int(n)

for x in num:
    for y in num:
        for z in num:
            sum = x + y + z
            if sum == 2020:
                p = x * y * z
                print(x, y, z, p)
                break
