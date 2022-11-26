from time import time


def triPentaHexaNumbers():
    """
    This function return a list of numbers who are, at the same time,
    a triangle numbers, a pentagonal numbers and hexagonal numbers
    until the first 1 million integer.
    :return:
    """
    l1, l2, l3, l4 = [], [], [], []
    for i in range(2, 100_000 + 1):
        # Formula to find triangle numbers.
        t = (i * (i + 1)) / 2
        # Formula to find pentagonal numbers.
        p = (i * (3 * i - 1)) / 2
        # Formula to find hexagonal numbers.
        h = i * (2 * i - 1)
        l1.append(int(t))
        l2.append(int(p))
        l3.append(h)
    for i in l1:
        if i in l2 and i in l3:
            l4.append(i)
    return print(*l4)


triPentaHexaNumbers()

