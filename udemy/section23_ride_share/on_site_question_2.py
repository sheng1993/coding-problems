# Write a function that given a target amount of money
# and a list of possible coin denominations, return the number of ways,
# to make change for the target amount using the coin denominations

def solution(n, coins):
    arr = [1] + [0]*n

    for coin in coins:
        for i in range(coin, n+1):
            arr[i] += arr[i - coin]

    if n == 0:
        return 0
    else:
        return arr[n]