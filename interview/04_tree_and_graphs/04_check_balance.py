# Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.

from utils.models.trees import Node
import math

def get_height(root: Node) -> int:
    if not root:
        return -1

    return max(get_height(root.left), get_height(root.right)) + 1

def is_balanced(root: Node) -> bool:
    if not root:
        return True
    
    height_diff = get_height(root.left) - get_height(root.right)
    if abs(height_diff) > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)

def is_balanced_optimal(root: Node):
    return check_height(root) != -math.inf

def check_height(root: Node):
    if not root:
        return -1
    
    left_height = check_height(root.left)
    if left_height == -math.inf:
        return -math.inf
    
    right_height = check_height(root.right)
    if right_height == -math.inf:
        return -math.inf

    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return -math.inf
    else:
        return max(left_height, right_height) + 1

