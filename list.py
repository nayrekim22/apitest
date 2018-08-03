char_list = ['a', 'b', 'c']

num_list = [1, 6, 3, 2]

concat_list = char_list + num_list
print(concat_list)

combined_list = ['q', 9, 'w', 8, 'e', 7]

list_of_list = [21, [22, 23], 24]

print(list_of_list[1][1])

# repitition
print(combined_list *2)

# SORTING
print("Sorting example")
print(num_list)
num_list.sort()
print(num_list)

a = 10
b = a
# id allows access to the memory index
print("reference of 'a' before increment {}".format(id(a)))

print("reference of 'b' before increment {}".format(id(b)))

a = a + 1
print("reference of 'a' and 'b' after increment {}, {}".format(id(a), id(b)))

print("values of a and b after increment, a={}, b={}".format(a, b))

# pop - by default deletes the last element of a list and returns the element
print(char_list.pop())
print(char_list)

# tuple - immutable lists
t = (1,2,3,4,5)
t1 = (7,) # single element must have comma to indicate a list, otherwise it would be an int

t3 = t + t1

print(t3)