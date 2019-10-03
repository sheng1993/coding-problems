# String Rotation: Assume you have a method i 5Su b 5 tr ing which checks if one word is a substring
# of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
# call to i5Sub5tring (e.g., "waterbottle" is a rotation of" erbottlewat").

def is_rotation(str1, str2):
    len_str1 = len(str1)

    if len_str1 == len(str2) and len > 0:
        s1s1 = str1 + str1
        return is_substring(s1s1, str2)

    return False


def is_substring(str1, str2):
    pass