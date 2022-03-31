#!/usr/bin/python3
"""Module create_helpers
This module contains helper functions for the method do_create() in
the module console.py
"""


def is_int(s):
    """Tests if a string is convertable to integer.
    Args:
        s (str): String to be tested.
    Returns:
        True if the string is convertable, False otherwise.
    """
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def is_float(s):
    """Tests if a string is convertable to float.
    Args:
        s (str): String to be tested.
    Returns:
        True if the string is convertable, False otherwise.
    """
    try:
        float(s)
        return True
    except Exception:
        return False


def findOccurrences(string, char):
    """Finds the indices of a string where a character occurs.

    Args:
        string (str): String which @char will be looked for
        char (str): a character to be looked for in @string

    Returns:
        A list of indicies where @char is found in @string.
        An empty list if it there's no occurence.
    """
    return [i for i, letter in enumerate(string) if letter == char]


# def splitStrToNewList(s, l):
#     """Takes a string and a list of indicies, and splits
#     the string on the indicies and returns the splitted strings
#     in a list.

#     Args:
#         s (str): String to split
#         l (list): List of indicies to split the string

#     Returns:
#         A list of strings."""
#     splitList = []
#     splitList.append(s[:l[0]])
#     for i, strIndex in enumerate(l):
#         if (i == len(l) - 1):
#             splitList.append(s[strIndex + 1:])
#         else:
#             splitList.append(s[strIndex + 1: l[i + 1]])

#     return splitList


def dictFromList(list):
    """Forms a dictionary from a list of strings.
    Each string is iterated and the key is taken as the string before the equal
    sign and the value is taken as the string after the equal sign. If there's
    no equal sign or the key or value is invalid, it is not added to
    the dictionary.

    Args:
        list (list): List of strings that have keys and values separated
                     by equal signs.
    Returns:
        A dictionary constructed from the string.
    """
    dict = {}
    for i in list:
        param = i.split('=')

        # Go to the next iteration if there's no equal sign in this string
        if (len(param) == 0):
            continue

        key, value = param

        # If the key or value doesn't exist, don't add it to the dictionary
        if len(key) == 0 or len(value) == 0:
            continue
        # If the key (attribute) is not a string, don't add it to the dict
        if is_int(key) or is_float(key):
            continue

        if is_int(value):
            dict[key] = int(value)
        elif is_float(value):
            dict[key] = float(value)
        else:
            if (value[0] == '"'):
                value = value[1:]
            if (value[-1] == '"'):
                value = value[:-1]
            value = value.replace('"', '\"')
            value = value.replace('_', ' ')
            dict[key] = value

    return dict


def test_funcs():
    """Program starts here
    To see how the functions work, execute this function
    """
    # myStr = '= a=b missing_equal_sign missing_value= =missing_key "\
    #     "c="Hollow"_"Knight" integer=1 '\
    #     'float=1.2452 id=0001 name="Beautiful_Sunset" 1="invalid_key"'
    # list = myStr.split(' ')
    # print(list)
    # # Only valid entries are added to the dict from the list
    # print(dictFromList(list))


if __name__ == "__main__":
    test_funcs()
