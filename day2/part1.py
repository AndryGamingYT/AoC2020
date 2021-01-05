db = open('input.txt').readlines()

valid_password = 0
for line in db:
    policy, password = line.split(": ")
    min, max = policy[:-2].split("-")
    min, max = int(min), int(max)
    let = policy.split()[1]
    n = password.count(let)
    if n >= min and n <= max:
        valid_password += 1

print(valid_password)

