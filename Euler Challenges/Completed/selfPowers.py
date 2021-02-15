sum = 0

# for values of x in bound add x^x to sum
for x in range(1,1001):
    sum += x**x

# convert to string to use list comprehension 
answer = str(sum)
print("Answer: {}".format(answer[-10::]))
