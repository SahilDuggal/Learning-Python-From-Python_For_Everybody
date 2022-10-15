fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    if line.startswith('From '):
        line = line.split()
        lst.append(line[1])

for ele in lst:
    print(ele)
print("There were",len(lst), "lines in the file with From as the first word")
