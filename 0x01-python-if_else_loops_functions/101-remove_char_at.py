#!/usr/bin/python3
def remove_char_at(str, n):
    str_num = len(str)
    if n < 0 or str_num <= n:
        return (str)
    else:
        string = ""
        for i in range(str_num):
            if i == n:
                continue
            else:
                string += str[i]
        return (string)
