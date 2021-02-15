l1 = []
l2 = []
lFinal = []

for num1 in range(100,1000):
    l1.append(num1)

for num2 in range(100,1000):
    l2.append(num2)

for x in l1:
    for y in l2:
        prod = x * y
        if str(prod)[::-1] == str(prod):
            lFinal.append(prod)

print("Answer: {}".format(max(lFinal)))
