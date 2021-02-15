from math import *

# simple 3 nested for loops looking in ranges
for num1 in range(150,500):
    for num2 in range(150,500):
        for num3 in range(150,500):
            # check if current lager than former and equal, and equal to 1000
            if num1 < num2 < num3 and sqrt(num1**2 + num2**2) == sqrt(num3**2) and num1 + num2 + num3 == 1000:
                print("Answer: {}".format(num1 * num2 * num3))
                exit()
            else:
                continue








