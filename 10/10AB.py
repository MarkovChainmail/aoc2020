from collections import Counter
from functools import reduce

# Exercise A: sort, zip adjacent positions, map to difference and count.
print((c := Counter(map(lambda x: x[1]-x[0], zip([0] + (a := sorted(map(int, open('adapters.txt').readlines()))), a + [a[-1]+3]))))[1] * c[3])

# Exercise B: maintain tuples of the different routes, cull tuples that represent unreachable paths
print(reduce(lambda x,y: (culled := [z for z in x if y-z[0] <= 3]) + [(y, sum(map(lambda p: p[1], culled)))], (a := sorted(map(int, open('adapters.txt').readlines()))) + [a[-1] + 3],[(0,1)])[-1][1])