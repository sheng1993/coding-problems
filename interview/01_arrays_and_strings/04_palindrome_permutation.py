# Palindrome Permutation: Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat'; "atc o eta·; etc.)

def isPermutationOfPalindrome(phrase):
    table = buildCharFrequencyTable(phrase)
    return checkMaxOneOdd(table)

def isPermutationOfPalindrome2(phrase):
    countOdd = 0
    table = table = [0 for i in range(ord('z') - ord('a') + 1)]

    for c in phrase:
        x = getCharNumber(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2 == 1:
                countOdd += 1
            else:
                countOdd -= 1

    return countOdd <= 1

def checkMaxOneOdd(table):
    foundOdd = False
    for count in table:
        if count % 2 == 1:
            if foundOdd:
                return False
            foundOdd = True
    
    return True

def getCharNumber(c):
    """
    Map character to a number. Non-leeter characters map to -1
    """
    a = ord('a')
    val = ord(c)
    z = ord('z')
    if a <= val <= z:
        return val - a
    
    return -1

def buildCharFrequencyTable(phrase):
    table = [0 for i in range(ord('z') - ord('a') + 1)]

    for c in phrase:
        x = getCharNumber(c)
        if x != -1:
            table[x] += 1

    return table