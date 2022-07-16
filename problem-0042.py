from time import time
from csv import reader

start = time()


def numbers():
    """
    This function return a list from 1 to 26 that is the number of letter
    of latin alphabet
    :return:
    """
    num = []
    for i in range(1, 27):
        num.append(i)
    return num


def alphabet():
    """
    This function return a list of latin alphabet letter.
    :return:
    """
    alph = []
    for k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        alph.append(k)
    return alph


def trianglersNumbers():
    """
    This function return a list of trianglers numbers.
    :return:
    """
    n_t = []
    for i in range(0, 1_000_000):
        tn = (i * (i + 1)) / 2
        n_t.append(int(tn))
    return n_t


def words():
    """
    This function return a list of english word from a csv file.
    :return:
    """
    lt_n = []
    arq = open('words.csv')
    l_w = reader(arq, delimiter=',')
    l_w = list(l_w)
    for i in range(0, len(l_w)):
        for k in range(0, len(l_w[i])):
            lt_n.append(l_w[i][k])
    return lt_n


def codedTriangleNumbers(num, alf, n_t, lt_n):
    """
    Coded triangle numbers

    The nth term of the sequence of triangle numbers is given by,
    tn = ½n(n+1); so the first ten triangle numbers are:

          1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to
    its alphabetical position and adding these values we form a word
    value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
    If the word value is a triangle number then we shall call the word a
    triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16 Kb text
    file containing nearly two-thousand common English words, this functions
    return the numbers triangle words are there.
    :param num:
    :param alf:
    :param n_t:
    :param lt_n:
    :return:
    """
    cont1, cont2 = 0, 0
    for i in range(0, len(lt_n)):
        for k in range(0, len(lt_n[i])):
            letra = lt_n[i][k]
            index_l = alf.index(letra)
            cont1 += num[index_l]
        if cont1 in n_t:
            cont2 += 1
        cont1 = 0
    return print(cont2)


codedTriangleNumbers(numbers(), alphabet(), trianglersNumbers(), words())
end = time()
print(f'{(end - start):.2f}')
