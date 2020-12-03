def day3():
    data = open(r'Inputs\day3.in').readlines()
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    x = 0
    trees = 0
    for y in range(0, len(data), 1):
        print(data[y][x])
        if (data[y][x] == "#"):
            trees += 1
        x = (x + 3) % len(data[0])
    return trees

def part2(data):
    return 0

day3()