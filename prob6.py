def first_n_sqares(n):
    for i in range(n+1):
        yield i**2

print sum(range(100 + 1))**2 - sum(first_n_sqares(100))
