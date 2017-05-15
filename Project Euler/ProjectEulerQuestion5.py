import math

for x in range(0,100000):
    for y in range (1,20):
        if x % y == 0:
            print(x)
        else:
            x += 1
            y += 1
