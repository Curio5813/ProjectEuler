from time import time

start = time()


def primosAteMil():
    """
    This functio return the numbers primes until one thousand.
    :return:
    """
    lim, primes, not_primes = 1_000, [], set()
    for i in range(2, lim + 1):
        if i in not_primes:
            continue
        for k in range(i * 2, lim + 1, i):
            not_primes.add(k)
        primes.append(i)
    return primes


def quadraticPrimes(primes):
    """
    This parameters is a list of prime numbers until one thousand
    :param primes:

    Quadratic primes

    Euler discovered the remarkable quadratic formula:

                n² + n + 41

    It turns out that the formula will produce 40 primes for
    the consecutive integer values 0 <= n <= 39. However,
    when n = 40, 40² + 40 + 41 = 40(40 + 1) + 41 is divisible
    by 41, and certainly when n = 41, 41² + 41 + 41  is clearly
    divisible by 41.

    The incredible formula n² - 79n + 1601 was discovered, which
    produces 80 primes for the consecutive values 0 <= n <= 79.
    The product of the coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

        n² + an + b, where |a| < 1000 and |b| < 1000

    where n is the modulus/absolute value of n.

    e.g. |11| = 11 and |-4| = 4

    This function return the product of the coefficients, and, for the quadratic
    expression that produces the maximum number of primes for consecutive
    values of n, starting with n = 0.
    :return:
    """
    pdl, pd, pl, pq, pdl2, pda, pdb = [], 0, [], [], [], [], []
    for a in range(1, 1_001):
        for b in range(1, 1_001):
            pd = a * b
            pda.append(a)
            pdb.append(b)
            pdl.append(pd)
            for n in range(0, 1_001):
                p = n ** 2 + n * a + b
                if p in primes:
                    pl.append(p)
                else:
                    break
        pq.append(len(pl))
        pdl2.append(pd)
        pdl = []
        pl = []
    idx = pq.index(max(pq))
    return print(f'{pdl2[idx]} {pda[idx]} {pdb[idx]}')


quadraticPrimes(primosAteMil())

end = time()
print(f'{(end - start):.2f}')
