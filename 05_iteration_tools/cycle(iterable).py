from itertools import cycle

count = 0
for i in cycle (['A', 'B', 'C']):
    print(i)
    count += 1
    if count > 5:
        break
