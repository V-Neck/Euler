def collatz(n, depth=1):
    if n == 1:
        return depth
    if n % 2 == 0:
        depth = collatz(n / 2, depth+1)
    else:
        depth = collatz(3 * n + 1, depth+1)
    return depth

if __name___ == "__main__":
    largest = 0
    largest_n = 0
    for i in range(1, 10**6):
        if collatz(i) > largest:
            largest = collatz(i)
            largest_n = i

    print largest_n
