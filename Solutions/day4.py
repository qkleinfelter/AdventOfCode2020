def day4():
    data = open(r'Inputs\day4.in').read().split('\n\n')
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    valid = 0
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for x in data:
        x = x.split()
        passport = [y.split(':')[0] for y in x]
        print(passport)
        invalid = False
        for field in required:
            if (not(field in passport)):
                invalid = True
        if not invalid:
            valid += 1
    return valid

def part2(data):
    return 0

day4()