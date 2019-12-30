# Given a list of intergers, write a function that will return a list, in which for each index the
# element will be the product of all the integers except for the element at the index.
# For example, an input of [1,2,3,4] would return [24, 12, 8, 6]

def solution(arr: list):
    total = 1
    for v in arr:
        total *= v
    
    result = []
    for i in range(len(arr)):
        result.append(int(total / arr[i]))
    
    return result

print(solution([1,2,3,4,5]))
