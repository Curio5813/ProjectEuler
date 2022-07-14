from statistics import mean, median_high, mode
from time import time
from csv import reader

start = time()


def maximumPathSumI():
    """
    Maximum path sum I

    By starting at the top of the triangle below and moving
    to adjacent numbers on the row below, the maximum total
    from top to bottom is 23.

                    3
                   7 4
                  2 4 6
                 8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    This function return the maximum sum by adjacent numbers
    from top to bottom of the triangle below:

                                  75
                                 95 64
                               17 47 82
                              18 35 87 10
                            20 04 82 47 65
                           19 01 23 75 03 34
                         88 02 77 73 07 63 67
                        99 65 04 28 06 16 70 92
                       41 41 26 56 83 40 80 70 33
                     41 48 72 33 47 32 37 16 94 29
                    53 71 44 65 25 43 91 52 97 51 14
                   70 11 33 28 77 73 17 78 39 68 17 57
                  91 71 52 38 17 14 91 43 58 50 27 29 48
                63 66 04 68 89 53 67 30 73 16 69 87 40 31
               04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve
    this problem by trying every route. However, Problem 67, is the
    same challenge with a triangle containing one-hundred rows; it
    cannot be solved by brute force, and requires a clever method! ;O)
    :return:
    """
    mod, l2, l3, l4, l5 = [], [], [], [], []
    arq = open('max_path_sum_01_test.csv')
    t = reader(arq, delimiter=' ')
    l1 = list(t)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = int(l1[i][k])
    tri = int((len(l1) * (len(l1) + 1) / 2))
    soma = int(tri * 3)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            med = mean(l1[i])
            mediana = median_high(l1[i])
            moda = mode(l1[i])
            num1 = l1[i][k] - med + 0.1
            num2 = l1[i][k] - mediana + 0.1
            num3 = l1[i][k] - moda
        l2.append(num1)
        l3.append(num2)
        l4.append(num3)
        idx1 = l2.index(max(l2))
        idx2 = l3.index(min(l3))
        idx3 = l4.index(min(l4))
        if idx1 >= idx2 >= idx3:
            l5.append(l1[i][idx2])
        elif idx1 <= idx2 <= idx3:
            l5.append((l1[i][idx1]))
        elif idx1 <= idx2 >= idx3:
            l5.append(l1[i][idx3])
    a = sum(l5)
    print(len(l5))
    print(l5)
    print(a)
    if a % 3 == 0 or a % 5 == 0 or a % 7 == 0:
        print(sum(l5) + soma)
    else:
        print(sum(l5))


maximumPathSumI()
end = time()
