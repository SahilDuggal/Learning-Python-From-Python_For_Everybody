name_input = input('Enter the name of the file : ')

try:
    file = open(name_input)
except:
    print('Enter a valid file name!')
    quit()

for line in file:
    line = line.upper()
    line = line.rstrip()
    print(line)
