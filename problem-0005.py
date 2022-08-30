def smallestMultiple():
    """
    This function return the smallest number that can be divided from 1
    to 20 without any remainder.
    :return:
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
