with open("1_1input.txt") as f:
    content = f.readlines()

content = [int(x.strip()) for x in content]

lessthousand = [x for x in content if x < 1000]
morethousand = [x for x in content if x > 1000]

for x in content:
    for y in content:
        for z in content:
            if x + y + z == 2020:
                print(x,y,z)