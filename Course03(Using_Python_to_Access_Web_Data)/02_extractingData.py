import re

x = ('My fav2 numbers are 54 and 77')
print(re.findall('[0-9]+',x))
print(re.findall('[AEIOU]+',x))
print(re.findall('[aeiou]+',x))

#............................................................................

x = 'From: Sahil Duggal, at : 7:34:76 AM.'
print(re.findall('^F.+:',x))                # To get the largest output(Greedy Matching)
print(re.findall('^F.+?:',x))               # To get the smallest output(Non-Greedy Matching)

file = open('mbox-short.txt')
for line in file:
    x = re.findall('^From (\S+@\S+)', line)
    if x != []:
        print(x)
    elif x == []:
        continue
########################### Other Way to do above one. ################################
file = open('mbox-short.txt')
for line in file:
    x = re.findall('^From ([^ ]*)', line)
    if x != []:
        print(x)
    elif x == []:
        continue

#............................................................................

file = open('mbox-short.txt')
ls = list()
cont = 0
for line in file:
    line = line.rstrip()
    xtract = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if xtract == []: continue
    val = float(xtract[0])
    ls.append(val)
    cont = cont +1
print('Average =', sum(ls)/cont)

#............................................................................

# If we want to do extraction based of expressions used like $ or ()
x = 'We have $100.00 left. '
print(re.findall('\$[0-9.]+',x))
