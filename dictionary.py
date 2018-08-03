# Dictionary is a key value pair
# can't have duplicate keys

dict1 = {'name':'john','age':21,'surname':'doe'}

print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1['name'])

dict_empty = {}
print(dict_empty.items())

dict_empty['language'] = 'python'
print(dict_empty.items())

# copy a dictionary
cp_dict = dict(dict_empty)
print(cp_dict)

cp_dict['version'] = '3'
print(cp_dict)
print(dict_empty)

print(type(dict_empty))
print(type(cp_dict))