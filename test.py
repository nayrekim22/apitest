print("Python pycharm hands on")
#
print("Varible and object reference")
x = 10
y = x

print("address of x:", id(x))
print("address of y:", id(y))

x = x + 1

print("address of x:", id(x))
print("address of y:", id(y))
_z = y
print("address of _z:", id(_z))

print("String and list")
#
# list1 = ['py charm', 'pydoc', 'py thon']
# list2 = ['IDE', 'module', 'interpreter']
#
# list1 = list1 + list2
# print(list1)
#
# pycharm = list1[0].replace(" ","")
# python = list1[2].replace(" ","")
# print(pycharm, python)
#
# list1[0] = pycharm
# list1[2] = python
#
# print(list1)
#
# list1.reverse()
#
# print(list1)
#
# concat_string = pycharm + " " + python
#
# print("reversing strings")
# print(concat_string[::-1])
# print(''.join(reversed(concat_string)))
#
# removed = list1.pop()
# print("removed: {} from {}".format(removed, list1))
# del list1[0]
#
# print(list1)
#
# list1.append(removed)
# list1.sort()
# print(list1 * 2)
#

print("Dictionary")

# beginners_batch = {}
# for (a, b) in zip(['pycharm','python'], ['2018','3.x']):
#     beginners_batch[a] = b
# print(beginners_batch.items())
#
# for (a, b) in zip(['bgbatch-1', 'bgbatch-2'], ['july-16-20','july-22-27' ]):
#     beginners_batch[a] = b
# print(beginners_batch.items())
#
# beginners_batch['bgbatch-1'] = 'Aug-16-19'
# del beginners_batch['bgbatch-2']
# print(beginners_batch.items())
#
# advanced_batch = dict(beginners_batch)
# print(advanced_batch.items())
#
# beginners_batch.update(advanced_batch)
#
# new_batch = beginners_batch
# beginners_batch['handson'] = 'july-16-20'
#
# print(new_batch.items())
# print(beginners_batch.items())
# print(advanced_batch.items())

print("Tuple")
# tuple_data =  (4, 6, 2, 8, 3, 1)
# # tuple_data[2] = 9
#
# tuple1 = (9,)
# tuple_data = tuple_data + tuple1
# print(tuple_data)
# print(tuple_data[:5])
# tuple_data = tuple_data[:5] + (13,14,15)
# print(tuple_data)
#
# list1 = list(tuple_data)
# list1.append(20)
# tuple_data = tuple(list1)
#
# print(tuple_data)
