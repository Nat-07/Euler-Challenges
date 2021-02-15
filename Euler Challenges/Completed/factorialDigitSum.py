l = []
l2 = []
currentVal = 1

givenBound = 100*(100-1)

for i in range(1,99):
    currentVal *= i

l.append(givenBound*currentVal)

# get individual symbols(numbers) in large number
for num in l:
    for elm in str(num):
        l2.append(int(elm))

# sum list
print("Answer {}".format(sum(l2)))
