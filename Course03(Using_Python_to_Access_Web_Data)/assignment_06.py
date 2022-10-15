import urllib.request as UR
import json

j_url = input("Enter location: ")
print("Retrieving ", j_url)
data = UR.urlopen(j_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
obj_j = json.loads(data)

sum = 0
total_number = 0

for comment in obj_j["comments"]:
    sum += int(comment["count"])
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)