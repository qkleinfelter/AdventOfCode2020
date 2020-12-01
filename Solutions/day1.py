def day1():
    data = [int(x) for x in open(r'C:\Users\Quinn\Documents\GitHub\AdventOfCode2020\Inputs\day1.txt')]
    for x in data:
        if (2020 - x in data):
            print((2020 - x) * x) 
            
    for i in data:
        for j in data:
            for h in data:
                if (i + j + h == 2020):
                    print(i*j*h)

day1()