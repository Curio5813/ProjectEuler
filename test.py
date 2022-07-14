from statistics import median, mode


def test():
    l = [8, 5, 9, 3, 3]
    l.sort()
    print(l)
    for i in range(0, len(l)):
        print(mode(l))
        break


test()

moda = mode([1, 1, 1, 3, 3, 2])
print(moda)