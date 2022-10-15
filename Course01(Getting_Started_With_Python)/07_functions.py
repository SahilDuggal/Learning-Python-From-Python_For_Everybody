# def is used to define the function like below "a" is a function
# "()" are used to give additional conditions or operations. 
def a():
    print('Hello')
    print('Sahil here!')

# To call the function we just need to type the name of function with ()
a() # This is calling the function or invoking the function.
print('yup\n')
a()

###################################################################

# Now let's see some other functions:
# max()
# min()

B = max("Sahil Duggal")
print(B)
b = min("Sahil Duggal")
print(b)

C = max(30,50,77,69,65)
print(C)
c = min(30,50,77,69,65)
print(c)

###################################################################

def y(a,b):
    c = a+b
    print(c)

print('Enter the numbers to do addition : ')
a = int(input("Enter 1st no : "))
b = int(input("Enter 2st no : "))
y(a,b)

###################################################################

def add(a,b):
    c = a+b
    print('Output =',c)

def sub(a,b):
    c = a-b
    print('Output =',c)

def mul(a,b):
    c = a*b
    print('Output =',c)

def dev(a,b):
    a = float(a)
    c = a/b
    print('Output =',c)

def mod(a,b):
    c = a%b
    print('Output =',c)

print('Enter the numbers:\n')

a = int(input("Enter 1st no : "))
b = int(input("Enter 2st no : "))

print('\nEnter the opertation you want to perform :')
print('Enter add for addition')
print('Enter sub for substraction')
print('Enter mul for multiplication')
print('Enter dev for division')
print('Enter mod for modular')

opp = input()

if opp == 'add':
    add(a,b)

elif opp == 'sub':
    sub(a,b)

elif opp == 'mul':
    mul(a,b)

elif opp == 'dev':
    dev(a,b)

elif opp == 'mod':
    mod(a,b)

else:
    print('Enter correct opperation...')

###################################################################

def calce(opp):
    if opp == 'add':
        a = int(input("Enter 1st no : "))
        b = int(input("Enter 2st no : "))
        c = a+b
        return c

    elif opp == 'sub':
        a = int(input("Enter 1st no : "))
        b = int(input("Enter 2st no : "))
        c = a-b
        return c

    elif opp == 'mul':
        a = int(input("Enter 1st no : "))
        b = int(input("Enter 2st no : "))
        c = a*b
        return c
        
    elif opp == 'dev':
        a = int(input("Enter 1st no : "))
        b = int(input("Enter 2st no : "))
        c = a/b
        return c
        
    elif opp == 'mol':
        a = int(input("Enter 1st no : "))
        b = int(input("Enter 2st no : "))
        c = a%b
        return c

    else:
        print('Enter correct opperation...')
        
opp = input()
print('Your Output =',calce(opp))
# This can also be dene as :-
uu = calce(opp)
print('Your Output =',uu)

# The functions which returns values are fruitfull functions
# The functions which do not returns values are non-fruitfull functions
