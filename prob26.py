from math import log, exp
from prob3 import factorize

FACTORS_OF_10 = [1, 2, 5]

def contains_other(l, whitelist):
    for item in l:
        if item not in whitelist:
            return True
    return False

def is_repeating_decimal(n):
    return contains_other(factorize(n), FACTORS_OF_10)

for i in range(1, 100):
    if(is_repeating_decimal(i)):
