def fib(n):
    a, b = 1, 1
    while a + b < n:
        yield a + b
        a, b = b, a + b

def even_n(l):
    for i in l:
        if i % 2 == 0:
            yield i

sum(even_n(fib(4*10**15)))
