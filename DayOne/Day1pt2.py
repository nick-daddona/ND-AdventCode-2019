def find_fuel(mass):
    return int(mass)//3 - 2


f = open('inputfile', 'r')
fuel = 0
total = 0

for m in f:
    fuel = find_fuel(m)
    while fuel > 0:
        total += fuel
        fuel = find_fuel(fuel)

print(total)
f.close()
