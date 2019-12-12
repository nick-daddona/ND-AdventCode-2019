f = open('inputfile', 'r')

searching = True
noun = 0
verb = -1

while searching:

    intcodes = f.read().split(',')
    f.seek(0)
    intcodes = [int(i) for i in intcodes]
    index = 0

    if verb == 99:
        noun += 1
        verb = 0
    else:
        verb += 1
    intcodes[1] = noun
    intcodes[2] = verb

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

    if intcodes[0] == 19690720:
        print("19690720 found")
        print(100*noun+verb)
        searching = False
    else:
        print("Noun and Verb do not result in 19690720")

f.close()
