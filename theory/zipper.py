from itertools import chain


_ = int(input())
a, b = input().split(), input().split()
c = chain.from_iterable(zip(a, b))
print(" ".join(c))
