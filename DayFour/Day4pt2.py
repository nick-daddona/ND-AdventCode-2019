passCount = 0
for num in range(256310, 732736):
    attempt = [int(i) for i in list(str(num))]

    if attempt == sorted(attempt):
        if len(attempt) > len(set(attempt)):
            correct = False
            for x in set(attempt):
                y = attempt.count(x)
                if y == 2:
                    correct = True
                    break
            if correct:
                passCount += 1


print(passCount)
