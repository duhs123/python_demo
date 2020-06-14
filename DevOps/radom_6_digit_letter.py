import random

rand = []

for x in range(6):
    y = random.randrange(0, 5)
    if y == 2 or y == 4:
        num = random.randrange(0, 9)
        rand.append(str(num))
    else:
        temp = random.randrange(65, 91)
        c = chr(temp)
        rand.append(c)
result = "".join(rand)
print result
