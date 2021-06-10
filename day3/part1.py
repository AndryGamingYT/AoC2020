alberi = 0

with open('input.txt', 'r') as fp:
    lines = fp.readlines()
    x = 0
    for line in lines:
        line = line.strip()
        if line[x % len(line)] == '#':
                alberi += 1
        x += 3

print(alberi)
