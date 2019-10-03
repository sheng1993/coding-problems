# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an
# algorithm to create a binary search tree with minimal height.

from utils.models.trees import Node

def create_minimal_tree(arr) -> Node:
    return create_minimal_tree(arr, 0, len(arr) - 1)

def create_minimal_tree(arr, start, end) -> Node:
    if end < start:
        return None

    mid = (start + end) // 2
    n = Node(arr[mid])
    n.left = create_minimal_tree(arr, start, mid - 1)
    n.right = create_minimal_tree(arr, mid + 1, end)
    return n