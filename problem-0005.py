def smallestMultiple():
    """
    2520 is the smallest number that can be divided by each of the
    numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible
    by all of the numbers from 1 to 20?

    :return:
    This function return the smallest number that can be divided from 1
    to 20 without any remainder.
    """
    cont = 0
    for i in range(2520, 500_000_000 + 1, 20):
        for k in range(1, 20 + 1):
            if i % k == 0:
                cont += 1
                if cont == 20:
                    return print(i)
            else:
                cont = 0
                break


smallestMultiple()
