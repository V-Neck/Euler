#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Vaughn Johnson
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b,
# then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000

from math import sqrt

def sum_prop_facts(n):
    if n < 1:
        raise ValueError
    factors = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i) == 0:
            factors.append(i)
            if i*i != n:
                factors.append(n/i)
    return sum(factors)

N = 10000

if __name__ == "__main__":
    amicables = []

    for n in range(1, N):
        a = sum_prop_facts(n)
        if sum_prop_facts(a) == n and a != n:
            amicables.append(n)

    print sum(amicables)
