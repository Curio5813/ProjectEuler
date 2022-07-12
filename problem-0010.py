from time import time

inicio = time()
def summationOfPrimes():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    This function find the sum of all the primes below two
    million.
    :return: 
    """
    nao_primos, primos = set(), []
    for i in range(2, 2_000_000 + 1):
        if i in nao_primos:
            continue
        for k in range(i * 2, 2_000_000 + 1, i):
            nao_primos.add(k)
        primos.append(i)
    print(sum(primos))


summationOfPrimes()

fim = time()
print(f'{(fim - inicio):.2f}')
