l = []
l2 = []
add = 0
answer = []

'''
We know the range to go up to 413343 as...
1×9^5=59049
2×9^5=118098
3×9^5=177147
4×9^5=236196
5×9^5=295245
6×9^5=354294
7×9^5=413343

And we know that if we were to have seven digits, we would get back a 6 digit number, which doesn't work in the problem.
'''

for x in range(1,413343):

    for letter in str(x):
     l.append(int(letter))

    for num in l:
        l2.append(num**5)
        add += num**5

    if x == add:
        answer.append(x)

    add = 0
    l.clear()
    l2.clear()

print("Sum: {}".format(sum(answer)))
