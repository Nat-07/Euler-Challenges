l = []
for num in range(2,101):
    for x in range(2,101):
        if num ** x in l:
            continue
        else:
            l.append(num ** x)

print("\nAnswer: {}".format((len(l))))
