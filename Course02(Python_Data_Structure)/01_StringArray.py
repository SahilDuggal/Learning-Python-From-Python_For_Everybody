# In this program we are going to get perticular alphabet(elemet)
# from a word/sentence(string array)

# As we all know that the counting in computer language starts from 0
#             0 1 2 3 4 5
#  Therefor : b a n a n a

fruit = 'banana'
ele = fruit[1]
print(ele)

x = 6
y = fruit[x-1]
print(y)

###################################################################################
# to get the length and a perticular element of the string entered.

name = input('Enter your name : ')
print('Length of eneted string is = ',len(name))

digit_no = int(input('Enter the no of digit you want to know : '))

ele = name[digit_no +1]

print('The',digit_no,'elemet is :',ele)

###################################################################################
# to get a part of string. 

name =  input('Enter your full name : ')
leng = len(name)

dg = int(input('Enter the no of alphabets in your First name : '))

print('Your First name is', name[0:dg])
print('Your Last name is', name[dg+1:leng])

# other way to do the last step can be:-

name =  input('Enter your full name : ')

dg = int(input('Enter the no of alphabets in your First name : '))

print('Your First name is', name[0:dg])
print('Your Last name is', name[dg+1:1000]) #As the name of anyone can't be of more than 1000 alphabets.
 