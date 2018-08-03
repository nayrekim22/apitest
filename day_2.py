def fun_add(x, y, z):
    x = x + y + z
    return x


def fun_add(x, y):
    x = x + y
    return x


def default_arg(x, y, z =8 ):
    return x + y + z

def fun_add(*args):
    result = 0
    for i in args:
        print(i)
        result = result + i
    return result, i


# passing in dictionaries needs the function parameter to have **
def fun_dict(**keywargs):
    for key, value in keywargs.items():
        print(key, value)


#  function must be called with a double ** when using a dictionary
# dictionary value assigned to the hey using :
keyword1_args = {'pycharm' : 'community 2018', 'python' : '3.x', 'var_type' : 'kwargs_var'}
fun_dict(**keyword1_args)

# execute with a list assigning a value to a variable using =
fun_dict(pycharm ='community 2018', python  ='3.x', var_type  ='kwargs_var')


# print(fun_add(2, 3))
# print(fun_add(2, 3, 4))
# print(default_arg(2, 3))

# num_list = [2,3,5,6,7]
# ret = fun_add(*num_list)
# print(ret)

# print(fun_add((2,3,4,5,6)))
