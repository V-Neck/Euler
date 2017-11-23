import numpy as np
import math

def is_prime(n):
    if n == 2:
        return True

    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factorize(n):
    factors = []

    if is_prime(n):
        return [n]

    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            factors.append(i)
            break
    factors.extend(factorize(n / i))
    return factors

if __name__ == "__main__":
    large = 600851475143
    print max(factorize(large))
