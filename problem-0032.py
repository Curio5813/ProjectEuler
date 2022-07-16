from time import time

start = time()


def pandigitalProducts():
    """
    Pandigital products

    We shall say that an n-digit number is pandigital if it makes use
    of all the digits 1 to n exactly once; for example, the 5-digit
    number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254,
    containing multiplicand, multiplier, and product is 1 through 9
    pandigital.

    Thie functions return the sum of all products whose multiplicand/multiplier/product
    identity can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only
    include it once in your sum.
    :return:
    """
    intl, l1, l2, l3 = '', [], [], set()
    for i in range(1, 15_999):
        for k in range(1, 999):
            mult = i * k
            stri = str(i)
            strk = str(k)
            strmult = str(mult)
            if '0' not in stri and '0' not in strk and '0' not in strmult:
                intl += stri
                intl += strk
                intl += strmult
            if '1' in intl and '2' in intl and '3' in intl and '4' in intl and '5' \
                    in intl and '6' in intl and '7' in intl and '8' in intl and '9' \
                    in intl and len(intl) == 9:
                l1.append(int(intl))
                l2.append(int(strmult))
                l3.add(int(strmult))
                intl = ''
            else:
                intl = ''
        l4 = list(l3)
        l4.sort()
    print(l4)
    return print(sum(l4))


pandigitalProducts()

end = time()
print(f'{(end - start):.2f}')
