l = []

for num in range(1,1001):
    if num % 3 == 0 or num % 5 == 0:
        l.append(num)

print("Answer: {}".format( sum(l) - 1000))
