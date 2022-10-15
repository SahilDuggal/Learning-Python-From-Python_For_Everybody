# Split function by default splits string by space 
fullName = 'Sahil Duggal'
nameSplit = fullName.split()

firtName = nameSplit[0]
lastName = nameSplit[1]

print('First name =',firtName,'\n','Last name =',lastName)

# But when needed the default can be changed to a condition (delimiter)

string = 'One two three, come with me'
string = string.split('e')
print(string)
 