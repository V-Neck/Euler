from math import log

N_DIGITS = 10**3

def num_digits(n):
    return log(n)/log(10) + 1


idx = 1
a = 1
b = 1

while num_digits(a) < N_DIGITS:
    idx += 1
    c = a + b
    a = b
    b = c

print idx
