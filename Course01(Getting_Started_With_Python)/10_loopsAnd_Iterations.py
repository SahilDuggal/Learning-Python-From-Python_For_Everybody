print('Program to do sum of numbers.')
ls = []
sum = 0

for i in range(0,10000000000000000000000000000000):
    a = input("Enter the number for sum or enter any alphabet to done! ")
    try:
        a = int(a)
        ls.append(a)
    except:
        break

for j in ls:
    sum = sum +j
    
print('Sum of numbers =',sum)

#####################################################################################

print('Program to do average of numbers.')
ls = []
co = 0
sum = 0

for i in range(0,10000000000000000000000000000000):
    a = input("Enter the number for average or enter any alphabet to done! ")
    try:
        a = int(a)
        ls.append(a)
    except:
        break

for j in ls:
    sum = sum +j
    co = co +1

average = sum / co
print('Average of numbers =',average)

#####################################################################################

print('Program to perform filter in loop.')
ls = []

for i in range(0,10000000000000000000000000000000):
    a = input("Enter the number for average or enter any alphabet to done! ")
    try:
        a = int(a)
        ls.append(a)
    except:
        break

for j in ls:
    if j > 20:
        print(j)