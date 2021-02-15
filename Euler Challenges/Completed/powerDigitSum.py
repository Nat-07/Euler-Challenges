l = []

# get individual symbols (numbers) from 2**1000
for x in str(2**1000):
    l.append(int(x))

print("Answer: {}".format(sum(l)))
