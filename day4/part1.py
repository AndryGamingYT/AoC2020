db = open('input.txt').readlines()

required_field = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

p = 0
people_data = [{}]

for line in db:
    if not line.strip():
        p += 1
        people_data.append({})
        continue

    data = people_data[p]
    for kv in line.strip().split():
        key, value = kv.split(':')
        data[key] = value
    people_data[p] = data

valid = 0

for data in people_data:
    check = [key in data.keys() for key in required_field]
    
    if False not in check:
        valid += 1

print(valid)
