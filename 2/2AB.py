# Exercise A
print(len(list(filter(lambda x: len(x[1]) in range((l := list(map(int, x[0].split("-"))))[0], l[1]+1), [(s[0], "".join(sym for sym in s[2] if sym==s[1])) for s in list([line.replace(":", "").replace("\n","").split(" ") for line in open('passwords.txt')])]))))

# Exercise B
print(len(list(filter(lambda x: len(x)==1, list(["".join(sym for e,sym in enumerate(s[2]) if e+1 in list([int(i) for i in (s[0]).split("-")]) and sym==s[1]) for s in list([line.replace(":", "").replace("\n","").split(" ") for line in open('passwords.txt')])])))))
