#!/usr/bin/python3
def convert_roman(ch):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    return (roman_dict.get(ch, -1))


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return (0)

    conv = 0
    prev_value = 0

    for i in reversed(roman_string):
        cur = convert_roman(i)
        if cur == -1:
            return (0)
        if cur < prev_value:
            conv -= cur
        else:
            conv += cur
        prev_value = cur
    return (conv)
