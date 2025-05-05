# islice(): Slices an iterator like a list.

from itertools import islice
for i in islice(range(10), 2, 7, 2):
    print(i)
