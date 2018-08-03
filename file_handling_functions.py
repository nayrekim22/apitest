"""
File handling functions
ensure you open a file in the right mode using the file variable, see d3 p5
inputFile = open("data.txt", "r") # opens the file in read only mode, inputFile is the pointer to the first char in the first line

loop throught the file, for example
for line in inputFile:
    print(line)

consider the size of the input file:
- readline() will read one line at a time into memory, you can process the line you need once it's found
- readlines() reads the entire file in to memory as a string array, then lines can be referenced by their index

"""
import sys




# ensure your loop breaks out when eof is found otherwise it will loop back throught the file in an infite loop

def file_open(filename, file_mode):
    """

    :param filename: path to file
    :param file_mode: mode the file will be opened in, red , write etc
    :return:
    """

    try:
        fobj = open(filename, file_mode) # read-only mode
    except FileNotFoundError as e:
        print("file not found", format(filename))
        sys.exit() # returns -1
    except Exception as e:
        print("caught unknown exception")
    else:
        print("found the file")
        return fobj # return the pointer to the file to the caller


def open_file_for_read(filename):
    return file_open(filename, 'r')


def open_file_for_write(filename):
    return file_open(filename, 'w')


def print_file_line_by_line(myfile):
    """

    :param myfile: file object reference
    :return:
    """
    print("in print_file_line_by_line")
    # loop throught the file
    line = myfile.readline()
    while line:
        print(line, end="") # end supresses a new blank line getting added to the output
        line = myfile.readline()

def get_file_as_list_of_strings(file_name):
    """

    :param file_name:
    :return:
    """
    # this leaves the file open, close it from the same place as this is called
    return open_file_for_read(file_name).readlines()


def main():

    myfile = open_file_for_read("example.txt")

    print_file_line_by_line(myfile)

    # ensure you close the file
    myfile.close()

    myfileAllLines = open_file_for_read("example.txt")
    lines = myfileAllLines.readlines()
    print(lines)

    # can loop through each line
    for line in lines:
        print(line)

    myfileAllLines.close()

    sobj = get_file_as_list_of_strings("example.txt")

    print("{} lines in the file".format(len(sobj)))

    wobj = open_file_for_write("output.txt")

    wobj.writelines(sobj)


    sobj.close()

# if executed from this file then this will run whats in main
# when this file is imported then main is not run but the functions are available
if __name__ == "__main__":
    main()

