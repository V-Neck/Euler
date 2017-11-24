from math import sqrt

def primes_below_n(n):
    # By definition
    primes = [2]

    # Check if m is prime
    m = 3

    while m < n:
        is_prime = True
        for p in primes:
            if m % p == 0:
                is_prime = False
                break
        if is_prime:
            # Doesn't make sense to use a generator, because you store the list anyway
            primes.append(m)
        m += 2
    return primes

x = primes_below_n(2*10**5)
sum(x)
