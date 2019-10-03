# Paths with Sum: You are given a binary tree in which each node contains an integer value (which
# might be positive or negative). Design an algorithm to count the number of paths that sum to a
# given value. The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).

from utils.models.trees import Node
from collections import defaultdict

def count_paths_with_sum(node:Node, target: int):
    return count_paths_with_sum(node, target, 0, defaultdict(lambda: 0))

def count_paths_with_sum(node :Node, target: int, running: int, table:defaultdict):
    if not node: return 0

    running += node.val
    sum = running - target
    total_paths = table[sum]

    if running == target:
        total_paths += 1

    increment_hash_table(table, running, 1)
    total_paths += count_paths_with_sum(node.left, target, running, table)
    total_paths += count_paths_with_sum(node.right, target, running, table)
    increment_hash_table(table, running, -1)

    return total_paths

def increment_hash_table(table: defaultdict, key, delta):
    new_count = table[key] + delta
    if new_count == 0:
        del table[key]
    else:
        table[key] = new_count