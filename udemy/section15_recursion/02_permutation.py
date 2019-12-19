def permute(s: str):
    out = []

    if len(s) == 1:
        out = [s]
    else:
        for i,let in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [let + perm]

    return out

def permute2(a, l, r):
    if l == r:
        print(''.join(a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute2(a, l+1, r)
            a[l], a[i] = a[i], a[l]

x = '123'
arr = [c for c in x]
print(permute2(arr, 0, len(arr) - 1))
print('--------')
print(permute(x))