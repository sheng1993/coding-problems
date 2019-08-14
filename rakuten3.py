import math

def solve_base_2(B):
    result = []
    for i in range(len(B)):
        result.append(B[i] * (-2)**i)
    return sum(result)

def next(A):
    l = len(A)
    if not A:
        return [0]
    if A[0] == 0:
        A[0] = 1
    else:
        append_last = False
        for i in range(l):
            if A[i] == 0:
                A[i] = 1
                break
            if A[i] == 1:
                if i == l - 1:
                    append_last = True
                A[i] = 0
        if append_last:
            A.append(1)
    return A

def prev(A):
    l = len(A)
    if not A:
        return []
    curr = l - 1
    while A[curr] != 0:
        curr-=1
    if curr == -1:
        A[0] = 0
    else:
        A[curr] = 1
        A[curr + 1] = 0
    return A

def solution(A):
    x = solve_base_2(A)
    ceil = math.ceil(x/2)

    curr = [] if x >= 0 else A

    f = next if x >= 0 else prev
    
    aux = solve_base_2(curr)
    while aux < ceil:
        curr = f(curr)
        aux = solve_base_2(curr)        

    return curr

print(solution([1, 0, 0, 1, 1, 1]))
