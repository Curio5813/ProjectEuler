from time import time

inicio = time()
def specialPythagoreanTriplet():
    """
    A Pythagorean triplet is a set of three natural numbers,
    a < b < c, for which,

                a² + b² = c²

    For example, 3² + 4² = 9 + 16 = 25 = 5².

    This function find the exactly one Pythagorean triplet for
    which a + b + c = 1000, and calculate its product.
    :return:
    """
    l = []
    for i in range(2, 500):
        for k in range(2, 500):
            if k > i:
                break
            for j in range(2, 500):
                if j > k or j > i:
                    break
                if i ** 2 == k ** 2 + j ** 2 and i + k + j == 1000:
                    l.append(i)
                    l.append(k)
                    l.append(j)
                    return print(i * k * j)


specialPythagoreanTriplet()

fim = time()
print(f'{(fim - inicio):.2f}')
