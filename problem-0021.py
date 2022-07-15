from time import time

start = time()
def amicableNumbers():
    """
    Amicable numbers

    Let sum(d(n)) be defined as the sum of proper divisors of n
    (numbers less than n which divide evenly into n).
    If sum(d(a)) = b and sum(d(b)) = a, where a ≠ b, then a and b are called
    amicable numbers.

    For example, the proper divisors of 220 are

    1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
    
    The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    This function return the sum of all the amicable numbers under 10.000.
    :return:
    """
    d, l, l1, l2, l3 = 0, [], [], [], []
    for i in range(1, 10_000):
        for k in range(1, 10_000):
            if i % k == 0 and i != k:
                l.append(k)
        l1.append(i)
        l2.append(sum(l))
        l = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1)):
            if l1[i] == l2[k] and l1[k] == l2[i] and l1[i] != l1[k]:
                l3.append(l1[i])
    print(sum(l3))


amicableNumbers()
end = time()
print(f'{(end - start):.2f}')

