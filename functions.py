# function parameters can have defaults set in the function signature
# default paramters should be kept at the end of the signature for pep8 compliance
def hello_world(a="hello", b=123):
    # detect the type of the prameter using type
    print(type(b))
    if type(b) is int:
        print("parameter is an int")
    print(a, b)


# functions can take a variable number of parameters using the * syntax
def variable_args(*var_args):
    # how do you get the parameter type getting passed in??
    result = 0
    mylist = []
    # print(defarg)
    for i in var_args:
        result = result + i
        mylist.append(result)

    # functions can return multiple parameters
    return result, mylist


# passing in dictionaries needs the function parameter to have **
def keyword_args(**keywargs):
    for key, value in keywargs.items():
        print(key, value)



#  function must be called with a double **
keyword1_args = {'first' : '1st', 'second' : '2nd', 'third' : '3rd'}

res = keyword_args(**keyword1_args)


# function call can then modify one or more of the parameters, or just take defaults
# use type in the function to detect the type of parameter passed in
hello_world()

hello_world(a="bonjour")

hello_world(b=999)

# variable typr can be overridden in the call, it will reference a new area in memory
hello_world(b="world")

print("Multiple parameter examples")
# passing in multiple parameters
# # either using multiple parameters
# ret = variable_args(2,3,4,5,6)
# print(ret)
#
# # or by using a list
# var_list = [9,8,7,6,5,4,3,2]
# # function call needs to change to indicate you are passing in a list using *
# ret = variable_args(*var_list)
# print(ret)
