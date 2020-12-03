from itertools import combinations_with_replacement

# Exercise A
print([x*y for x,y in combinations_with_replacement([int(x.strip()) for x in open("data.txt").readlines()], 2) if x+y==2020][0])

# Exercise B
print([x*y*z for x,y,z in combinations_with_replacement([int(x.strip()) for x in open("data.txt").readlines()], 3) if x+y+z==2020][0])
