import numpy as np
import math
large = 600851475143

def is_prime(n):
    if n == 2:
        return True

    for i in range(2, int(np.sqrt(large)) + 1):
        if n % i == 0:
            return False
    return True

def factorize(n):
    factors = []

    if is_prime(n):
        return [n]

    for i in range(2, int(math.sqrt(large)) + 1):
        if (n % i) == 0:
            factors.append(i)
            break
    factors.extend(factorize(n / i))
    return factors

factorize(large)
