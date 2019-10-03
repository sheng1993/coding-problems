# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def compress_bad(str1):
    result = []
    countConsecutive = 0
    for i in range(len(str1)):
        countConsecutive += 1

        if i + 1 >= len(str1) or str1[i] != str1[i+1]:
            result.append(str1[i])
            result.append(str(countConsecutive))
            countConsecutive = 0
    
    return ''.join(result) if len(result) < len(str1) else str1

print(compress_bad('aabcccccaaa'))