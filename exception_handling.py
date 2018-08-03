def open_file_catch_exception(file_path):
    print("open file in path:", format(file_path))
    try:
        open(file_path)
    except IndexError as e:
        print("index is out of range")
    except Exception as e: # catch all with Exception
        print("this is the exception:", format(e))
    else:
        print("else executes when try passes")
    finally:
        print("finally always executes, this can be used for cleanup")
    #     for example the code to close an opened file could be placed here

    print("Code continues because the exception has been caught and dealt with")

def open_file(file_path):
    open(file_path)

open_file_catch_exception('ffff')

# open_file('fff')