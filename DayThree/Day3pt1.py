
f = open('puzzleinput.txt', 'r')

wireOne = f.readline().strip().split(',')
wireTwo = f.readline().split(',')

f.close()

currentPosition = [0, 0]
previousPosition = []
oneLines = []
twoLines = []

for m in range(len(wireOne)):
    direction = wireOne[m][0]
    distance = int(wireOne[m][1:])
    previousPosition = list(currentPosition)
    if direction == 'U':
        currentPosition[0] += distance
        for p in range(previousPosition[0]+1, currentPosition[0]+1):
            oneLines.append("{},{}".format(p, currentPosition[1]))
    elif direction == 'D':
        currentPosition[0] -= distance
        for p in range(currentPosition[0], previousPosition[0]-1):
            oneLines.append("{},{}".format(p, currentPosition[1]))
    elif direction == 'R':
        currentPosition[1] += distance
        for p in range(previousPosition[1]+1, currentPosition[1]+1):
            oneLines.append("{},{}".format(currentPosition[0], p))
    elif direction == 'L':
        currentPosition[1] -= distance
        for p in range(currentPosition[1], previousPosition[1]-1):
            oneLines.append("{},{}".format(currentPosition[0], p))

currentPosition = [0, 0]

for m in range(len(wireTwo)):
    direction = wireTwo[m][0]
    distance = int(wireTwo[m][1:])
    previousPosition = list(currentPosition)
    if direction == 'U':
        currentPosition[0] += distance
        for p in range(previousPosition[0]+1, currentPosition[0]+1):
            twoLines.append("{},{}".format(p, currentPosition[1]))
    elif direction == 'D':
        currentPosition[0] -= distance
        for p in range(currentPosition[0], previousPosition[0]-1):
            twoLines.append("{},{}".format(p, currentPosition[1]))
    elif direction == 'R':
        currentPosition[1] += distance
        for p in range(previousPosition[1]+1, currentPosition[1]+1):
            twoLines.append("{},{}".format(currentPosition[0], p))
    elif direction == 'L':
        currentPosition[1] -= distance
        for p in range(currentPosition[1], previousPosition[1]-1):
            twoLines.append("{},{}".format(currentPosition[0], p))


iPoints = set(oneLines).intersection(set(twoLines))
manDist = []
for p in iPoints:
    p1, p2 = p.split(',')
    x = int(p1)
    y = int(p2)

    manDist.append(abs(x) + abs(y))

print(min(manDist))
