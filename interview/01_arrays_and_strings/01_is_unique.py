# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

def isUniqueWithHash(str):
    if (len(str) > 128): return False       # ASCII 128 characters or 256 in extended ASCII

    char_set = [False for i in range(128)]

    for i in range(len(str)):
        val = ord(str[i])
        if char_set[val]:
            return False
        char_set[val] = True
    
    return True

def isUnique(str):
    checker = 0
    for i in range(len(str)):
        val = ord(str[i]) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        
        checker |= (1 << val)

    return True