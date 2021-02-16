l1 = []
l2 = []

for x in range(1,101):
    l1.append(x**2)
    l2.append(x)
    
print((sum(l2) ** 2) - sum(l1))
