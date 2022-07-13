from time import time
start = time()

def longestCollatzSequence():
    """
    Longest Collatz Sequence

    The following iterative sequence is defined for the set of positive integers:

            n → n/2 (n is even)

            n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains
    terms. Although it has not been proved yet (Collatz Problem), it is thought
    that all starting numbers finish at 1.

    This function return the number whom has the longest chain of Collatz Sequence
    under one million.

    NOTE: Once the chain starts the terms are allowed to go above one million.
    :return: 
    """
    cont, l1, l2 = 1, [], []
    for i in range(1, 1_000_000):
        l1.append(i)
        while i > 1:
            if i % 2 == 0:
                i = i / 2
                cont += 1
            elif i % 2 == 1:
                i = 3 * i + 1
                cont += 1
        l2.append(cont)
        cont = 1
    print(l1[l2.index(max(l2))])


longestCollatzSequence()

end = time()
print(f'{(end - start):.2f}')
