from time import time

start = time()


def strNumbers():
    """
    This function return a list of string numbers until one million
    :return:
    """
    l, l1, cont = [], [], 0
    for i in range(2, 1_000_000):
        str_l1 = str(i)
        l.append(str_l1)
    for i in range(0, len(l)):
        for k in range(0, len(l[i])):
            if l[i].count(l[i][k]) == 1:
                cont += 1
        if cont == len(l[i]):
            l1.append(l[i])
        cont = 0
    return l1


def strDouble(l1):
    """
    This function return the double of the list obtained in the
    function strNumbers.
    :param l1:
    :return:
    """
    l2 = []
    for i in range(0, len(l1)):
        str_l2 = str(int(l1[i]) * 2)
        l2.append(str_l2)
    return l2


def strTriple(l1):
    """
    This function return the triple of the list obtained in
    the function strNumbers.
    :param l1:
    :return:
    """
    l3 = []
    for i in range(0, len(l1)):
        str_l3 = str(int(l1[i]) * 3)
        l3.append(str_l3)
    return l3


def strQuadruple(l1):
    """
    This function return the quadruple of the list obtained in the
    function strNumbers.
    :param l1:
    :return:
    """
    l4 = []
    for i in range(0, len(l1)):
        str_l4 = str(int(l1[i]) * 4)
        l4.append(str_l4)
    return l4


def strQuintuple(l1):
    """
    This function return the quintuple of the list obtained in
    the function strNumbers.
    :param l1:
    :return:
    """
    l5, l5_str, cont = [], [], 0
    for i in range(0, len(l1)):
        str_l5 = str(int(l1[i]) * 5)
        l5.append(str_l5)
    return l5


def strSixtuple(l1):
    """
    This function return the sixtuple of the list obtained in the
    function strNumbers.
    :param l1:
    :return:
    """
    l6, l6_str, cont = [], [], 0
    for i in range(0, len(l1)):
        str_l6 = str(int(l1[i]) * 6)
        l6.append(str_l6)
    return l6


def permutedMultiples(l1, l2, l3, l4, l5, l6):
    """
    Permuted multiples

    It can be seen that the number, 125874, and its double, 251748,
    contain exactly the same digits, but in a different order.

    This function return the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
    and 6x, contain the same digits.
    :param l1:
    :param l2:
    :param l3:
    :param l4:
    :param l5:
    :param l6:
    :return:
    """
    p, cont = [], 0
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            if l1[i][k] in l2[i] and l1[i].index(l1[i][k]) != l2[i].index(l1[i][k]):
                cont += 1
            if l1[i][k] in l3[i] and l1[i].index(l1[i][k]) != l3[i].index(l1[i][k]):
                cont += 1
            if l1[i][k] in l4[i] and l1[i].index(l1[i][k]) != l4[i].index(l1[i][k]):
                cont += 1
            if l1[i][k] in l5[i] and l1[i].index(l1[i][k]) != l5[i].index(l1[i][k]):
                cont += 1
            if l1[i][k] in l6[i] and l1[i].index(l1[i][k]) != l6[i].index(l1[i][k]):
                cont += 1
        if cont == len(l1[i]) * 5:
            p.append(int(l1[i]))
        cont = 0
    print(p[0])
    return p


permutedMultiples(strNumbers(), strDouble(strNumbers()),
                  strTriple(strNumbers()), strQuadruple(strNumbers()),
                  strQuintuple(strNumbers()), strSixtuple(strNumbers()))
end = time()
print(f'{(end - start):.2f}')
