passCount = 0
for num in range(256310, 732736):
    attempt = [int(i) for i in list(str(num))]

    if attempt == sorted(attempt):
        if len(attempt) > len(set(attempt)):
            passCount += 1

print(passCount)
