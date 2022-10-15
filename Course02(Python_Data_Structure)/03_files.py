# # Opening a file :-
# file = open('demo.txt')
# print(file)

# count = 0
# for potato in file:
#     print(potato)
#     count = count + 1
# print('Line count = ', count)

# rr = file.read()
# print(len(rr))
# print(rr[:20])

# a = 'Hello.abc@gmail.com'
# if a.endswith('@gmail.com'):
#     cc = a.find('@')
#     print(a[:cc])

# count = 0
# for potato in file:
#     potato = potato.rstrip()
#     print(potato)
#     # if potato.startswith('From:'):
#     #     print(potato)
#     count = count + 1
# print('Line count = ', count)

name_input = input('Enter the name of the file : ')

try:
    file = open(name_input)
except:
    print('Enter a valid file name!')
    quit()

count = 0
for line in file:
    line = line.rstrip()
    print(line)
    count = count +1
print('Line count = ', count)