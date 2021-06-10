import re

db = open('input.txt').readlines()

required_field = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

p = 0
people_data = [{}]

for line in db:
    if not line.strip():
        p += 1
        people_data.append({})
        continue

    for kv in line.strip().split():
        key, value = kv.split(':')
        people_data[p][key] = value

valid = 0

for data in people_data:
    check = []
    if 'byr' in data.keys():
        if len(data['byr']) == 4 and int(data['byr']) >= 1920 and int(data['byr']) <= 2002:
            check.append(True)
    if 'iyr' in data.keys():
        if len(data['iyr']) == 4 and int(data['iyr']) >= 2010 and int(data['iyr']) <= 2020:
            check.append(True)
    if 'eyr' in data.keys():
        if len(data['eyr']) == 4 and int(data['eyr']) >= 2020 and int(data['eyr']) <= 2030:
            check.append(True)
    if 'hgt' in data.keys():
        try:
            n = int(data['hgt'][:-2])
            u = data['hgt'][-2:]
            if (u == 'cm' and n >= 150 and n <= 193) or (u == 'in' and n >= 59 and n <= 76):
                check.append(True)
        except Exception:
            pass
    if 'hcl' in data.keys():
        try:
            if data['hcl'][0] == '#' and int(data['hcl'][1:], 16):
               check.append(True)
        except Exception:
            pass
    if 'ecl' in data.keys():
        if data['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
            check.append(True)
    if 'pid' in data.keys():
        try:
            if len(data['pid']) == 9 and int(data['pid']):
                check.append(True)
        except Exception:
            pass

    if len(check) >= len(required_field):
        valid += 1

print(valid)
