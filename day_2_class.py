paragraph = """Classes provide a means of bundling data and functionality together. 
Creating a new class creates a new type of object, 
allowing new instances of that type to be made. Each class instance can have attributes 
attached to it for maintaining its state. 
Class instances can also have methods (defined by its class) for modifying its state."""

class Stringoperations:
    # initalise the object first
    def __init__(self, paragraph = paragraph):
        # self.string = string
        self.paragraph = paragraph

    def find_string(self, string):
        # print("Returns the index of {} in {}".format(string, paragraph))
        return paragraph.find(string)

    def split_paragraph(self):
        return paragraph.split('.')

    def replace_string(self, string):
        return paragraph.replace("class", string)

    def join_string(self, strings):
        split_list = paragraph.split('.')
        join_para = strings.join_string(split_list)


# print(help(Stringoperations))
sobj = Stringoperations()

# will print the index the string is found at, otherwise -1
print(sobj.find_string('class'))
print(sobj.find_string('classssssssss'))

# splits = sobj.split_paragraph()
# print(splits)
