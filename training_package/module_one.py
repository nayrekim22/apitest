# each .py file is a module
# importing modules can be done either by whole module:
import os
# or by importing a specific function from a module:
from os import getcwd

# need to consider which method suits best wrt memory usage

# class name should be in caps
class Method1:
    # define class variables, each instance will have this variable with the set value
    chipset = "intel"

    # initalise the object using __init__
    def __init__(self, device, chipset = chipset):
        # initalise the variables
        self.device = device
        self.chipset = chipset

    # an object instance value can be viewed using print(object.__dict__)

    def print_cwd:
        print("Using the method imported from the os package", format(getcwd()))
        print("Using the method from os.getcwd package", format(os.getcwd()))

    # can also print out help on any module using:
    def print_os_package_help:
        print(help(os))

    # class constructor allow you to provide a simpler way of creating the object
    # Allows a list (or dict) to be paassed in and split out
    # rather than splitting the data and then instantiating the object in the calling code
    @classmethod
    def class_method(cls, new_data):
        router = new_data[0]
        device = new_data[1]
        return cls

# # Parent class
# class Topology():
# #     when a class is imported by a child the code inside main() is NOT imported
#
# # child class can be created based on parent by calling the parent as a parameter
# class Device(Topology):
#     # initalise the child class first
#     def __init__(self):
#         # then initalise the parent
#         def
#
# # get the inheritance path for an object by using
# #     print(help(Device))

# m1 = Method1
# print(m1.chipset)