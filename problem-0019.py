from datetime import datetime
from calendar import day_name


def countingSundays():
    """
    This function calculate how many Sundays fell on the
    first of the month during the twentieth century
    (1 Jan 1901 to 31 Dec 2000)?
    :return:
    """
    cont = 0
    for i in range(1901, 2000 + 1):
        for k in range(1, 12 + 1):
            date = datetime(i, k, 1).weekday()
            weekday = day_name[date]
            if weekday == "Sunday":
                cont += 1
    return print(cont)


countingSundays()
