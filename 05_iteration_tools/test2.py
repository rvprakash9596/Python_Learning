from itertools import count

for i in count(5, 2):
    print(i)
    if i > 10:
        break
