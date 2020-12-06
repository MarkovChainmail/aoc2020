from collections import Counter

# Exercise A
print(sum(len(set(str.replace("\n",""))) for str in open("questions.txt").read().split("\n\n")))

# Exercise B
print(sum(map(lambda c: len(list(c[v] for v in c if (c[v]>c['\n']))), (Counter(str) for str in open("questions.txt").read()[:-1].split("\n\n")))))