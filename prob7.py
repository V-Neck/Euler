from math import sqrt
from prob3 import is_prime

def first_n_primes(n):
    # By definition
    primes = [2]

    # Check if m is prime
    m = 3

    while len(primes) < n:
        is_prime = True
        for p in primes:
            if sqrt(p) > m:
                break
            if m % p == 0:
                is_prime = False
                break
        if is_prime:
            # Doesn't make sense to use a generator, because you store the list anyway
            primes.append(m)
        m += 2
    return primes

if __name__ == "__main__":
    print first_n_primes(10001)[-1]
