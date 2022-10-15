name = input('Enter your name: ')
print('Welcome', name + "!")

inp = int(input('What is your year of birth: '))
currAge = 2022 - inp
print('Currently you are',currAge,'years old')

year_inp = int(input('enter the year you want to see your age: '))

if year_inp > 2022:
    newAge = year_inp - inp
    print('You will be', newAge,'years old.')

elif year_inp < 2022:
    newAge = year_inp - inp
    print('You was',newAge,'years old.')

# file_name = input('Enter the name of file you want to open :')
# A = open(file_name)
# print(A)