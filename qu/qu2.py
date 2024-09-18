names_list=input("enter the names").split()
names_set=set(names_list)
names_fset=frozenset(names_set)

names_dict={name:len(name) for name in names_fset}
print(f'origibnal list:{names_list}\n')
print(f'set:{names_set}\n')
print(f'fset:{names_fset}\n')
print(f'dict:{names_dict}\n')

import json

with open('uq2.json','w') as names_db:
    json.dump(names_dict,names_db)# dump :writting to the file.
print("dict written in json")
with open('uq2.json','r') as names_db:
    names_dict2=json.load(names_db)
    print(f'reading from json..\n{names_dict2}')


