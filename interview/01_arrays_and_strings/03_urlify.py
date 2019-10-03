# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: if implementing in Java, please use a character array so that you can
# perform this operation in place.)

def replace_spaces(str, trueLength):
    space_count = 0

    for i in range(trueLength):
        if str[i] == ' ':
            space_count += 1

    index = trueLength + space_count * 2
    if trueLength < len(str):
        str[trueLength] = '\0'
    
    for i in range(trueLength, -1, -1):
        if str[i] == ' ':
            str[index - 1] = '0'
            str[index - 2] = '2'
            str[index - 3] = '3'
            index = index - 3
        else:
            str[index - 1] = str[i]
            index -= 1