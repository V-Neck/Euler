import numpy as np

for a in range(1, 1000):
    for b in range(1, a):
        c = np.sqrt(a**2 + b**2)
        if (int(c) - c) == 0:
            if (a + b + c) == 1000:
                print a, b, c, a*b*c
