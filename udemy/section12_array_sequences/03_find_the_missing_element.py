from collections import defaultdict

def finder(arr1, arr2):
    d = defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

def finder2(arr1, arr2):
    result = 0
    for num in arr1 + arr2:
        result ^= num
    
    return result