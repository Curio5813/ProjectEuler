from statistics import median, mode


def test():
    l = [8, 5, 9, 3, 3]
    l2 = l.copy()
    l2.sort()
    print(l)
    print(l2)
    print(median(l))
    print(median(l2))


test()