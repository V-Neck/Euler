import numpy as np
from prob3 import factorize

def cancel(ll):
    l0 = []
    for l in ll:
        for i in l:
            if i in l0:
                l0.remove(i)
        l0.extend(l)
    return l0

primes = []
n = 20

for i in range(2, n + 1):
    primes.append(factorize(i))

np.product(cancel(primes))
