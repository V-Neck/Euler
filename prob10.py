from math import sqrt

def primes_below_n(n):
    # Check if m is prime
    m = 3
    primes = []
    prime_append = primes.append
    while m < n:
        is_prime = True
        for p in primes:
            if p > sqrt(m):
                break
            if m % p == 0:
                is_prime = False
                break
        if is_prime:
            # Doesn't make sense to use a generator, because you store the list anyway
            prime_append(m)
        m += 2

    # By definition
    return [2] + primes

x = primes_below_n(2*10**6)
sum(x)
