# Lets do some String Manipulations.
# String Concatinations(+)

a = 'Hello'
b = 'World!'
c = a + b
print(c)
# This program will literally concatinate the strings without space 
# To give space in between we will have to :

a = 'Hello'
b = 'World!'
c = a + ' ' + b
print(c)

####################################################################

# Program to see weather a string contains a particular alphabet or not

name = input('Enter your name : ')
if 'a' in name:
    print('True')
else:
    print('False')

####################################################################

# Now let's compare and perform logistic opperations on them

word = input('Enter any fruit name: ')

if word == 'banana':
    print('Everything is going bananassss.')
elif word < 'banana':
    print('Your entered',word,'comes before banana.')
elif word > 'banana':
    print('Your entered',word,'comes after banana.')
else:
    print('Y U Entering numbers ??')

####################################################################
# String Library...

lower = 'heLlo everyone!'
upper = lower

print(lower.lower())
print(upper.upper())
print(dir(lower)) # Actions which can be performed on string.
print(lower.capitalize())

r = lower.replace('heLlo', 'Hola')
print(r)

rep = lower.replace('e','i')
print(rep)

# To remove white space :
say = '     Hello World!    '

print(say.lstrip()) # left strip
print(say.rstrip()) # right strip
print(say.strip())  # strip space from both sides.

# To check if string stsrts with a certain prefix.
line = 'Hello World!'

print(line.startswith('Hello'))
print(line.startswith('h'))

# To get a particular slice of a string.
emil = 'Email Received from sahilmdugga@gmail.com at 09:21 AM on 7th August.'
atpos = emil.find('@')
sppos = emil.find(' ',atpos)
host = emil[atpos+1:sppos]

f_t = emil.find('at')         # position of at before time
spos_t = emil.find(' ',f_t)   # position of ' ' before time
f_d = emil.find('on')         # position of on before date
spos_d = emil.find(' ',f_d)   # position of ' ' before date

tme = emil[spos_t+1:f_d]

dte = emil[spos_d+1:-1]

print('Host = ',host)
print('Time = ',tme)
print('Date = ',dte)

# program to store names of students alphabatically...

ls = []
ele_no = 0

for i in range(10000000):
    name = input('Enter the name of student or done to finish : ')
    if name == 'done':
        break
    else:
        a = name 
        ls.append(a)
        ele_no = i
print(ls)
print(ele_no+1)

print('After the process to get alphabatically...')

ls.sort()
print(ls)
