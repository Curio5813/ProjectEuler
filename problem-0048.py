from time import time

start = time()


def selfPowers():
    """
    Self powers

    The series, 1¹ + 2² + 3³ + ... + 10¹⁰ = 10405071317.

    This function retudn the last ten digits of the
    series, 1¹ + 2² + 3³ + ... + 1000¹⁰⁰⁰.
    :return:
    """
    soma = 0
    for i in range(1, 1000 + 1):
        soma += i ** i
    str_soma = str(soma)
    str_soma = str_soma[::-1]
    str_soma = str_soma[0:10]
    str_soma = str_soma[::-1]
    print(str_soma)


selfPowers()
end = time()
print(f'{(end - start):.2f}')
