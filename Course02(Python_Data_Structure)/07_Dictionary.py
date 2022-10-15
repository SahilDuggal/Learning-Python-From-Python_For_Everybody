# Programm to take input from user and increase number of repeation

rep = {}
for i in range(10000000):
    name = input("Enter a name: ")
    # if name == 'done':
    #     break
    # else:
    #     if name in rep:
    #         rep[name] = rep[name] +1
    #     else:
    #         rep[name] = 1

    ######################## Other Way #############################

    if name == 'done':
        break
    else:
        rep[name] = rep.get(name,0) +1

print(rep)                                        #print whole dic

print(rep.values())                             #print count of name(in this case)
print(rep.keys())                               #print name
print(zip(rep.values(), rep.keys()))            #zip's both values and store it
print(max(zip(rep.values(), rep.keys())))       #print max zipped value both name and count
print(max(zip(rep.values(), rep.keys()))[0])    #print max count without name
print(max(zip(rep.values(), rep.keys()))[1])    #print max name repeat/count
print(max(rep))                                 #print max in name (comparing alphabets of name)
