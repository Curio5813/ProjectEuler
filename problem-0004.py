def largestPalindromeProduct():
    """
    A palindromic number reads the same both ways. The largest
    palindrome made from the product of two 2-digit numbers is
    9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit
    numbers.

    :return:
    This function return the largest palindrome number made by the
    product of 3-digit number.
    """
    p = []
    for i in range(101, 999 + 1):
        for k in range(101, 999 + 1):
            mult = i * k
            str_p = str(mult)
            if str_p == str_p[::-1]:
                p.append(int(str_p))
    print(max(p))


largestPalindromeProduct()
