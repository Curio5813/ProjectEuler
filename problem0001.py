#Find the sum of all the multiples of 3 or 5 below 1000

s = 0
n = 3
while n < 1000:
    if n >= 1000:
        break
    if n % 3 == 0 or n % 5 == 0:
        s = s + n
        n = n + 1
    else:
        n = n + 1
print(s)