from time import time
from math import factorial

start = time()
def factorialDigitSum():
    """
    Problem 0020 - Factorial digit sum n! means
    n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the
    sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    this function return the sum of the digits in the number 100!
    :return:
    """
    soma = 0
    n = factorial(100)
    str_n = str(n)
    for i in str_n:
        soma += int(i)
    print(soma)


factorialDigitSum()
end = time()
print(f'{(end - start):.2f}')
