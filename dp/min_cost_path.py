# Min Cost Path
import math


def min_cost_path_recursive(cost, m, n):
    if (n < 0 or m < 0):
        return math.inf
    elif (m == 0 and n == 0):
        return cost[m][n]
    else:
        return cost[m][n] + min(min_cost_path(cost, m-1, n-1),
                                min_cost_path(cost, m-1, n),
                                min_cost_path(cost, m, n-1))


def min_cost_path_dp(cost, m, n):
    tc = [[0 for x in range(n + 1)] for x in range(m + 1)]

    tc[0][0] = cost[0][0]

    for i in range(1, m + 1):
        tc[i][0] = tc[i-1][0] + cost[i][0]
    for j in range(1, n+1):
        tc[0][j] = tc[0][j-1] + cost[0][j]

    for i in range(1, m+1):
        for j in range(1, n+1):
            tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j]

    return tc[m][n]
