fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    spl = line.rstrip().split()
    for ele in spl:
        if ele in lst:
            continue
        else:
            lst.append(ele)
lst.sort()
print(lst)
