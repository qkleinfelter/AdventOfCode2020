def day2():
    data = open(r'Inputs\day2.in').readlines()
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    valid = 0
    for x in data:
        numbers, char, password = x.split()
        low, hi = map(int, numbers.split('-'))
        char = char[0]
        charct = 0
        for y in password:
            if y == char:
                charct += 1
        if (low <= charct) and (hi >= charct):
            valid += 1

    return valid

def part2(data):
    for x in data:
        print(x)
        numbers, char, password = x.split()
        pos1, pos2 = map(int, numbers.split('-'))
        char = char[0]
        valid = 0
        print(char)
        print(password[pos1-1])
        print(password[pos2-1])
        if ((password[pos1-1] == char) ^ (password[pos2-1] == char)):
            valid += 1
    return valid
day2()