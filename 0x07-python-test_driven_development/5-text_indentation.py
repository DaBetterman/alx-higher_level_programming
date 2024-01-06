#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the input text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    new_list = ['.', '?', ':']
    new_string = ""
    i = 0
    for i in range(len(text)):
        if text[i] not in new_list:
            new_string += text[i]
        else:
            new_string += (text[i] + '\n\n')
            
    print(new_string)
