l = [1]
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
x = 0

while True:
    x +=1

    # base ver
    l[0] = x
    for y in str(l[0]):
        l1.append(int(y))

    # *2 ver
    l[0] = x * 2
    for y in str(l[0]):
        l2.append(int(y))

    # *3 ver
    l[0] = x * 3
    for y in str(l[0]):
        l3.append(int(y))

    # *4 ver
    l[0] = x * 4
    for y in str(l[0]):
        l4.append(int(y))

    # *5 ver
    l[0] = x * 5
    for y in str(l[0]):
        l5.append(int(y))

    # *6 ver
    l[0] = x * 6
    for y in str(l[0]):
        l6.append(int(y))

    # sort all lists to compare apples to apples
    if (sorted(l1, key=int) == sorted(l2, key=int) and sorted(l2, key=int) == 
        sorted(l3, key=int) and sorted(l3, key=int) == sorted(l4, key=int) and 
        sorted(l4, key=int) == sorted(l5, key=int) and sorted(l5, key=int) == sorted(l6, key=int)):
        print("\nAnswer: {}".format(x))
        break
    else:
        # if not answer, start over
        l1.clear()
        l2.clear()
        l3.clear()
        l4.clear()
        l5.clear()
        l6.clear()
        continue
