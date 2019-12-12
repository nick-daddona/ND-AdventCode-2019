f = open('inputfile', 'r')

intcodes = f.read().split(',')
intcodes = [int(i) for i in intcodes]
intcodes[1] = 12
intcodes[2] = 2
index = 0

while intcodes[index] != 99:
    if intcodes[index] == 1:
        intcodes[intcodes[index+3]] = intcodes[intcodes[index+1]] + \
            intcodes[intcodes[index+2]]
    elif intcodes[index] == 2:
        intcodes[intcodes[index+3]] = intcodes[intcodes[index+1]] * \
            intcodes[intcodes[index+2]]
    else:
        print("Something is wrong")
    index += 4

print(intcodes[0])
f.close()
