for i in [5, 4, 3, 2, 1]:
    print(i)
print('Done!!!')

#################################################################

n =  int(input('Enter the number of time you want *'))
ch = '*'
for i in range(n):
    i = i +1
    print(ch*i)

#################################################################

ls = []
noOfFriends = int(input("Enter no. of friends : "))

for i in range (0,noOfFriends):
    a = input('Enter friends name : ')
    ls.append(a)
print(ls)

message = input('Enter the message you want to output : \n')
print('\n')

for i in ls :
    print(message,i)

#################################################################

print('Prgram to check biggest no.')
ls = []
for i in range(0,10000000000000000000000000000000):
    a = input("Enter the elements of list or enter anything to done! ")
    try:
        a = int(a)
        ls.append(a)
    except:
        break

ch = 0
for i in ls:
    if ch < i:
        ch = i
    elif ch > i:
        ch = ch
print('Biggest no. is',ch)

#################################################################

print('Prgram to check smallest no.')
ls = []
for i in range(0,10000000000000000000000000000000):
    a = input("Enter the elements of list or enter anything to done! ")
    try:
        a = int(a)
        ls.append(a)
    except:
        break

ch = 0
for i in ls:
    if ch > i:
        ch = i
    elif ch < i:
        ch = ch
print('Smallest no. is',ch)
