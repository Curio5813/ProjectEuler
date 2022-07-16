from time import time

start = time()


def doubleBasePalindromes():
    """
    Double-base palindromes

    The decimal number, 585 = 1001001001 (binary), is palindromic
    in both bases.

    This function return the sum of all numbers, less than one million,
    which are palindromic in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not
    include leading zeros.)
    :return:
    """
    cont, l1, l2 = 0, [], []
    for i in range(10, 1_000_000):
        b = bin(i)
        n_b = b[2:]
        r_b = n_b[::-1]
        str_i = str(i)
        r_i = str_i[::-1]
        if r_b == n_b and r_i == str_i:
            l2.append(n_b)
            l1.append(int(str_i))
        s = sum(l1)
    print(*l2)
    print(*l1)
    print(s)


doubleBasePalindromes()

end = time()
print(f'{(end - start):.2f}')
