import re

# Exercise A
print(len(list(x for x in [{"byr","iyr","eyr","hgt","hcl","ecl","pid"} - set(text.split(":", 1)[0] for text in re.split('[ \n]',str)) for str in open("passports.txt").read().split("\n\n")] if not x)))

#Exercise B
print(sum(map(lambda x: all([("byr" in x and int(x["byr"]) in range(1920,2003)), "iyr" in x and int(x["iyr"]) in range(2010,2021), "eyr" in x and int(x["eyr"]) in range(2020,2031), "hgt" in x and ((re.match(r'^[0-9]+in$', x["hgt"]) and int(x["hgt"].replace("in","")) in range(59,77)) or (re.match(r'^[0-9]+cm$', x["hgt"]) and int(x["hgt"].replace("cm","")) in range(150,194))), "hcl" in x and re.match(r'^#[0-9a-f]{6}$', x["hcl"]), "ecl" in x and x["ecl"] in {"amb","blu","brn","gry","grn","hzl","oth"}, "pid" in x and (x["pid"].isdigit()) and (len(x["pid"])==9)]), ({k:v for (k,v) in list((tuple(x.split(":"))) for x in re.split('[ \n]' , s) if len(x) > 2)} for s in open("passports.txt").read().split("\n\n")))))