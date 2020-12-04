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
    oneone = part1(data, 1, 1)
    threeone = part1(data, 3, 1)
    fiveone = part1(data, 5, 1)
    sevenone = part1(data, 7, 1)
    onetwo = part1(data, 1, 2)
    return oneone*threeone*fiveone*sevenone*onetwo

day3()