# Validate BST: Implement a function to check if a binary tree is a binary search tree.

from utils.models.trees import Node

def check_bst_min_max(root: Node, min=None, max=None):
    if not root:
        return True
    
    if (not min and root.val <= min) or (not max and root.val > max):
        return False

    if not check_bst_min_max(root.left, min, root.val) or not check_bst_min_max(root.right, root.val, max):
        return False

    return True

last_visited = None
def check_bst_optimal(root: Node):
    global last_visited

    if not root:
        return True
    
    if not check_bst_optimal(root.left):
        return False
    
    if not last_visited and root.val <= last_visited:
        return False
    
    last_visited = root.val
    
    if not check_bst_optimal(root.right):
        return False
    
    return True

def check_bst(root: Node):
    pass

index = 0
def copy_bst(root: Node, array):
    global index
    if not root:
        return
    copy_bst(root.left, array)
    array[index] = root.val
    index += 1
    copy_bst(root.right, array)

def check_bst(root: Node):
    array = [None for _ in 10]
    copy_bst(root, array)
    for i in range(1, 10):
        if array[i] <= array[i - 1]:
            return False
    return True