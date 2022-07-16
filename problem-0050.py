from time import time

start = time()


def generatePrimeNumbers():
    """
    This function return a list of prime numbers
    :return:
    """
    prime, not_prime, lim = [], set(), 1_000_000
    for i in range(2, lim):
        if i in not_prime:
            continue
        for k in range(i * 2, lim, i):
            not_prime.add(k)
        prime.append(i)
    len(prime)
    return prime


def consecutivePrimeSum(prime):
    """
    The prime 41, can be written as the sum of six consecutive primes:

                        41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime
    below one-hundred.

    The sum of the most the longest sum of consecutive primes below
    one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

    This function return a prime number that can be written as the sum of
    the most consecutive primes below one million.
    :return:
    """
    n, soma, l1, l2 = 0, 0, [], []
    for i in range(5):
        for k in range(n, len(prime)):
            soma += prime[k]
            l1.append(prime[k])
            if soma in prime and soma not in l2:
                l2.append(soma)
            if prime[k] > (len(prime) // 2):
                break
        soma = 0
        n += 1
    print(prime[n])
    print(prime.index(prime[k]) + 1)
    print(max(l2))


consecutivePrimeSum(generatePrimeNumbers())
end = time()
print(f'{(end - start):.2f}')
