db = open('input.txt').readlines()

valid_password = 0
for line in db:
    policy, password = line.split(": ")
    pos1, pos2 = policy[:-2].split("-")
    pos1, pos2 = int(pos1), int(pos2)
    let = policy.split()[1]
    if (password[pos1-1] == let) ^ (password[pos2-1] == let):
        valid_password += 1

print(valid_password)

