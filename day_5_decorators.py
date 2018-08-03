"""
Decorators are used to allow you to replace a parameter with a function.
This is useful when you need to do more processing on a parameter thats passed in
the decorator @<functionName> indicated to python that the function is a decorator

the @<functionName> is then passed as a parameter to the function that's decorated

take a function and return a function
"""

import time

def timing_function(some_function):
    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "time took to run function: " +str((t2 - t1)) + "\n"
    return wrapper

@timing_function
def some_function():
    num_list = []
    for num in (range(0, 1000)):
        num_list.append(num)
    print("\nSum of all numbers: " + str((sum(num_list))))


print(some_function())
