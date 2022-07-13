from math import factorial
from time import time

start = time()
def latticePaths():
    """
    Lattice paths

    Starting in the top left corner of a 2×2 grid, and only being
    able to move to the right and down, there are exactly 6 routes
    to the bottom right corner.

    This function return how many routes are there through a 20×20
    grid, that goes from the top left to the top down rigth.
    :return:
    """
    d = 20
    a = 1_000_000_000
    b = 1_000_000_000_000
    comb = factorial(d + d) / (factorial(d) * factorial(d))
    if a <= comb < b:
        return print(f'{(int(comb)/a):.2f} bilhões de rooutas')


latticePaths()

end = time()
print(f'{(end - start):.2f}')
