# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if not A:
        return 0
    
    pending = binarian(A)
    result = 0

    while pending > 0:
        p, n = largest_pow_smaller_than(pending)
        pending -= n
        result += 1
    
    return result

def largest_pow_smaller_than(n):
    p = n.bit_length() - 1
    return p, 1 << p

def binarian(A):
    result = 0
    for a in A:
        result += 2**a
    return result

print(solution([1, 5, 4]))