from time import time
from itertools import permutations

start = time()


def pandigitalPrime():
    """
    Pandigital prime

    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

    This function return the largest n-digit pandigital prime that exists?
    :return:
    """
    num, l_n, str_n, l_m, cont, n_num1, n_num2 = '1234', [], '', [], 0, 0, ''
    while len(num) <= 9:
        n = permutations(num)
        l = list(n)
        for i in range(0, len(l)):
            for k in range(0, len(l[i])):
                str_n += l[i][k]
            l_n.append(int(str_n))
            for i in range(2, l_n[0]):
                if l_n[0] % i == 0:
                    cont += 1
                    break
            if cont == 0:
                l_m.append(l_n[0])
            str_n = ''
            l_n = []
            cont = 0
            n_num1 = int(num[-1]) + 1
            n_num2 = str(n_num1)
        num += n_num2
    print(max(l_m))


pandigitalPrime()
end = time()
print(f'{(end - start):.2f}')
