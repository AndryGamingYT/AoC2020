alberi = []

pendenze = [(1,1),(3,1),(5,1),(7,1),(1,2)]

with open('input.txt', 'r') as fp:
    lines = fp.readlines()

    for p in pendenze:
        x = 0
        a = 0
        for l in range(0, len(lines), p[1]):
            line = lines[l].strip()
            if line[x % len(line)] == '#':
                    a += 1
            x += p[0]
        alberi.append(a)

a = 1
for r in alberi:
    a *= r

print(a)
