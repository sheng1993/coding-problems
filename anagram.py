from itertools import permutations

vowels = {'A', 'E', 'I', 'O', 'U'}

def solution(S):
    if not S:
        return 0

    l = len(S)
    if l <= 1:
        return 0
    
    # Count all characters to check if structured word is possible
    # to avoid going throught all permutations
    if not possibleStructureWords(S):
        return 0
        
    count = 0
    found = set()
    for perm in permutations(S):
        permStr = ''.join(perm)
        if permStr not in found and isAnagram(perm) :
            found.add(permStr)
            count += 1
    return count
    
def isAnagram(s):
    l = len(s)
    if l == 0:
        return False
    if s[0] in vowels:
        return False
    
    for i in range(1, l):
        if i % 2 == 0 and s[i] in vowels:
            return False
        elif i % 2 != 0 and s[i] not in vowels:
            return False
    return True
    
def possibleStructureWords(S):
    l = len(S)
    vowelCount = 0
    nonVowelCount = 0
    for i in range(len(S)):
        if S[i].upper() in vowels:
            vowelCount += 1
        else:
            nonVowelCount += 1
    
    return (vowelCount == nonVowelCount) or (vowelCount == nonVowelCount - 1)

print(solution('AABCY'))