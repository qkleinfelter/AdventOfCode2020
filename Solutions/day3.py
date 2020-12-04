def day3():
    data = open(r'Inputs\day3.in').read().splitlines()
    print('Part 1 result: ' + str(part1(data, 3, 1)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data, right, down):
    x = 0
    dx = right
    dy = down
    trees = 0
    for y in range(0, len(data), dy):
        if (data[y][x] == "#"):
            trees += 1
        x = (x + dx) % len(data[0])
    return trees

def part2(data):
    slopes =[(1,1), (3,1), (5,1), (7,1), (1,2)]
    total = 1
    for slope in slopes:
        total *= part1(data, slope[0], slope[1])
    return total

day3()