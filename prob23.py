# Vaughn Johnson
# very tired, this is going to be shitty code

from prob21 import sum_prop_facts
from itertools import combinations_with_replacement
abundant = []

# TODO cap this number
for i in range(1, 28124 - 12):
    i_fact_sum = sum_prop_facts(i)
    if i_fact_sum > i:
        abundant.append(i)

candidates = set(range(28124))

for pair in combinations_with_replacement(abundant, 2):
    candidates.discard(sum(pair))

print sum(candidates)
