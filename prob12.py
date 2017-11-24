from math import sqrt

triangle = lambda x: sum(range(1, x + 1))

def factorize(n):
    factors = []

    for i in range(1, int(sqrt(n)) + 1):
        if (n % i) == 0:
            factors.append(i)
            factors.append(n / i)
    return factors

n = 0
while len(factorize(triangle(n))) < 500:
    n += 1

print triangle(n)
