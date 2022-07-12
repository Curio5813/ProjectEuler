# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find
# the sum of the even-valued terms.

soma = 0
a = 0
p = 1
s = 1
while s <= 4000000:
    s = a
    a = p
    p = a + s
    if s % 2 == 0:
        soma += s
print(soma)
