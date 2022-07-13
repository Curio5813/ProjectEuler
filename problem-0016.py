from time import time

start = time()
def powerDigitSum():
    """
    Power digit sum

    2¹⁵ = 32768 and the sum of its digits
    is 3 + 2 + 7 + 6 + 8 = 26.

    This function return the sum of the digits of
    the number 2¹⁰⁰⁰?
    :return:
    """
    p = 2 ** 1000
    str_p = str(p)
    l = [int(i) for i in str_p]
    print(sum(l))


powerDigitSum()

end = time()
print(f'{(end - start)}')
