def tenThousandOneStPrime():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
    can see that the 6th prime is 13.

    What is the 10 001st prime number?

    This function return the 1.001 prime number inside of the primes numbers set
    :return:
    """
    nao_primos, primos = set(), []
    for i in range(2, 2_000_000):
        if i in nao_primos:
            continue
        for k in range(i * 2, 2_000_000, i):
            nao_primos.add(k)
        primos.append(i)
    print(primos[10_000])


tenThousandOneStPrime()
