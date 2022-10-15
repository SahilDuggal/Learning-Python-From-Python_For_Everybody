import json
data = '''{
    "name" : "Sahil",
    "phone" : {
        "type" : "intl",
        "number" : "+91 87250 21104"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:' ,info["name"])
print('Hide:' ,info["email"]["hide"])
print(info)

##############################################################

import json
data = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Sahil"
    },
    { "id" : "002",
      "x" : "4",
      "name" : "Nittin"
    }
]'''

info = json.loads(data)
print('User Count:' ,len(info))
for all in info:
    print('\tName', all['name'])
    print('\tID', all['id'])
    print('\tAttribute', all['x'], '\n')
