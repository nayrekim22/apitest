def func(a: "hello", b:"world"):
    """

    :param a: string
    :param b: string
    :return:
    """
    # print("hello world")
    print("hello again")
    print(a)
    print(b)
    c = a + " " + b
    print(c)
    # print(_)
    string_array = c.split(" ")
    print(string_array[0])
    print(string_array[1])
    # print out the values in the string array
    print(string_array[0:2])
    print(string_array[-1])
    # next 2 examples print the same characters starting at the beginning of the string and then the end
    print(a[2:4])
    print(a[-3:-1])
    print(str(a.find('ll')))
    print(len(a))
    print(a.upper().replace("LL", "dd"))
    print(':'.join(string_array))
    print(a.rstrip(), b.lstrip())


func('hello  ', '  world')
