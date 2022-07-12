def largestPrimeFactor():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143?

    That function take the number we want and factore it in primes
    factor, the last factor is the largest.
    """
    n, d = 600851475143, 2
    while n > 1:
        if n % d == 0:
            n /= d
        else:
          d += 1
    print(d)


largestPrimeFactor()
