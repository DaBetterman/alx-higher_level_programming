def print_reversed_list_integer(my_list=[]):
        new_list = my_list[0:]
        new_list.reverse()
        for i in range(len(new_list)):
            print("{:d}".format(new_list[i]))