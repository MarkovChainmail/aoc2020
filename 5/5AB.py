# Exercise A: build a binary number out of the seating instructions, then retrieve the seat id from that
print(max(a*8+b for a, b in ((map(lambda x: int(x, 2), (string[:7], string[7:]))) for string in list(("".join("0" if s in ["F","L"] else "1" for s in line[:-1])) for line in open('seats.txt')))))

# Exercise B: (min and max values 47, 922 found by calling sorted on the whole)
print((set(range(48,922)) - set(a*8+b for a, b in ((map(lambda x: int(x, 2), (string[:7], string[7:]))) for string in list(("".join("0" if s in ["F","L"] else "1" for s in line[:-1])) for line in open('seats.txt'))))).pop())
