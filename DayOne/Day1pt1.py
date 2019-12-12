def find_fuel(mass):
    return int(mass)//3 - 2


f = open('puzzleinput.txt', 'r')
total = 0

for m in f:
    total += find_fuel(m)

print(total)
f.close()
