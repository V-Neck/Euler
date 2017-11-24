import numpy as np
from math import ceil

def place_values(n):
    values = []
    for place in range(int(np.log10(n)) + 1):
        x = n % 10
        n /= 10
        values.append(x)
    return values

def is_palindrome(n):
    # There must be a faster way·
    return place_values(n) == list(reversed(place_values(n)))

def largest_palindrome_of_2_n_digit_numbers(n):
    largest_seen = 0
    for i in range(10**(n) -1, 10**(n-1) -1, -1):
        for j in range(i, 10**(n-1) -1, -1):
            if is_palindrome(i*j) and i*j > largest_seen:
                largest_seen = i*j
    return largest_seen

largest_palindrome_of_2_n_digit_numbers(3)
