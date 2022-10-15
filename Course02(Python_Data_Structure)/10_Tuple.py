# program to sort and get first 10 maximum repreating key 
name = input("Enter file:")
if len(name) < 1:
    name = "romeo.txt"
fh = open(name)
c_dic = dict()

for w in fh:
    w = w.rstrip()
    words = w.split()
    for word in words:
        c_dic[word]= c_dic.get(word,0)+1

ls = list()
for k,v in c_dic.items():
    nT = (v,k)
    ls.append(nT)
ls = sorted(ls, reverse=False)

for v,k in ls[:10]:
    print(k,v)
################# Other Way to do line(14-18)##############
l = sorted([(v,k) for k,v in c_dic.items()])
for i in range(10):
    print(l[i])