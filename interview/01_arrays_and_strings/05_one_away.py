# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false

def one_edit_away(str1, str2):
    if len(str1) == len(str2):
        return one_edit_replace(str1, str2)
    elif len(str1) == len(str2) + 1:
        return one_edit_insert(str2, str1)
    elif len(str1) + 1 == len(str2):
        return one_edit_insert(str1, str2)
    return False

def one_edit_insert(str1, str2):
    index1 = index2 = 0
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index2 += 1
            index1 += 1
    return True

def one_edit_replace(str1, str2):
    found = False
    for i in range(len(str1)):
        if str1[i] != str[2]:
            if found:
                return False
            found = True
    return True