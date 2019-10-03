# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.


def is_permutation_with_sort(str1, str2):
    """
    If two string are permutations, then they have the same characters, but in different order.
    """
    if len(str1) != len(str2):
        return False

    str1_s = sorted(str1)
    str2_s = sorted(str2)

    return str1 == str2


def is_permutation_counting_characters(str1, str2):
    """
    Two words with the same character count
    """

    if len(str1) != len(str2):
        return True

    letters = [0 for i in range(128)]   # Asumption 128 characters ASCII

    for c in str1:
        letters[ord(c)] += 1
    
    for c in str2:
        val = ord(c)
        letters[val] -= 1

        if letters[val] < 0:
            return False
    
    return True