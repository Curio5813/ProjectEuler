from math import sqrt


def cardanoTriplets():
    """
    This function return a cardano triple equal or less than
    a + b + c <= 110_000_000 that satisfies the condition below:

    (a + b * (c) ** (1/2)) ** (1/3) + (a - b * (c) ** (1/2)) ** (1/3) = 1

    :return:
    """
    l1, l2 = [], []
    for a in range(0, 100 + 1):
        for b in range(0, 100 + 1):
            for c in range(0, 100 + 1):
                if a + b + c >= 1_000:
                    break
                elif (a + b * c ** (1/2)) ** (1/3) + (a - b * c ** (1/2)) ** (1/3) == 1:
                    print(f"{a} {b} {c}")
                    l1.append(a)
                    l1.append(b)
                    l1.append(c)
            l2.append(l1)


cardanoTriplets()
