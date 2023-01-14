from time import time

start = time()


def generatePrimes():
    """
    This function return a list of prime numbers until a limit given.
    :return:
    """
    lim = 800_000 + 1
    p, n_p = [], set()
    for i in range(2, lim):
        if i in n_p:
            continue
        for k in range(i * 2, lim, i):
            n_p.add(k)
        p.append(i)
    return p


def truncatablePrimes(p):
    """
    Truncatable primes

    The number 3797 has an interesting property. Being prime itself,
    it is possible to continuously remove digits from left to right,
    and remain prime at each stage: 3797, 797, 97, and 7. Similarly
    we can work from right to left: 3797, 379, 37, and 3.

    This function return the sum of the only eleven primes that are both
    truncatable from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    :param p:
    :return:
    """
    t = []
    for i in range(0, len(p)):
        x = len(str(p[i]))
        y = 10 ** (x - 1)
        a = p[i]
        b = p[i]
        while a in p and b in p:
            a %= y
            b //= 10
            y //= 10
            if y == 0 and a == 0 and b == 0 and p[i] > 7:
                t.append(p[i])
                break
    print(t)
    print(sum(t))


truncatablePrimes(generatePrimes())

end = time()
print(f'{(end - start):.2f}')
