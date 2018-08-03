import sys

class Filehandler:
    def __init__(self, filename):
        self.filename = filename


    def file_open(filename, file_mode):
        """

        :param filename:
        :return:
        """
        try:
            fobj = open(filename, file_mode)
        except FileNotFoundError as e:
            print("file not found", format(filename))
            sys.exit() # returns -1
        except Exception as e:
            print("caught unknown exception")
        else:
            print("found the file")
            return fobj # return the pointer to the file to the caller


    def print_file_line_by_line(myfile):
        """

        :param myfile:
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
        return file_open(file_name).readlines()


def main():

    myfile = file_open("example.txt")

    print_file_line_by_line(myfile)

    # ensure you close the file
    myfile.close()

    myfileAllLines = file_open("example.txt")
    lines = myfileAllLines.readlines()
    print(lines)

    # can loop through each line
    for line in lines:
        print(line)

    myfileAllLines.close()

    sobj = get_file_as_list_of_strings("example.txt")

    print("{} lines in the file".format(len(sobj)))
    sobj.close()

# if executed from this file then this will run whats in main
# when this file is imported then main is not run but the functions are available
if __name__ == "__main__":
    main()

