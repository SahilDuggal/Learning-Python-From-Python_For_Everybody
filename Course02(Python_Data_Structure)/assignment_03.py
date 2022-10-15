# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
ls =[]

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence:"):
        a = line.startswith("X-DSPAM-Confidence:")
        term = line.find(' ',a)
        value_ext = line[term+1:term+7]
        f_value = float(value_ext)
        ls.append(f_value)

a = 0.0
count = 0
for i in ls:
    a = a + i
    count = count +1

avrg = a/count
print('Average spam confidence:',avrg)
