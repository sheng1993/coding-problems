# Longest Common Subsequence


def lcs_naive(str1, str2, m, n):
    if m == 0 or n == 0:
        return 0
    elif str1[m-1] == str2[n-1]:
        return 1 + lcs_naive(str1, str2, m-1, n-1)
    else:
        return max(lcs_naive(str1, str2, m, n-1),
                   lcs_naive(str1, str2, m-1, n))


def lcs_tabulation(str1, str2):
    m = len(str1)
    n = len(str2)

    L = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])

    return L[m][n]
