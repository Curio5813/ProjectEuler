def sumSquareDifference():
    """
    The sum of the squares of the first ten natural numbers is,

      1² + 2² + ... + 10² = 385

    The square of the sum of the first ten natural numbers is,

      (1 + 2 + ... + 10)² = 55² = 3025

    Hence the difference between the sum of the squares of the first ten natural
    numbers and the square of the sum is.

        3025 - 385 = 2640

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.

    This function return the value about the difference between the sum of first 100
    squares natural number for the sum of first 100 numbers.
    :return:
    """
    sq1, sq2, = 0, 0
    for i in range(1, 100 + 1):
        sq1 += i
        sq2 += i ** 2
    print(sq1 ** 2 - sq2)


sumSquareDifference()
