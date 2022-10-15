name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
c_dic = dict()

for w in handle:
    if w.startswith('From '):
        w = w.rstrip()
        words = w.split()
        word = words[5]
        word = word.split(':')
        word = word[0]
        c_dic[word]= c_dic.get(word,0)+1

ls = list()
for k,v in c_dic.items():
    nT = (k,v)
    ls.append(nT)
ls = sorted(ls, reverse=False)

for k,v in ls:
    print(k,v)