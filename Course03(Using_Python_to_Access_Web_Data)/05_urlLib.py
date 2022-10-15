# Instead of Socket we can use 'urllib' to make our lives easier.

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().strip()
    print(words)
    # The output of this does not consist of any headers 
    # as most of the time we don't need one but if we do want it
    # we can ask urllib for it. 
    for word in words:
        counts[word] = counts.get(word, 0) +1
print(counts)

# Code to get the headers 
# headers = dict(connection.getheaders())
