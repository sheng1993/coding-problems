# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def largest_sum(arr: list):
    if not arr:
        return 0

    l = len(arr)
    
    if l <= 2:
        return max(arr)
    
    pass

arr = []
assert largest_sum(arr) == 0

arr = [10, 1]
assert largest_sum(arr) == 10

arr = [2, 4, 6, 2, 5]
assert largest_sum(arr) == 13

arr = [5, 1, 1, 5]
assert largest_sum(arr) == 10