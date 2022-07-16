from operator import add
from operator import mul
from functools import reduce

l = [1, 2, 3, 4, 5]
print(reduce(add, l))
print(reduce(mul, l))



