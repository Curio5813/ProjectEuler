from time import time
from operator import mul
from functools import reduce

start = time()


def primeFactorsNumbers():
    """
    This function return a lis of prime factors numbers.
    :return:
    """
    ld, lnum = [], []
    for i in range(2, 135_000):
        n, a, lp = 2, 1, []
        while i != 1:
            while i % n == 0:
                i /= n
                a *= n
                if i % n != 0:
                    lp.append(a)
            n += 1
            a = 1
        if len(lp) == 4:
            lnum.append(lp)
    return lnum


def interger4Sequence(lnum):
    """
    This function return a sequence of 4 interger.
    :param lnum:
    :return:
    """
    ldnum = []
    for i in range(0, len(lnum)):
        cont = 0
        if i >= len(lnum) - 3:
            break
        if reduce(mul, lnum[i + 1]) - reduce(mul, lnum[i]) == 1:
            cont += 1
        if reduce(mul, lnum[i + 2]) - reduce(mul, lnum[i + 1]) == 1:
            cont += 1
        if reduce(mul, lnum[i + 3]) - reduce(mul, lnum[i + 2]) == 1:
            cont += 1
        if cont == 3:
            ldnum.append(lnum[i])
            ldnum.append(lnum[i + 1])
            ldnum.append(lnum[i + 2])
            ldnum.append(lnum[i + 3])
    return ldnum

def first4ConsecutivePrimeFactors(ldnum):
    """
    Distinct primes factors

    The first two consecutive numbers to have two distinct
    prime factors are:

                14 = 2 × 7
                15 = 3 × 5

    The first three consecutive numbers to have three distinct
    prime factors are:

            644 = 2² × 7 × 23
            645 = 3 × 5 × 43
            646 = 2 × 17 × 19.

    This function return the first four consecutive integers to have four distinct
    prime factors each. What is the first of these numbers?
    :param ldnum:
    :return:
    """
    for i in range(0, len(ldnum), 4):
        cont = 0
        for k in range(0, len(ldnum[i])):
            if ldnum[i][k] not in ldnum[i + 1]:
                cont += 1
            if ldnum[i][k] not in ldnum[i + 2]:
                cont += 1
            if ldnum[i][k] not in ldnum[i + 3]:
                cont += 1
            if ldnum[i + 1][k] not in ldnum[i + 2]:
                cont += 1
            if ldnum[i + 1][k] not in ldnum[i + 3]:
                cont += 1
            if ldnum[i + 2][k] not in ldnum[i + 3]:
                cont += 1
            if cont == 6:
                return print(reduce(mul, ldnum[i]))


first4ConsecutivePrimeFactors(interger4Sequence(primeFactorsNumbers()))
end = time()
print(f'{(end - start):.2f}')
