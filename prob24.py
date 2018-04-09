from prob15 import fact

m = 10**6 -1
alphabet = range(10)
seq = [None] * 10

for i in range(10):
    rollover = fact(len(alphabet) - 1)
    seq[i] = alphabet[(m / rollover)]
    alphabet.pop((m / rollover))
    m %= rollover

print seq
