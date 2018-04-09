from operator import mul
# Each lattice path for an nxn grid
# requires n moves down and n moves right
#
# Therefore, we need to find all the permutations of
# of 20 down and 20 right
#
# There are 20! number of ways of arranging the
# downs and 20! of arranging the rights
# There are 40! ways of arranging all 40 moves

def fact(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    return reduce(mul, range(1, n+1))

if __name__ == "__main__":
    print fact(40) / (fact(20) * fact(20))
