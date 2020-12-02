valid = 0

for line in open('passwords.txt'):
    l = line.replace(":", "").replace("\n","")
    listy = list(l.split(" "))
    listy[0] = [int(i) for i in (listy[0]).split("-")]

    reduced = [s for e, s in enumerate(listy[2]) if e+1 in listy[0]]
    if 1 == reduced.count(listy[1]):
        valid += 1

print(valid)

