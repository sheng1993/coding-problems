def editDistanceNaive(str1, str2, m, n):

    if m == 0:
        return n

    if n == 0:
        return m

    # If last characters of the two string are same,
    # nothing to do. Continue
    if str1[m-1] == str2[n-1]:
        return editDistanceNaive(str1, str2, m-1, n-1)

    return min(
        editDistanceNaive(str1, str2, m, n-1),   # Insert
        editDistanceNaive(str1, str2, m-1, n),   # Remove
        editDistanceNaive(str1, str2, m-1, n-1)  # Replace
    )


def editDistanceDP(str1, str2, m, n):
    dp = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:    # Last character of the two
                dp[i][j] = dp[i-1][j-1]     # string are the same
            else:
                dp[i][j] = 1 + min(dp[i][j-1],      # Insert
                                   dp[i-1][j],      # Remove
                                   dp[i-1][j-1])    # Replace

    return dp[m][n]


def editDistanceMemoization(str1, str2, m, n, dp):
    if (m == 0):
        return n

    if (n == 0):
        return m

    if (dp[m-1][n-1] != -1):
        return dp[m-1][n-1]

    if (str1[m-1] == str2[n-1]):
        dp[m-1][n-1] = editDistanceMemoization(str1, str2, m-1, n-1, dp)
        return dp[m-1][n-1]

    dp[m-1][n-1] = 1 + min(editDistanceMemoization(str1, str2, m, n-1, dp),    # Insert
                           editDistanceMemoization(str1, str2, m-1, n, dp),    # Remove
                           editDistanceMemoization(str1, str2, m-1, n-1, dp))  # Replace
    return dp[m-1][n-1]
