# Programm to take input from a file and perform functions over dictionary.
fname = input('Enter the name of thr file : ')
fhand = open(fname)
c_dic = dict()

for w in fhand:
    w = w.rstrip()
    words = w.split()
    for word in words:
        c_dic[word]= c_dic.get(word,0)+1
    
print(c_dic)
print(max(zip(c_dic.values(), c_dic.keys())))

################ Other Way to do max(line 13):- ################

bigcount = None
bigword = None
for word,count in c_dic.items():            # word var goes through all keys and count goes through values.
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
    
print(bigcount,bigword)

################################################################################

# now let's convert dictionary to list 
demo = {'chuck':1, 'fred':44, 'jan':100}

print(list(demo)) 
# as list consist of less info. the outputs are only keys not alues.
print(demo.keys())
# to get output of keys only
print(demo.values)
# to get output of values only
print(demo.items())
# to get output of keys and values in a pair (tuple.)

a = None
print(a)
