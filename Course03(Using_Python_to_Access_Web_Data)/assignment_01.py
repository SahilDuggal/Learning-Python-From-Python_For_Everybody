import re

file = open('actualData.txt')
ls = list()

for line in file:
    line = line.rstrip()
    xtract = re.findall('([0-9]+)', line)
    # print(xtract)
    if xtract == []: continue
    for i in xtract:
        val = int(i)
        ls.append(val)
# print(ls)
print('Sum =', sum(ls))
