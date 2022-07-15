from time import time
from csv import reader

start = time()


def nameScore():
    """
    Names scores

    Using names.txt (right click and 'Save Link/Target As...'),
    a 46 Kb text file containing over five-thousand first names,
    begin by sorting it into alphabetical order. Then working out
    the alphabetical value for each name, multiply this value by its
    alphabetical position in the list to obtain a name score.


    For example, when the list is sorted into alphabetical order,
    COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
    name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.


    This function return the total of all the name scores in the file?
    :return:
    """
    l, soma, idx, score = [], 0, 0, []
    arq = open('names.csv')
    nomes = reader(arq)
    l1 = list(nomes)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l.append(l1[i][k])
    l.sort()
    l.insert(0, ' ')
    letter = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(0, len(l)):
        for k in range(0, len(l[i])):
            soma += letter.index(l[i][k])
            idx = l.index(l[i])
        prod = idx * soma
        score.append(prod)
        soma = 0
    return print(sum(score))


nameScore()
end = time()
print(f'{(end - start):.2f}')
