import itertools
import math

# A
print([line[(index*3) % (len(line)-1)] for index, line in enumerate(open('toboggan.txt'))].count("#"))

# B
print(math.prod(list(len(list(l)) for _,l in itertools.groupby(filter(lambda x: x[1] == "#", [(e, line[math.floor(((index*directions[0]) /directions[1])) % (len(line)-1)]) for e, directions in enumerate([(1,1), (3,1), (5,1), (7,1), (1,2)]) for index, line in enumerate(open('toboggan.txt')) if (index % directions[1] == 0)]), lambda x: x[0]))))
