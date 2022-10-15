# () ---> Parenthesis                                                               |
# ** ---> Power                                                                     |
# *  ---> Multiplication # /  ---> Division     # %  ---> Modular(Remander)         |
# +  ---> Additions      # -  ---> Subtration                                       |
# After that left to right                                                          V

x = 2 + 67 - 4 * 10 / 5 ** 5 % 2            #--->68.9872 
y = ((((2 + 67 - 4) * 10) / 5) ** 5) % 2    #--->0.0
print(x, y)
print(type(x))
print(type(y))
y = int(y)
print(type(y))

a = 'Hello'
b = 'World!'
c = a + ' ' + b
print(c)
type(c)

A = 'Hello World!'
# B = A - '!'
# print(B)

stringg = '123'
intttt = int(stringg)
y = intttt + 1
print(y)