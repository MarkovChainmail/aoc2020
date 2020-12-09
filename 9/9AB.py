from functools import reduce
from itertools import combinations_with_replacement

# Exercise A
# Normally, you would not do this with reduce
# But you have to make some compromises for oneline code
print(next(filter(lambda x: all(a+b!=x[25] for a,b in combinations_with_replacement(x[:25],2)), filter(lambda x: len(x) == 26, reduce(lambda acc,x: acc + [acc[-1] + [x]] if len(acc[-1]) <= 25 else acc + [acc[-1][-25:] + [x]], map(int, open('xmas.txt').read().split("\n")[:-1]), [[]]))))[25])

# Exercise B
# For every step in reduce, test all options in the list, discard non-viable options at every step
# If a valid answer has been found, just return that
print(reduce(lambda acc,x: acc if type(acc)==int else (max(answer[0]) + min(answer[0]) if (answer := list(filter(lambda x: sum(x)==1212510616, acc))) else (list(y+[x] for y in acc) + [[x]])),map(int, open('xmas.txt').read().split("\n")[:-1]), []))
