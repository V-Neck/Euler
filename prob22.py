from urllib2 import urlopen
from numpy import dot
prod = lambda x: reduce(mul, x)

alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
alphabet = dict(zip(alphabet, range(1, 27)))
names = urlopen("https://projecteuler.net/project/resources/p022_names.txt").read()
names = names.replace("\"", "").split(",")
names = sorted(names)

names = [sum([alphabet[i] for i in name]) for name in names]

print dot(names, range(1, len(names) + 1))
