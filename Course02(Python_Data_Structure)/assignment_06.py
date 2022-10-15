name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
c_dic = dict()

for w in fh:
    if w.startswith('From '):
        w = w.rstrip()
        words = w.split()
        word = words[1]
        c_dic[word]= c_dic.get(word,0)+1

bigcount = None
bigword = None
for word,count in c_dic.items():            
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
    
print(bigword,bigcount)
