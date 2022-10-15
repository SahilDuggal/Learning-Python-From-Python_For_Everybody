n = input('Enter the condition : ')
n = int(n)

# while function is like if which says:
# while the condition remains true run the code.

while n > 0:
    print(n)
    n = n -1
print('Boom!!!')
print(n)

#####################################################################

n = int(input("Enter the no of repeatations : "))

while n > 0:
    opp = input('Enter the operation you want to perform : ')
    if opp == 'add':
        a = int(input('Enter 1st no. = '))
        b = int(input('Enter 2nd no. = '))
        c = a+b
        print(c)
        n = n -1
    elif opp =='sub':
        a = int(input('Enter 1st no. = '))
        b = int(input('Enter 2nd no. = '))
        c = a-b
        print(c)
        n = n -1
    elif opp =='mul':
        a = int(input('Enter 1st no. = '))
        b = int(input('Enter 2nd no. = '))
        c = a*b
        print(c)
        n = n -1
    elif opp =='div':
        a = float(input('Enter 1st no. = '))
        b = int(input('Enter 2nd no. = '))
        c = a/b
        print(c)
        n = n -1
    elif opp =='mod':
        a = int(input('Enter 1st no. = '))
        b = int(input('Enter 2nd no. = '))
        c = a%b
        print(c)
        n = n -1
    elif opp == 'done':
        break
    else:
        print('Enter valid operation.')
        continue
print('Thank you!!!')

#####################################################################

opp = input('Enter the opperation you want to perform : ')

if opp == '+':
    print('Start entering the numbers :-')
    b = 0
    while 1 > 0:
        c = b
        try:
            a = input()
            a = int(a)
            if a>0:
                b = b + a 
                print('=',b)
        except:
            print('Final answer = ', c)
            print('Thank You !!!')
            break
elif opp == '*':
    print('Start entering the numbers :-')
    b = 1
    while 1 > 0:
        c = b
        try:
            a = input()
            a = int(a)
            if a>0:
                b = b * a 
                print('=',b)
        except:
            print('Final answer = ', c)
            print('Thank You !!!')
            break