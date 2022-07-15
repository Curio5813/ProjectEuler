from time import time
from csv import reader
from math import factorial

start = time()


def coinSums():
    """
    Coin sums

    In the United Kingdom the currency is made up of pound
    (£) and pence (p). There are eight coins in general
    circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

    It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

    This functions returns how many different ways can £2 be made using
    any number of coins?
    :return:
    """
    soma, n = 0, 1
    arq = open('coin_sums.csv')
    c = reader(arq, delimiter=' ')
    coins = list(c)
    for i in range(0, len(coins)):
        for k in range(0, len(coins[i])):
            coins[i][k] = int(coins[i][k])
            n += 1
    print(coins)


coinSums()

end = time()
print(f'{(end - start):.2f}')
